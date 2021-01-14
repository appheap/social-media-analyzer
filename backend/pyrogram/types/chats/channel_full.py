from typing import List, Optional

import pyrogram
from pyrogram import utils, raw, types
from ..object import Object


class ChannelFull(Object):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            id: int = None,
            can_view_participants: bool = None,
            can_set_username: bool = None,
            can_set_stickers: bool = None,
            is_prehistory_hidden: bool = None,
            can_set_location: bool = None,
            has_scheduled: bool = None,
            can_view_stats: bool = None,
            is_blocked: bool = None,
            about: str = None,
            members_count: int = None,
            admins_count: int = None,
            kicked_count: int = None,
            banned_count: int = None,
            online_count: int = None,
            read_inbox_max_id: int = None,
            read_outbox_max_id: int = None,
            unread_count: int = None,
            chat_photo: "types.Photo" = None,
            notify_settings: "types.PeerNotifySettings" = None,
            invite_link: str = None,
            bot_infos: List["types.BotInfo"] = None,
            migrated_from: "types.Chat" = None,
            migrated_from_max_id: int = None,
            pinned_message: "types.Message" = None,
            stickerset: "types.StickerSet" = None,
            min_available_message_id: int = None,
            folder_id: int = None,
            linked_chat: Optional["types.Chat"] = None,
            location: "types.ChannelLocation" = None,
            slowmode_seconds: int = None,
            slowmode_next_send_date=None,
            stats_dc: int = None,
            pts: int = None,
    ):
        super().__init__(client)

        self.id = id
        self.can_view_participants = can_view_participants
        self.can_set_username = can_set_username
        self.can_set_stickers = can_set_stickers
        self.is_prehistory_hidden = is_prehistory_hidden
        self.can_set_location = can_set_location
        self.has_scheduled = has_scheduled
        self.can_view_stats = can_view_stats
        self.is_blocked = is_blocked
        self.about = about
        self.members_count = members_count
        self.admins_count = admins_count
        self.kicked_count = kicked_count
        self.banned_count = banned_count
        self.online_count = online_count
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.unread_count = unread_count
        self.chat_photo = chat_photo
        self.notify_settings = notify_settings
        self.invite_link = invite_link
        self.bot_infos = bot_infos
        self.migrated_from = migrated_from
        self.migrated_from_max_id = migrated_from_max_id
        self.pinned_message = pinned_message
        self.stickerset = stickerset
        self.min_available_message_id = min_available_message_id
        self.folder_id = folder_id
        self.linked_chat = linked_chat
        self.location = location
        self.slowmode_seconds = slowmode_seconds
        self.slowmode_next_send_date = slowmode_next_send_date
        self.stats_dc = stats_dc
        self.pts = pts

    @staticmethod
    async def _parse(client: "pyrogram.Client", channel_full: raw.types.ChannelFull, users, chats):
        if channel_full is None:
            return None

        peer_id = utils.get_channel_id(channel_full.id)
        raw_linked_chat = chats.get(getattr(channel_full, 'linked_chat_id', None), None)
        if raw_linked_chat:
            linked_chat = await types.Chat._parse_chat(client, raw_linked_chat)
        else:
            linked_chat = None

        migrated_from = None
        if getattr(channel_full, 'migrated_from_chat_id'):
            chat = chats.get(getattr(channel_full, 'migrated_from_chat_id', None), None)
            if chat:
                migrated_from = await types.Chat._parse_chat(client, chat)

        return ChannelFull(
            client=client,

            id=peer_id,
            can_view_participants=getattr(channel_full, 'can_view_participants', None),
            can_set_username=getattr(channel_full, 'can_set_username', None),
            can_set_stickers=getattr(channel_full, 'can_set_stickers', None),
            is_prehistory_hidden=getattr(channel_full, 'hidden_prehistory', None),
            can_set_location=getattr(channel_full, 'can_set_location', None),
            has_scheduled=getattr(channel_full, 'has_scheduled', None),
            can_view_stats=getattr(channel_full, 'can_view_stats', None),
            is_blocked=getattr(channel_full, 'blocked', None),
            about=getattr(channel_full, 'about', None),
            members_count=getattr(channel_full, 'participants_count', None),
            admins_count=getattr(channel_full, 'admins_count', None),
            kicked_count=getattr(channel_full, 'kicked_count', None),
            banned_count=getattr(channel_full, 'banned_count', None),
            online_count=getattr(channel_full, 'online_count', None),
            read_inbox_max_id=getattr(channel_full, 'read_inbox_max_id', None),
            read_outbox_max_id=getattr(channel_full, 'read_outbox_max_id', None),
            unread_count=getattr(channel_full, 'unread_count', None),
            chat_photo=types.Photo._parse(client, getattr(channel_full, "chat_photo", None)),
            notify_settings=types.PeerNotifySettings._parse(client, getattr(channel_full, 'notify_settings', None)),
            pinned_message=await client.get_messages(
                peer_id,
                channel_full.pinned_msg_id
            ) if getattr(channel_full, 'pinned_msg_id') else None,
            invite_link=channel_full.exported_invite.link if isinstance(channel_full.exported_invite,
                                                                        raw.types.ChatInviteExported) else None,
            bot_infos=types.List(
                [types.BotInfo._parse(client, r) for r in getattr(channel_full, 'bot_info', [])]) or None,
            migrated_from=migrated_from,
            migrated_from_max_id=getattr(channel_full, 'migrated_from_max_id', None),
            stickerset=types.StickerSet._parse(client, getattr(channel_full, 'stickerset', None)),
            min_available_message_id=getattr(channel_full, 'available_min_id', None),
            folder_id=getattr(channel_full, 'folder_id', None),
            linked_chat=linked_chat,
            location=types.ChannelLocation._parse(client, getattr(channel_full, 'location', None)),
            slowmode_seconds=getattr(channel_full, 'slowmode_seconds', None),
            slowmode_next_send_date=getattr(channel_full, 'slowmode_next_send_date', None),
            stats_dc=getattr(channel_full, 'stats_dc', None),
            pts=getattr(channel_full, 'pts', None),
        )
