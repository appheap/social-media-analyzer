import pyrogram
from pyrogram import raw, types
from .channel_admin_log_event_action import ChannelAdminLogEventAction


class ChannelAdminLogEventActionEditMessage(ChannelAdminLogEventAction):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            prev_message: "types.Message" = None,
            new_message: "types.Message" = None,
    ):
        super().__init__(client=client)

        self.prev_message = prev_message
        self.new_message = new_message

    @staticmethod
    def _parse(client: "pyrogram.Client", action: raw.base.ChannelAdminLogEventAction, users: dict, chats: dict):
        if action is None:
            return None

        return ChannelAdminLogEventActionEditMessage(
            client=client,

            prev_message=types.Message._parse(client, getattr(action, 'prev_message', None), users, chats),
            new_message=types.Message._parse(client, getattr(action, 'new_message', None), users, chats),
        )
