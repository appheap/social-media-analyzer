import asyncio
import base64
import functools
import hashlib
import os
import struct
from concurrent.futures.thread import ThreadPoolExecutor
from getpass import getpass
from typing import Union, List, Optional, Dict

import pyrogram
from pyrogram import raw
from pyrogram import types
from pyrogram.file_id import FileId, FileType, PHOTO_TYPES, DOCUMENT_TYPES


async def ainput(prompt: str = "", *, hide: bool = False):
    """Just like the built-in input, but async"""
    with ThreadPoolExecutor(1) as executor:
        func = functools.partial(getpass if hide else input, prompt)
        return await asyncio.get_event_loop().run_in_executor(executor, func)


def get_input_media_from_file_id(
        file_id: str,
        expected_file_type: FileType = None
) -> Union["raw.types.InputMediaPhoto", "raw.types.InputMediaDocument"]:
    try:
        decoded = FileId.decode(file_id)
    except Exception:
        raise ValueError(f'Failed to decode "{file_id}". The value does not represent an existing local file, '
                         f'HTTP URL, or valid file id.')

    file_type = decoded.file_type

    if expected_file_type is not None and file_type != expected_file_type:
        raise ValueError(f'Expected: "{expected_file_type}", got "{file_type}" file_id instead')

    if file_type in (FileType.THUMBNAIL, FileType.CHAT_PHOTO):
        raise ValueError(f"This file_id can only be used for download: {file_id}")

    if file_type in PHOTO_TYPES:
        return raw.types.InputMediaPhoto(
            id=raw.types.InputPhoto(
                id=decoded.media_id,
                access_hash=decoded.access_hash,
                file_reference=decoded.file_reference
            )
        )

    if file_type in DOCUMENT_TYPES:
        return raw.types.InputMediaDocument(
            id=raw.types.InputDocument(
                id=decoded.media_id,
                access_hash=decoded.access_hash,
                file_reference=decoded.file_reference
            )
        )

    raise ValueError(f"Unknown file id: {file_id}")


def get_offset_date(dialogs):
    for m in reversed(dialogs.messages):
        if isinstance(m, raw.types.MessageEmpty):
            continue
        else:
            return m.date
    else:
        return 0


def unpack_inline_message_id(inline_message_id: str) -> "raw.types.InputBotInlineMessageID":
    r = inline_message_id + "=" * (-len(inline_message_id) % 4)
    r = struct.unpack("<iqq", base64.b64decode(r, altchars=b"-_"))

    return raw.types.InputBotInlineMessageID(
        dc_id=r[0],
        id=r[1],
        access_hash=r[2]
    )


MIN_CHANNEL_ID = -1002147483647
MAX_CHANNEL_ID = -1000000000000
MIN_CHAT_ID = -2147483647
MAX_USER_ID = 2147483647


def get_raw_peer_id(peer: raw.base.Peer) -> Optional[int]:
    """Get the raw peer id from a Peer object"""
    if isinstance(peer, raw.types.PeerUser):
        return peer.user_id

    if isinstance(peer, raw.types.PeerChat):
        return peer.chat_id

    if isinstance(peer, raw.types.PeerChannel):
        return peer.channel_id

    return None


def get_peer_id(peer: raw.base.Peer) -> int:
    """Get the non-raw peer id from a Peer object"""
    if isinstance(peer, raw.types.PeerUser):
        return peer.user_id

    if isinstance(peer, raw.types.PeerChat):
        return -peer.chat_id

    if isinstance(peer, raw.types.PeerChannel):
        return MAX_CHANNEL_ID - peer.channel_id

    raise ValueError(f"Peer type invalid: {peer}")


def get_peer_type(peer_id: int) -> str:
    if peer_id < 0:
        if MIN_CHAT_ID <= peer_id:
            return "chat"

        if MIN_CHANNEL_ID <= peer_id < MAX_CHANNEL_ID:
            return "channel"
    elif 0 < peer_id <= MAX_USER_ID:
        return "user"

    raise ValueError(f"Peer id invalid: {peer_id}")


def get_channel_id(peer_id: int) -> int:
    return MAX_CHANNEL_ID - peer_id


def btoi(b: bytes) -> int:
    return int.from_bytes(b, "big")


def itob(i: int) -> bytes:
    return i.to_bytes(256, "big")


def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def xor(a: bytes, b: bytes) -> bytes:
    return bytes(i ^ j for i, j in zip(a, b))


def compute_password_hash(algo: raw.types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow,
                          password: str) -> bytes:
    hash1 = sha256(algo.salt1 + password.encode() + algo.salt1)
    hash2 = sha256(algo.salt2 + hash1 + algo.salt2)
    hash3 = hashlib.pbkdf2_hmac("sha512", hash2, algo.salt1, 100000)

    return sha256(algo.salt2 + hash3 + algo.salt2)


