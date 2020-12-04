from typing import Union, List

from ..object import Object
import pyrogram
from pyrogram import raw, types, utils

import logging

log = logging.getLogger(__name__)


class MessageReplies(Object):
    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            comments: Union[None, int] = None,
            replies: int = None,
            replies_pts: int = None,
            recent_repliers: Union[None, List["types.User"]] = None,
            channel_id: Union[None, int] = None,
            max_id: Union[None, int] = None,
            read_max_id: Union[None, int] = None,
    ):
        super().__init__(client)

        self.comments = comments
        self.replies = replies
        self.replies_pts = replies_pts
        self.recent_repliers = recent_repliers
        self.channel_id = channel_id
        self.max_id = max_id
        self.read_max_id = read_max_id

    @staticmethod
    async def _parse(client: "pyrogram.Client", message_replies: raw.base.MessageReplies, users: dict, chats: dict):
        if message_replies is None:
            return None

        def get_replier(peer: "raw.base.Peer"):
            if peer is None:
                return None
            if isinstance(peer, raw.types.PeerUser):
                return users.get(peer.user_id, None)
            elif isinstance(peer, raw.types.PeerChat):
                return chats.get(peer.chat_id, None)
            elif isinstance(peer, raw.types.PeerChannel):
                return chats.get(peer.channel_id, None)

        return MessageReplies(
            client=client,

            comments=getattr(message_replies, 'comments', None),
            replies=getattr(message_replies, 'replies', None),
            replies_pts=getattr(message_replies, 'replies_pts', None),
            recent_repliers=types.List([types.User._parse(client, get_replier(peer)) for peer in
                                        getattr(message_replies, 'recent_repliers', [])]) or None,
            channel_id=getattr(message_replies, 'channel_id', None),
            max_id=getattr(message_replies, 'max_id', None),
            read_max_id=getattr(message_replies, 'read_max_id', None),
        )
