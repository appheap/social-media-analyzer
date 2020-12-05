import pyrogram
from pyrogram import raw, types
from .channel_admin_log_event_action import ChannelAdminLogEventAction


class ChannelAdminLogEventActionTogglePreHistoryHidden(ChannelAdminLogEventAction):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            new_value: bool = None,
    ):
        super().__init__(client=client)

        self.new_value = new_value

    @staticmethod
    def _parse(client: "pyrogram.Client", action: raw.base.ChannelAdminLogEventAction, users: dict, chats: dict):
        if action is None:
            return None

        return ChannelAdminLogEventActionTogglePreHistoryHidden(
            client=client,

            new_value=getattr(action, 'new_value', None),
        )
