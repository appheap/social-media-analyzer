import pyrogram
from pyrogram import types, raw
from ..object import Object


class PhotoSizeEmpty(Object):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            type: str = None,
    ):
        super().__init__(client=client)

        self.type = type

    @staticmethod
    def _parse(client, photo_size: "raw.types.PhotoSizeEmpty"):
        if photo_size is None:
            return None

        return PhotoSizeEmpty(
            client=client,

            type=getattr(photo_size, 'type', None),
        )
