from typing import Union

from pyrogram import raw
from pyrogram.parser import Parser
from .input_message_content import InputMessageContent


class InputTextMessageContent(InputMessageContent):
    """Content of a text message to be sent as the result of an inline query.

    Parameters:
        message_text (``str``):
            Text of the message to be sent, 1-4096 characters.

        parse_mode (``str``, *optional*):
            By default, texts are parsed using both Markdown and HTML styles.
            You can combine both syntaxes together.
            Pass "markdown" or "md" to enable Markdown-style parsing only.
            Pass "html" to enable HTML-style parsing only.
            Pass None to completely disable style parsing.

        disable_web_page_preview (``bool``, *optional*):
            Disables link previews for links in this message.
    """

    def __init__(self, message_text: str, parse_mode: Union[str, None] = object, disable_web_page_preview: bool = None):
        super().__init__()

        self.message_text = message_text
        self.parse_mode = parse_mode
        self.disable_web_page_preview = disable_web_page_preview

    async def write(self, reply_markup):
        return raw.types.InputBotInlineMessageText(
            no_webpage=self.disable_web_page_preview or None,
            reply_markup=reply_markup.write() if reply_markup else None,
            **await(Parser(None)).parse(self.message_text, self.parse_mode)
        )
