import pyrogram
from pyrogram import types, raw
from ..object import Object
from typing import List


class MessageService(Object):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            outgoing: bool = None,
            mentioned: bool = None,
            media_unread: bool = None,
            is_silent: bool = None,
            is_post: bool = None,
            is_legacy: bool = None,
            from_chat: "types.Chat" = None,
            from_user: "types.User" = None,
            reply_header: "types.MessageReplyHeader" = None,
            action: "types.MessageAction" = None,
    ):
        super().__init__(client=client)

        self.outgoing = outgoing
        self.mentioned = mentioned
        self.media_unread = media_unread
        self.is_silent = is_silent
        self.is_post = is_post
        self.is_legacy = is_legacy
        self.from_chat = from_chat
        self.from_user = from_user
        self.reply_header = reply_header
        self.action = action

    @staticmethod
    async def _parse(client, message: raw.types.MessageService, users: dict, chats: dict):
        if message is None:
            return None

        action = await types.MessageAction._parse_action(client, message, users, chats)
        return MessageService(
            client=client,

            outgoing=getattr(message, 'out', None),
            mentioned=getattr(message, 'mentioned', None),
            media_unread=getattr(message, 'media_unread', None),
            is_silent=getattr(message, 'silent', None),
            is_post=getattr(message, 'post', None),
            is_legacy=getattr(message, 'legacy', None),
            from_user=None,
            from_chat=None,
            reply_header=types.MessageReplyHeader._parse(client, getattr(message, 'reply_to', None), users, chats),
            action=action,
        )
