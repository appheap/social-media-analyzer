import pyrogram
from pyrogram import raw
from pyrogram import types
from ..object import Object
from pyrogram import utils


class Dialog(Object):
    """A user's dialog.

    Parameters:
        chat (:obj:`~pyrogram.types.Chat`):
            Conversation the dialog belongs to.

        top_message (:obj:`~pyrogram.types.Message`):
            The last message sent in the dialog at this time.

        unread_messages_count (``int``):
            Amount of unread messages in this dialog.

        unread_mentions_count (``int``):
            Amount of unread messages containing a mention in this dialog.

        unread_mark (``bool``):
            True, if the dialog has the unread mark set.

        is_pinned (``bool``):
            True, if the dialog is pinned.
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            chat: "types.Chat",
            top_message: "types.Message",
            unread_messages_count: int,
            unread_mentions_count: int,
            unread_mark: bool,
            is_pinned: bool
    ):
        super().__init__(client)

        self.chat = chat
        self.top_message = top_message
        self.unread_messages_count = unread_messages_count
        self.unread_mentions_count = unread_mentions_count
        self.unread_mark = unread_mark
        self.is_pinned = is_pinned

    @staticmethod
    def _parse(client, dialog: "raw.types.Dialog", messages, users, chats) -> "Dialog":
        return Dialog(
            chat=types.Chat._parse_dialog(client, dialog.peer, users, chats),
            top_message=messages.get(utils.get_peer_id(dialog.peer)),
            unread_messages_count=dialog.unread_count,
            unread_mentions_count=dialog.unread_mentions_count,
            unread_mark=dialog.unread_mark,
            is_pinned=dialog.pinned,
            client=client
        )
