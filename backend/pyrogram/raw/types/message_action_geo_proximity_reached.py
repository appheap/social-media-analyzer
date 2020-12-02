from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Union, Any


# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class MessageActionGeoProximityReached(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``121``
        - ID: ``0x98e0d697``

    Parameters:
        from_id: :obj: `Peer <pyrogram.raw.base.Peer>`
        to_id: :obj: `Peer <pyrogram.raw.base.Peer>`
        distance: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["from_id", "to_id", "distance", ]

    ID = 0x98e0d697
    QUALNAME = "types.MessageActionGeoProximityReached"

    def __init__(self, *, from_id: "raw.base.Peer", to_id: "raw.base.Peer", distance: int) -> None:
        self.from_id = from_id  # Peer
        self.to_id = to_id  # Peer
        self.distance = distance  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MessageActionGeoProximityReached":
        # No flags

        from_id = TLObject.read(data)

        to_id = TLObject.read(data)

        distance = Int.read(data)

        return MessageActionGeoProximityReached(from_id=from_id, to_id=to_id, distance=distance)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.from_id.write())

        data.write(self.to_id.write())

        data.write(Int(self.distance))

        return data.getvalue()
