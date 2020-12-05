import pyrogram
from pyrogram import raw, types
from .channel_admin_log_event_action import ChannelAdminLogEventAction


class ChannelAdminLogEventActionParticipantJoin(ChannelAdminLogEventAction):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

    ):
        super().__init__(client=client)

    @staticmethod
    def _parse(client: "pyrogram.Client", action: raw.base.ChannelAdminLogEventAction, users: dict, chats: dict):
        if action is None:
            return None

        return ChannelAdminLogEventActionParticipantJoin(
            client=client,
        )
