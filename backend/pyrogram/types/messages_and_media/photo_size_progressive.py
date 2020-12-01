import pyrogram
from pyrogram import types, raw
from typing import List
from ..object import Object


class PhotoSizeProgressive(Object):
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
            sizes: List["int"] = None,
    ):
        super().__init__(client=client)

        self.type = type
        self.location = location
        self.w = w
        self.h = h
        self.sizes = sizes

    @staticmethod
    def _parse(client, photo_size: "raw.types.PhotoSizeProgressive"):
        if photo_size is None:
            return None
        return PhotoSizeProgressive(
            client=client,

            type=getattr(photo_size, 'type', None),
            location=types.FileLocation._parse(client, getattr(photo_size, 'location', None)),
            w=getattr(photo_size, 'w', None),
            h=getattr(photo_size, 'h', None),
            sizes=types.List([size for size in getattr(photo_size, 'sizes', [])]) or None,
        )
