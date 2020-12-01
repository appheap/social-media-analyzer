import pyrogram
from pyrogram import types, raw
from ..object import Object


class PhotoSizeBase(Object):
    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

    ):
        super().__init__(client)

    @staticmethod
    def _parse(client, photo_size: "raw.base.PhotoSize"):
        if photo_size is None:
            return None

        if isinstance(photo_size, raw.types.PhotoSizeEmpty):
            return types.PhotoSizeEmpty._parse(client, photo_size)

        elif isinstance(photo_size, raw.types.PhotoSize):
            return types.PhotoSize._parse(client, photo_size)

        elif isinstance(photo_size, raw.types.PhotoCachedSize):
            return types.PhotoCachedSize._parse(client, photo_size)

        elif isinstance(photo_size, raw.types.PhotoStrippedSize):
            return types.PhotoStrippedSize._parse(client, photo_size)

        elif isinstance(photo_size, raw.types.PhotoSizeProgressive):
            return types.PhotoSizeProgressive._parse(client, photo_size)

        elif isinstance(photo_size, raw.types.PhotoPathSize):
            return types.PhotoPathSize._parse(client, photo_size)

        else:
            return None
