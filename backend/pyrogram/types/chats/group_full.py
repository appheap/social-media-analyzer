from typing import List

from ..object import Object


class GroupFull(Object):
    def __init__(
            self,
            *,
            client: "Client" = None,
            id: int = None,
            can_set_username: bool,
            has_scheduled: bool = None,
            about: str = None,
            members: List["GroupParticipant"] = None,
            chat_photo: "ChatPhoto" = None,
            notify_settings: "PeerNotifySettings" = None,
            invite_link: str = None,
            bot_infos: List["BotInfo"] = None,
            pinned_message_id: int = None,
            folder_id: int = None
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
        self.pinned_message_id = pinned_message_id
        self.folder_id = folder_id
