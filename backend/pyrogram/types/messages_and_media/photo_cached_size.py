import pyrogram
from pyrogram import types, raw
from ..object import Object


class PhotoCachedSize(Object):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            type: str = None,
            location: "types.FileLocation" = None,
            w: int = None,
            h: int = None,
            size: int = None,
            bytes: bytes = None
    ):
        super().__init__(client=client)

        self.type = type
        self.location = location
        self.w = w
        self.h = h
        self.size = size
        self.bytes = bytes

    @staticmethod
    def _parse(client, photo_size: "raw.types.PhotoCachedSize"):
        if photo_size is None:
            return None
        return PhotoCachedSize(
            client=client,

            type=getattr(photo_size, 'type', None),
            location=types.FileLocation._parse(client, getattr(photo_size, 'location', None)),
            w=getattr(photo_size, 'w', None),
            h=getattr(photo_size, 'h', None),
            size=getattr(photo_size, 'size', None),
            bytes=getattr(photo_size, 'bytes', None),
        )
