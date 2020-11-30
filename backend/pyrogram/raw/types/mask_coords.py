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


class MaskCoords(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.MaskCoords`.

    Details:
        - Layer: ``117``
        - ID: ``0xaed6dbb2``

    Parameters:
        n: ``int`` ``32-bit``
        x: ``float`` ``64-bit``
        y: ``float`` ``64-bit``
        zoom: ``float`` ``64-bit``
    """

    __slots__: List[str] = ["n", "x", "y", "zoom"]

    ID = 0xaed6dbb2
    QUALNAME = "types.MaskCoords"

    def __init__(self, *, n: int, x: float, y: float, zoom: float) -> None:
        self.n = n  # int
        self.x = x  # double
        self.y = y  # double
        self.zoom = zoom  # double

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MaskCoords":
        # No flags

        n = Int.read(data)

        x = Double.read(data)

        y = Double.read(data)

        zoom = Double.read(data)

        return MaskCoords(n=n, x=x, y=y, zoom=zoom)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.n))

        data.write(Double(self.x))

        data.write(Double(self.y))

        data.write(Double(self.zoom))

        return data.getvalue()
