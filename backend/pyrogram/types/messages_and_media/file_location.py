import pyrogram
from pyrogram import types, raw
from ..object import Object


class FileLocation(Object):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            volume_id: int = None,
            local_id: int = None,
    ):
        super().__init__(client=client)

        self.volume_id = volume_id
        self.local_id = local_id

    @staticmethod
    def _parse(client, file_location):
        if file_location is None:
            return None

        return FileLocation(
            client=client,

            volume_id=getattr(file_location, 'volume_id', None),
            local_id=getattr(file_location, 'local_id', None),
        )
