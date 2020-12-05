import pyrogram
from pyrogram import raw, types
from .channel_admin_log_event_action import ChannelAdminLogEventAction


class ChannelAdminLogEventActionDefaultBannedRights(ChannelAdminLogEventAction):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            prev_banned_rights: "types.ChatPermissions" = None,
            new_banned_rights: "types.ChatPermissions" = None,
    ):
        super().__init__(client=client)

        self.prev_banned_rights = prev_banned_rights
        self.new_banned_rights = new_banned_rights

    @staticmethod
    def _parse(client: "pyrogram.Client", action: raw.base.ChannelAdminLogEventAction, users: dict, chats: dict):
        if action is None:
            return None

        return ChannelAdminLogEventActionDefaultBannedRights(
            client=client,

            prev_banned_rights=types.ChatPermissions._parse(getattr(action, 'prev_banned_rights', None)),
            new_banned_rights=types.ChatPermissions._parse(getattr(action, 'new_banned_rights', None)),
        )
