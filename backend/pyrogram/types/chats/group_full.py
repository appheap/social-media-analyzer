from typing import List

from ..object import Object
from pyrogram import raw
from pyrogram import types
import pyrogram


class GroupFull(Object):
    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            id: int = None,
            can_set_username: bool,
            has_scheduled: bool = None,
            about: str = None,
            members: List["types.GroupParticipant"] = None,
            chat_photo: "types.ChatPhoto" = None,
            notify_settings: "types.PeerNotifySettings" = None,
            invite_link: str = None,
            bot_infos: List["types.BotInfo"] = None,
            pinned_message: "types.Message" = None,
            folder_id: int = None,
    ):
        super().__init__(client)

        self.id = id
        self.can_set_username = can_set_username
        self.has_scheduled = has_scheduled
        self.about = about
        self.members = members
        self.chat_photo = chat_photo
        self.notify_settings = notify_settings
        self.invite_link = invite_link
        self.bot_infos = bot_infos
        self.pinned_message = pinned_message
        self.folder_id = folder_id

    @staticmethod
    async def _parse(client, chat_full: "raw.types.ChatFull", users: dict, chats: dict):
        if chat_full is None:
            return None

        peer_id = -chat_full.id

        return GroupFull(
            client=client,

            id=peer_id,
            can_set_username=getattr(chat_full, 'can_set_username', None),
            has_scheduled=getattr(chat_full, 'has_scheduled', None),
            about=getattr(chat_full, 'about', None),
            members=types.List(
                [types.GroupParticipant._parse(client, r, users) for r in
                 getattr(chat_full.participants, 'participants', [])]) or None,
            chat_photo=types.Photo._parse(client, getattr(chat_full, "chat_photo", None)),
            notify_settings=types.PeerNotifySettings._parse(client, getattr(chat_full, 'notify_settings', None)),
            invite_link=chat_full.exported_invite.link if isinstance(chat_full.exported_invite,
                                                                     raw.types.ChatInviteExported) else None,
            bot_infos=types.List(
                [types.BotInfo._parse(client, r) for r in getattr(chat_full, 'bot_info', [])]) or None,

            pinned_message=await client.get_messages(
                peer_id,
                message_ids=chat_full.pinned_msg_id
            ) if getattr(chat_full, 'pinned_msg_id', None) else None,
            folder_id=getattr(chat_full, 'folder_id', None),
        )
