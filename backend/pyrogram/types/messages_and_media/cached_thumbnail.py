import pyrogram
from ..object import Object


class CachedThumbnail(Object):
    """One size of a photo or a file/sticker thumbnail.

    Parameters:
        file_id (``str``):
            Identifier for this file, which can be used to download or reuse the file.

        file_unique_id (``str``):
            Unique identifier for this file, which is supposed to be the same over time and for different accounts.
            Can't be used to download or reuse the file.

        width (``int``):
            Photo width.

        height (``int``):
            Photo height.

        data (``bytes``):
            Sizes of progressive JPEG file prefixes, which can be used to preliminarily show the image..

        type (``str``):
            Thumbnail type.
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            file_id: str,
            file_unique_id: str,
            width: int,
            height: int,
            data: bytes,
            type: str
    ):
        super().__init__(client)

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.data = data
        self.type = type
