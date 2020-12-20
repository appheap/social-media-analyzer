from typing import Union

from .input_media import InputMedia


class InputMediaAnimation(InputMedia):
    """An animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent inside an album.

    Parameters:
        media (``str``):
            Animation to send.
            Pass a file_id as string to send a file that exists on the Telegram servers or
            pass a file path as string to upload a new file that exists on your local machine.

        file_ref (``str``, *optional*):
            A valid file reference obtained by a recently fetched media message.
            To be used in combination with a file id in case a file reference is needed.

        thumb (``str``, *optional*):
            Thumbnail of the animation file sent.
            The thumbnail should be in JPEG format and less than 200 KB in size.
            A thumbnail's width and height should not exceed 320 pixels.
            Thumbnails can't be reused and can be only uploaded as a new file.

        caption (``str``, *optional*):
            Caption of the animation to be sent, 0-1024 characters

        parse_mode (``str``, *optional*):
            By default, texts are parsed using both Markdown and HTML styles.
            You can combine both syntaxes together.
            Pass "markdown" or "md" to enable Markdown-style parsing only.
            Pass "html" to enable HTML-style parsing only.
            Pass None to completely disable style parsing.

        width (``int``, *optional*):
            Animation width.

        height (``int``, *optional*):
            Animation height.

        duration (``int``, *optional*):
            Animation duration.
    """

    def __init__(
            self,
            media: str,
            file_ref: str = None,
            thumb: str = None,
            caption: str = "",
            parse_mode: Union[str, None] = object,
            width: int = 0,
            height: int = 0,
            duration: int = 0
    ):
        super().__init__(media, file_ref, caption, parse_mode)

        self.thumb = thumb
        self.width = width
        self.height = height
        self.duration = duration
