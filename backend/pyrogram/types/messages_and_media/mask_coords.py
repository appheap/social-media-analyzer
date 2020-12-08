import pyrogram
from pyrogram import types, raw
from ..object import Object


class MaskCoords(Object):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            n: int,
            x: float,
            y: float,
            zoom: float,

    ):
        super().__init__(client=client)

        self.n = n
        self.x = x
        self.y = y
        self.zoom = zoom

    @staticmethod
    def _parse(client, mask_coords: raw.base.MaskCoords):
        if mask_coords is None:
            return None

        if isinstance(mask_coords, raw.types.MaskCoords):
            return MaskCoords(
                client=client,

                n=mask_coords.n,
                x=mask_coords.x,
                y=mask_coords.y,
                zoom=mask_coords.zoom,
            )
