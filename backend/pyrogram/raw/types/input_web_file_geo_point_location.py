#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

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


class InputWebFileGeoPointLocation(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputWebFileLocation`.

    Details:
        - Layer: ``117``
        - ID: ``0x9f2221c9``

    Parameters:
        geo_point: :obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`
        access_hash: ``int`` ``64-bit``
        w: ``int`` ``32-bit``
        h: ``int`` ``32-bit``
        zoom: ``int`` ``32-bit``
        scale: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["geo_point", "access_hash", "w", "h", "zoom", "scale"]

    ID = 0x9f2221c9
    QUALNAME = "types.InputWebFileGeoPointLocation"

    def __init__(self, *, geo_point: "raw.base.InputGeoPoint", access_hash: int, w: int, h: int, zoom: int,
                 scale: int) -> None:
        self.geo_point = geo_point  # InputGeoPoint
        self.access_hash = access_hash  # long
        self.w = w  # int
        self.h = h  # int
        self.zoom = zoom  # int
        self.scale = scale  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputWebFileGeoPointLocation":
        # No flags

        geo_point = TLObject.read(data)

        access_hash = Long.read(data)

        w = Int.read(data)

        h = Int.read(data)

        zoom = Int.read(data)

        scale = Int.read(data)

        return InputWebFileGeoPointLocation(geo_point=geo_point, access_hash=access_hash, w=w, h=h, zoom=zoom,
                                            scale=scale)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.geo_point.write())

        data.write(Long(self.access_hash))

        data.write(Int(self.w))

        data.write(Int(self.h))

        data.write(Int(self.zoom))

        data.write(Int(self.scale))

        return data.getvalue()