# noinspection PyPep8Naming
def compute_password_check(r: raw.types.account.Password, password: str) -> raw.types.InputCheckPasswordSRP:
    algo = r.current_algo

    p_bytes = algo.p
    p = btoi(algo.p)

    g_bytes = itob(algo.g)
    g = algo.g

    B_bytes = r.srp_B
    B = btoi(B_bytes)

    srp_id = r.srp_id

    x_bytes = compute_password_hash(algo, password)
    x = btoi(x_bytes)

    g_x = pow(g, x, p)

    k_bytes = sha256(p_bytes + g_bytes)
    k = btoi(k_bytes)

    kg_x = (k * g_x) % p

    while True:
        a_bytes = os.urandom(256)
        a = btoi(a_bytes)

        A = pow(g, a, p)
        A_bytes = itob(A)

        u = btoi(sha256(A_bytes + B_bytes))

        if u > 0:
            break

    g_b = (B - kg_x) % p

    ux = u * x
    a_ux = a + ux
    S = pow(g_b, a_ux, p)
    S_bytes = itob(S)

    K_bytes = sha256(S_bytes)

    M1_bytes = sha256(
        xor(sha256(p_bytes), sha256(g_bytes))
        + sha256(algo.salt1)
        + sha256(algo.salt2)
        + A_bytes
        + B_bytes
        + K_bytes
    )

    return raw.types.InputCheckPasswordSRP(srp_id=srp_id, A=A_bytes, M1=M1_bytes)


async def parse_text_entities(
        client: "pyrogram.Client",
        text: str,
        parse_mode: str,
        entities: List["types.MessageEntity"]
) -> Dict[str, raw.base.MessageEntity]:
    if entities:
        # Inject the client instance because parsing user mentions requires it
        for entity in entities:
            entity._client = client

        text, entities = text, [await entity.write() for entity in entities]
    else:
        text, entities = (await client.parser.parse(text, parse_mode)).values()

    return {
        "message": text,
        "entities": entities
    }


async def maybe_run_in_executor(func, data, length, loop, *args):
    return (
        func(data, *args)
        if length <= pyrogram.CRYPTO_EXECUTOR_SIZE_THRESHOLD
        else await loop.run_in_executor(pyrogram.crypto_executor, func, data, *args)
    )


async def parse_admin_log_events(
        client: "pyrogram.Client",
        admin_log_results: raw.base.channels.AdminLogResults
) -> List["types.ChannelAdminLogEvent"]:
    users = {i.id: i for i in admin_log_results.users}
    chats = {i.id: i for i in admin_log_results.chats}

    if not admin_log_results.events:
        return types.List()

    parsed_events = []
    for event in admin_log_results.events:
        parsed_event = await types.ChannelAdminLogEvent._parse(client, event, users, chats)
        if parsed_event:
            parsed_events.append(parsed_event)

    return types.List(parsed_events) if len(parsed_events) else types.List()


async def parse_message_views(
        client,
        message_views: "raw.types.messages.MessageViews",
        message_ids: list
) -> List["types.MessageViews"]:
    users = {i.id: i for i in message_views.users}
    chats = {i.id: i for i in message_views.chats}

    if not message_views.views:
        return types.List()

    parsed_views = []
    for message_id, view in zip(message_ids, message_views.views):
        parsed_view = await types.MessageViews._parse(client, message_id, view, users, chats)
        if parsed_view:
            parsed_views.append(parsed_view)

    return types.List(parsed_views)


async def parse_messages(
        client,
        messages: "raw.types.messages.Messages",
        replies: int = 1
) -> List["types.Message"]:
    users = {i.id: i for i in messages.users}
    chats = {i.id: i for i in messages.chats}

    if not messages.messages:
        return types.List()

    parsed_messages = []

    for message in messages.messages:
        parsed_messages.append(await types.Message._parse(client, message, users, chats, replies=0))

    return types.List(parsed_messages)


def parse_deleted_messages(client, update) -> List["types.Message"]:
    messages = update.messages
    channel_id = getattr(update, "channel_id", None)

    parsed_messages = []

    for message in messages:
        parsed_messages.append(
            types.Message(
                message_id=message,
                chat=types.Chat(
                    id=get_channel_id(channel_id),
                    type="channel",
                    client=client
                ) if channel_id is not None else None,
                client=client,
                type='empty',
            )
        )

    return types.List(parsed_messages)


def parse_search_counters(r: List["raw.types.messages.SearchCounter"]) -> List["types.SearchCounter"]:
    parsed_objects = []
    for raw_search_counter in r:
        parsed_objects.append(
            types.SearchCounter._parse(
                raw_obj=raw_search_counter
            )
        )
    return list(filter(lambda obj: obj is not None, parsed_objects))
