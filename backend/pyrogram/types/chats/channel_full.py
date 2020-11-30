from ..object import Object


class ChannelFull(Object):
    def __init__(
            self,
            *,
            client: "Client" = None,
            id: int = None,
            about: str = None,
            members_count: int = None,
            admins_count: int = None,
            kicked_count: int = None,
            banned_count: int = None,
            online_count: int = None,
            unread_count: int = None,
            chat_photo: "ChatPhoto" = None,
            notify_settings: "PeerNotifySettings",
            invite_link: str = None,
            migrated_from: "Group" = None,
            migrated_from_max_id: int = None,
            pinned_message_id: int = None,
            stickerset: "" = None,
            min_available_message_id: int = None,
            folder_id: int = None,
            linked_chat: "" = None,
            location: "" = None,
            slowmode_seconds: int = None,
            slowmode_next_send_date=None,
            stats_dc: int = None,
            pts: int = None,
            can_view_participants: bool = None,
            can_set_username: bool = None,
            can_set_stickers: bool = None,
            is_prehistory_hidden: bool = None,
            can_set_location: bool = None,
            has_scheduled: bool = None,
            can_view_stats: bool = None,
            is_blocked: bool = None,

    ):
        super().__init__(client)
        self.id = id
        self.about = about
        self.members_count = members_count
        self.admins_count = admins_count
        self.kicked_count = kicked_count
        self.banned_count = banned_count
        self.online_count = online_count
        self.unread_count = unread_count
        self.chat_photo = chat_photo
        self.notify_settings = notify_settings
        self.invite_link = invite_link
        self.migrated_from = migrated_from
        self.migrated_from_max_id = migrated_from_max_id
        self.pinned_message_id = pinned_message_id
        self.stickerset = stickerset
        self.min_available_message_id = min_available_message_id
        self.folder_id = folder_id
        self.linked_chat = linked_chat
        self.location = location
        self.slowmode_seconds = slowmode_seconds
        self.slowmode_next_send_date = slowmode_next_send_date
        self.stats_dc = stats_dc
        self.pts = pts
        self.can_view_participants = can_view_participants
        self.can_set_username = can_set_username
        self.can_set_stickers = can_set_stickers
        self.is_prehistory_hidden = is_prehistory_hidden
        self.can_set_location = can_set_location
        self.has_scheduled = has_scheduled
        self.can_view_stats = can_view_stats
        self.is_blocked = is_blocked
