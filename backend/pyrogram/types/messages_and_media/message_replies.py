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

            comments: Union[None, bool] = None,
            replies: int = None,
            replies_pts: int = None,
            recent_repliers: Union[None, List[Union["types.Chat", "types.User"]]] = None,
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
                return None, None
            if isinstance(peer, raw.types.PeerUser):
                return users.get(peer.user_id, None), 'user'
            elif isinstance(peer, raw.types.PeerChat):
                return chats.get(peer.chat_id, None), 'group'
            elif isinstance(peer, raw.types.PeerChannel):
                return chats.get(peer.channel_id, None), 'channel'

        recent_repliers = None
        if message_replies.recent_repliers:
            parsed_peers = []
            for peer in message_replies.recent_repliers:
                _peer, _type = get_replier(peer)
                if peer is None and _type is None:
                    continue

                if _type == 'user':
                    parsed_peer = types.User._parse(client, _peer)
                else:
                    parsed_peer = await types.Chat._parse_chat(client, _peer)

                if parsed_peer:
                    parsed_peers.append(parsed_peer)

            if len(parsed_peers):
                recent_repliers = types.List(parsed_peers)

        return MessageReplies(
            client=client,

            comments=getattr(message_replies, 'comments', None),
            replies=getattr(message_replies, 'replies', None),
            replies_pts=getattr(message_replies, 'replies_pts', None),
            recent_repliers=recent_repliers,
            channel_id=utils.get_channel_id(message_replies.channel_id) if getattr(message_replies, 'channel_id',
                                                                                   None) else None,
            max_id=getattr(message_replies, 'max_id', None),
            read_max_id=getattr(message_replies, 'read_max_id', None),
        )
