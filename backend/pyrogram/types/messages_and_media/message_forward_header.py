import pyrogram
from pyrogram import types, raw
from ..object import Object


class MessageForwardHeader(Object):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            date: int,
            forward_from_user: "types.User" = None,
            forward_from_chat: "types.Chat" = None,
            forward_sender_name: str = None,
            forward_from_message_id: int = None,
            forward_signature: str = None,
            saved_from_user: "types.User" = None,
            saved_from_chat: "types.Chat" = None,
            saved_from_message_id: int = None,
            psa_type: str = None,
    ):
        super().__init__(client=client)

        self.date = date
        self.forward_from_user = forward_from_user
        self.forward_from_chat = forward_from_chat
        self.forward_sender_name = forward_sender_name
        self.forward_from_message_id = forward_from_message_id
        self.forward_signature = forward_signature
        self.saved_from_user = saved_from_user
        self.saved_from_chat = saved_from_chat
        self.saved_from_message_id = saved_from_message_id
        self.psa_type = psa_type

    @staticmethod
    async def _parse(client, message_fwd_header: raw.base.MessageFwdHeader, users: dict, chats: dict):
        if message_fwd_header is None:
            return None

        saved_from_peer = getattr(message_fwd_header, 'saved_from_peer', None)
        saved_from_user = None
        saved_from_chat = None
        if saved_from_peer:
            if isinstance(saved_from_peer, raw.types.PeerUser):
                saved_from_user = types.User._parse(client, users.get(saved_from_peer.user_id, None))
            else:
                if isinstance(saved_from_peer, raw.types.PeerChannel):
                    _peer_id = saved_from_peer.channel_id
                else:
                    _peer_id = saved_from_peer.chat_id

                saved_from_chat = await types.Chat._parse_chat(client, chats.get(_peer_id, None))

        from_id = getattr(message_fwd_header, 'from_id', None)
        forward_from_user = None
        forward_from_chat = None
        if from_id:
            if isinstance(from_id, raw.types.PeerUser):
                forward_from_user = types.User._parse(client, users.get(from_id.user_id, None))
            else:
                if isinstance(from_id, raw.types.PeerChannel):
                    _peer_id = from_id.channel_id
                else:
                    _peer_id = from_id.chat_id

                forward_from_chat = await types.Chat._parse_chat(client, chats.get(_peer_id, None))

        return MessageForwardHeader(
            client=client,

            date=message_fwd_header.date,
            forward_from_user=forward_from_user,
            forward_from_chat=forward_from_chat,
            forward_sender_name=getattr(message_fwd_header, 'from_name', None),
            forward_from_message_id=getattr(message_fwd_header, 'channel_post', None),
            forward_signature=getattr(message_fwd_header, 'post_author', None),
            saved_from_user=saved_from_user,
            saved_from_chat=saved_from_chat,
            saved_from_message_id=getattr(message_fwd_header, 'saved_from_msg_id', None),
            psa_type=getattr(message_fwd_header, 'psa_type', None),
        )
