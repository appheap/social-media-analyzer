from uuid import uuid4

from pyrogram import types
from ..object import Object

"""- :obj:`~pyrogram.types.InlineQueryResultCachedAudio`
    - :obj:`~pyrogram.types.InlineQueryResultCachedDocument`
    - :obj:`~pyrogram.types.InlineQueryResultCachedGif`
    - :obj:`~pyrogram.types.InlineQueryResultCachedMpeg4Gif`
    - :obj:`~pyrogram.types.InlineQueryResultCachedPhoto`
    - :obj:`~pyrogram.types.InlineQueryResultCachedSticker`
    - :obj:`~pyrogram.types.InlineQueryResultCachedVideo`
    - :obj:`~pyrogram.types.InlineQueryResultCachedVoice`
    - :obj:`~pyrogram.types.InlineQueryResultAudio`
    - :obj:`~pyrogram.types.InlineQueryResultContact`
    - :obj:`~pyrogram.types.InlineQueryResultGame`
    - :obj:`~pyrogram.types.InlineQueryResultDocument`
    - :obj:`~pyrogram.types.InlineQueryResultGif`
    - :obj:`~pyrogram.types.InlineQueryResultLocation`
    - :obj:`~pyrogram.types.InlineQueryResultMpeg4Gif`
    - :obj:`~pyrogram.types.InlineQueryResultPhoto`
    - :obj:`~pyrogram.types.InlineQueryResultVenue`
    - :obj:`~pyrogram.types.InlineQueryResultVideo`
    - :obj:`~pyrogram.types.InlineQueryResultVoice`"""


class InlineQueryResult(Object):
    """One result of an inline query.

    Pyrogram currently supports results of the following types:

    - :obj:`~pyrogram.types.InlineQueryResultArticle`
    - :obj:`~pyrogram.types.InlineQueryResultPhoto`
    - :obj:`~pyrogram.types.InlineQueryResultAnimation`
    """

    def __init__(
            self,
            type: str,
            id: str,
            input_message_content: "types.InputMessageContent",
            reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self):
        pass
