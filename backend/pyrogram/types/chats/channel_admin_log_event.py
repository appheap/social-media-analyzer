import pyrogram
from pyrogram import raw, types
from ..object import Object


class ChannelAdminLogEvent(Object):

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            event_id: int = None,
            date: int = None,
            user: "types.User" = None,
            action: "types.ChannelAdminLogEventAction" = None,
    ):
        super().__init__(client)

        self.event_id = event_id
        self.date = date
        self.user = user
        self.action = action

    @staticmethod
    async def _parse(client: "pyrogram.Client", event: raw.base.ChannelAdminLogEvent, users: dict, chats: dict):
        if event is None:
            return None

        return ChannelAdminLogEvent(
            client=client,

            event_id=getattr(event, 'id', None),
            date=getattr(event, 'date', None),
            user=types.User._parse(client, users.get(getattr(event, 'user_id', None), None)),
            action=await types.ChannelAdminLogEventAction._parse(client, getattr(event, 'action', None), users, chats),
        )
