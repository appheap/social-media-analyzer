import pyrogram
from pyrogram import types, raw
from ..object import Object


class PhotoStrippedSize(Object):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            type: str = None,
            bytes: bytes = None
    ):
        super().__init__(client=client)

        self.type = type
        self.bytes = bytes

    @staticmethod
    def _parse(client, photo_size: "raw.types.PhotoStrippedSize"):
        if photo_size is None:
            return None
        return PhotoStrippedSize(
            client=client,

            type=getattr(photo_size, 'type', None),
            bytes=getattr(photo_size, 'bytes', None),
        )
