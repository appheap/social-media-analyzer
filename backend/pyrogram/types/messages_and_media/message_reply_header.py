import pyrogram
from pyrogram import types, raw
from ..object import Object


class MessageReplyHeader(Object):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            reply_to_message_id: int = None,
            reply_to_user: "types.User" = None,
            reply_to_chat: "types.Chat" = None,
            reply_to_top_id: int = None,
    ):
        super().__init__(client=client)

        self.reply_to_message_id = reply_to_message_id
        self.reply_to_user = reply_to_user
        self.reply_to_chat = reply_to_chat
        self.reply_to_top_id = reply_to_top_id

    @staticmethod
    def _parse(client, message_reply_header: raw.base.MessageReplyHeader, users: dict, chats: dict):
        if message_reply_header is None:
            return None

        reply_to_peer_id = getattr(message_reply_header, 'reply_to_peer_id', None)
        reply_to_user = None
        reply_to_chat = None
        if reply_to_peer_id:
            if isinstance(reply_to_peer_id, raw.types.PeerUser):
                reply_to_user = types.User._parse(client, users.get(reply_to_peer_id.user_id, None))
            else:
                if isinstance(reply_to_peer_id, raw.types.PeerChannel):
                    _peer_id = reply_to_peer_id.channel_id
                else:
                    _peer_id = reply_to_peer_id.chat_id

                reply_to_chat = types.Chat._parse_chat(client, chats.get(_peer_id, None))

        return MessageReplyHeader(
            client=client,
            reply_to_message_id=message_reply_header.reply_to_msg_id,
            reply_to_user=reply_to_user,
            reply_to_chat=reply_to_chat,
            reply_to_top_id=getattr(message_reply_header, 'reply_to_top_id', None),
        )
