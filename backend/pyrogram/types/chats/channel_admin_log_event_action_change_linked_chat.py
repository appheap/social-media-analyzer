import pyrogram
from pyrogram import raw, types
from .channel_admin_log_event_action import ChannelAdminLogEventAction


class ChannelAdminLogEventActionChangeLinkedChat(ChannelAdminLogEventAction):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            prev_value: int = None,
            new_value: int = None,
    ):
        super().__init__(client=client)

        self.prev_value = prev_value
        self.new_value = new_value

    @staticmethod
    def _parse(client: "pyrogram.Client", action: raw.base.ChannelAdminLogEventAction, users: dict, chats: dict):
        if action is None:
            return None

        return ChannelAdminLogEventActionChangeLinkedChat(
            client=client,

            prev_value=getattr(action, 'prev_value', None),
            new_value=getattr(action, 'new_value', None),
        )
