from pyrogram import raw, types as tg_types

from ..object import Object

import telegram.client as tg


class UserFull(Object):
    def __init__(
            self,
            *,
            client: "tg.Client" = None,
            blocked: bool = None,
            phone_calls_available: bool = None,
            video_calls_available: bool = None,
            phone_calls_private: bool = None,
            can_pin_message: bool = None,
            has_scheduled: bool = None,
            user: "tg_types.User" = None,
            about: str = None,
            settings: "tg_types.PeerSettings" = None,
            profile_photo: "tg_types.Photo" = None,
            notify_settings: "tg_types.PeerNotifySettings" = None,
            bot_info: "tg_types.BotInfo" = None,
            pinned_message: "tg_types.Message" = None,
            common_chats_count: int = None,
            folder_id: int = None,
    ):
        super().__init__(client)

        self.blocked = blocked
        self.phone_calls_available = phone_calls_available
        self.video_calls_available = video_calls_available
        self.phone_calls_private = phone_calls_private
        self.can_pin_message = can_pin_message
        self.has_scheduled = has_scheduled
        self.user = user
        self.about = about
        self.settings = settings
        self.profile_photo = profile_photo
        self.notify_settings = notify_settings
        self.bot_info = bot_info
        self.pinned_message = pinned_message
        self.common_chats_count = common_chats_count
        self.folder_id = folder_id

    @staticmethod
    async def _parse(client, user_full: "raw.types.UserFull"):
        return UserFull(
            client=client,
            blocked=getattr(user_full, 'blocked', None),
            user=tg_types.User._parse(client, user_full.user),
            phone_calls_available=getattr(user_full, 'phone_calls_available', None),
            video_calls_available=getattr(user_full, 'video_calls_available', None),
            phone_calls_private=getattr(user_full, 'phone_calls_private', None),
            can_pin_message=getattr(user_full, 'can_pin_message', None),
            has_scheduled=getattr(user_full, 'has_scheduled', None),
            about=getattr(user_full, 'about', None),
            settings=tg_types.PeerSettings._parse(client, getattr(user_full, 'settings', None)),
            profile_photo=tg_types.ChatPhoto._parse(
                client,
                user_full.profile_photo,
                user_full.user.id,
                user_full.user.access_hash,
            ),
            notify_settings=tg_types.PeerNotifySettings._parse(client, getattr(user_full, 'notify_settings')),
            bot_info=tg_types.BotInfo._parse(client, getattr(user_full, 'bot_info', None)),
            pinned_message=await client.get_messages(
                user_full.user.id,
                message_ids=user_full.pinned_msg_id
            ) if getattr(user_full, 'pinned_msg_id', None) else None,
            common_chats_count=getattr(user_full, 'common_chats_count', None),
            folder_id=getattr(user_full, 'folder_id', None),
        )
