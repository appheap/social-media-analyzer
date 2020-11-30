from typing import List

import pyrogram
from pyrogram import raw, types as tg_types
from pyrogram import types
from ..object import Object


class ChatPreview(Object):
    """A chat preview.

    Parameters:
        title (``str``):
            Title of the chat.

        type (``str``):
            Type of chat, can be either, "group", "supergroup" or "channel".

        members_count (``int``):
            Chat members count.

        photo (:obj:`~pyrogram.types.Photo`, *optional*):
            Chat photo.

        members (List of :obj:`~pyrogram.types.User`, *optional*):
            Preview of some of the chat members.
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            title: str,
            type: str,
            members_count: int,
            photo: "types.Photo" = None,
            members: List["tg_types.User"] = None
    ):
        super().__init__(client)

        self.title = title
        self.type = type
        self.members_count = members_count
        self.photo = photo
        self.members = members

    @staticmethod
    def _parse(client, chat_invite: "raw.types.ChatInvite") -> "ChatPreview":
        return ChatPreview(
            title=chat_invite.title,
            type=("group" if not chat_invite.channel else
                  "channel" if chat_invite.broadcast else
                  "supergroup"),
            members_count=chat_invite.participants_count,
            photo=types.Photo._parse(client, chat_invite.photo),
            members=[tg_types.User._parse(client, user) for user in chat_invite.participants] or None,
            client=client
        )

    # TODO: Maybe just merge this object into Chat itself by adding the "members" field.
    #  get_chat can be used as well instead of get_chat_preview
