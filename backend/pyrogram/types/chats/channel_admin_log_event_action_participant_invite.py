import pyrogram
from pyrogram import raw, types
from .channel_admin_log_event_action import ChannelAdminLogEventAction


class ChannelAdminLogEventActionParticipantInvite(ChannelAdminLogEventAction):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            chat_member: "types.ChatMember" = None,
    ):
        super().__init__(client=client)

        self.chat_member = chat_member

    @staticmethod
    def _parse(client: "pyrogram.Client", action: raw.base.ChannelAdminLogEventAction, users: dict, chats: dict):
        if action is None:
            return None

        return ChannelAdminLogEventActionParticipantInvite(
            client=client,

            chat_member=types.ChatMember._parse(client, getattr(action, 'participant', None), users)
        )
