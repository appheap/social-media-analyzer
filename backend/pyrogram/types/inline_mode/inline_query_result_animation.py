from typing import Union

from pyrogram import raw
from pyrogram import types
from pyrogram.parser import Parser
from .inline_query_result import InlineQueryResult


class InlineQueryResultAnimation(InlineQueryResult):
    """Link to an animated GIF file.

    By default, this animated GIF file will be sent by the user with optional caption.
    Alternatively, you can use *input_message_content* to send a message with the specified content instead of the
    animation.

    Parameters:
        animation_url (``str``):
            A valid URL for the animated GIF file.
            File size must not exceed 1 MB.

        thumb_url (``str``, *optional*):
            URL of the static thumbnail for the result (jpeg or gif)
            Defaults to the value passed in *animation_url*.

        id (``str``, *optional*):
            Unique identifier for this result, 1-64 bytes.
            Defaults to a randomly generated UUID4.

        title (``str``, *optional*):
            Title for the result.

        description (``str``, *optional*):
            Short description of the result.

        caption (``str``, *optional*):
            Caption of the photo to be sent, 0-1024 characters.

        parse_mode (``str``, *optional*):
            By default, texts are parsed using both Markdown and HTML styles.
            You can combine both syntaxes together.
            Pass "markdown" or "md" to enable Markdown-style parsing only.
            Pass "html" to enable HTML-style parsing only.
            Pass None to completely disable style parsing.

        reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
            An InlineKeyboardMarkup object.

        input_message_content (:obj:`~pyrogram.types.InputMessageContent`):
            Content of the message to be sent instead of the photo.
    """

    def __init__(
            self,
            animation_url: str,
            thumb_url: str = None,
            id: str = None,
            title: str = None,
            description: str = None,
            caption: str = "",
            parse_mode: Union[str, None] = object,
            reply_markup: "types.InlineKeyboardMarkup" = None,
            input_message_content: "types.InputMessageContent" = None
    ):
        super().__init__("gif", id, input_message_content, reply_markup)

        self.animation_url = animation_url
        self.thumb_url = thumb_url
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    async def write(self):
        animation = raw.types.InputWebDocument(
            url=self.animation_url,
            size=0,
            mime_type="image/gif",
            attributes=[]
        )

        if self.thumb_url is None:
            thumb = animation
        else:
            thumb = raw.types.InputWebDocument(
                url=self.thumb_url,
                size=0,
                mime_type="image/gif",
                attributes=[]
            )

        return raw.types.InputBotInlineResult(
            id=self.id,
            type=self.type,
            title=self.title,
            description=self.description,
            thumb=thumb,
            content=animation,
            send_message=(
                self.input_message_content.write(self.reply_markup)
                if self.input_message_content
                else raw.types.InputBotInlineMessageMediaAuto(
                    reply_markup=self.reply_markup.write() if self.reply_markup else None,
                    **await(Parser(None)).parse(self.caption, self.parse_mode)
                )
            )
        )
