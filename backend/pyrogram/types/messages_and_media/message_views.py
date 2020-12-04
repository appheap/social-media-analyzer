from typing import Union
import pyrogram
from pyrogram import raw, types

from ..object import Object


class MessageViews(Object):
    def __init__(
            self,
            *,
            client: "pyrogram.Client",
            message_id: int = None,
            views: Union[None, int,] = None,
            forwards: Union[None, int] = None,
            replies: Union[None, "types.MessageReplies"]
    ):
        super().__init__(client)

        self.message_id = message_id
        self.views = views
        self.forwards = forwards
        self.replies = replies

    @staticmethod
    async def _parse(client, message_id, message_views: raw.base.MessageViews, users: dict, chats: dict):
        if message_views is None:
            return None

        return MessageViews(
            client=client,

            message_id=message_id,
            views=getattr(message_views, 'views', None),
            forwards=getattr(message_views, 'forwards', None),
            replies=await types.MessageReplies._parse(client, getattr(message_views, 'replies', None), users, chats),
        )
