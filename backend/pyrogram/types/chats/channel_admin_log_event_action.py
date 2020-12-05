import pyrogram
from pyrogram import raw, types
from ..object import Object


class ChannelAdminLogEventAction(Object):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

    ):
        super().__init__(client)

    @staticmethod
    async def _parse(client: "pyrogram.Client", action: raw.base.ChannelAdminLogEventAction, users: dict, chats: dict):
        if action is None:
            return None

        if isinstance(action, raw.types.ChannelAdminLogEventActionChangeTitle):
            return types.ChannelAdminLogEventActionChangeTitle._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionChangeAbout):
            return types.ChannelAdminLogEventActionChangeAbout._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionChangeUsername):
            return types.ChannelAdminLogEventActionChangeUsername._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionChangePhoto):
            return types.ChannelAdminLogEventActionChangePhoto._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionToggleInvites):
            return types.ChannelAdminLogEventActionToggleInvites._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionToggleSignatures):
            return types.ChannelAdminLogEventActionToggleSignatures._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionUpdatePinned):
            return types.ChannelAdminLogEventActionUpdatePinned._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionEditMessage):
            return types.ChannelAdminLogEventActionEditMessage._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionDeleteMessage):
            return types.ChannelAdminLogEventActionDeleteMessage._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionParticipantJoin):
            return types.ChannelAdminLogEventActionParticipantJoin._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionParticipantLeave):
            return types.ChannelAdminLogEventActionParticipantLeave._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionParticipantInvite):
            return types.ChannelAdminLogEventActionParticipantInvite._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionParticipantToggleBan):
            return types.ChannelAdminLogEventActionParticipantToggleBan._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionParticipantToggleAdmin):
            return types.ChannelAdminLogEventActionParticipantToggleAdmin._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionChangeStickerSet):
            return await types.ChannelAdminLogEventActionChangeStickerSet._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionTogglePreHistoryHidden):
            return types.ChannelAdminLogEventActionTogglePreHistoryHidden._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionDefaultBannedRights):
            return types.ChannelAdminLogEventActionDefaultBannedRights._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionDefaultBannedRights):
            return types.ChannelAdminLogEventActionDefaultBannedRights._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionStopPoll):
            return types.ChannelAdminLogEventActionStopPoll._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionChangeLinkedChat):
            return types.ChannelAdminLogEventActionChangeLinkedChat._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionChangeLocation):
            return types.ChannelAdminLogEventActionChangeLocation._parse(client, action, users, chats)

        elif isinstance(action, raw.types.ChannelAdminLogEventActionToggleSlowMode):
            return types.ChannelAdminLogEventActionToggleSlowMode._parse(client, action, users, chats)

        else:
            return None
