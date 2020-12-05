import pyrogram
from pyrogram import raw, types
from .channel_admin_log_event_action import ChannelAdminLogEventAction


class ChannelAdminLogEventActionParticipantToggleBan(ChannelAdminLogEventAction):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            prev_chat_member: "types.ChatParticipant" = None,
            new_chat_member: "types.ChatParticipant" = None,
    ):
        super().__init__(client=client)

        self.prev_chat_member = prev_chat_member
        self.new_chat_member = new_chat_member

    @staticmethod
    def _parse(client: "pyrogram.Client", action: raw.base.ChannelAdminLogEventAction, users: dict, chats: dict):
        if action is None:
            return None

        return ChannelAdminLogEventActionParticipantToggleBan(
            client=client,

            prev_chat_member=types.ChatParticipant._parse(client, getattr(action, 'prev_participant', None), users),
            new_chat_member=types.ChatParticipant._parse(client, getattr(action, 'new_participant', None), users)
        )
