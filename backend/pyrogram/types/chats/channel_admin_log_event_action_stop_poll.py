import pyrogram
from pyrogram import raw, types
from .channel_admin_log_event_action import ChannelAdminLogEventAction


class ChannelAdminLogEventActionStopPoll(ChannelAdminLogEventAction):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            message: "types.Message" = None,
    ):
        super().__init__(client=client)

        self.message = message

    @staticmethod
    def _parse(client: "pyrogram.Client", action: raw.base.ChannelAdminLogEventAction, users: dict, chats: dict):
        if action is None:
            return None

        return ChannelAdminLogEventActionStopPoll(
            client=client,

            message=types.Message._parse(client, getattr(action, 'message', None), users, chats),
        )
