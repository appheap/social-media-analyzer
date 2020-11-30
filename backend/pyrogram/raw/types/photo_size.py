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


class PhotoSize(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PhotoSize`.

    Details:
        - Layer: ``117``
        - ID: ``0x77bfb61b``

    Parameters:
        type: ``str``
        location: :obj:`FileLocation <pyrogram.raw.base.FileLocation>`
        w: ``int`` ``32-bit``
        h: ``int`` ``32-bit``
        size: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["type", "location", "w", "h", "size"]

    ID = 0x77bfb61b
    QUALNAME = "types.PhotoSize"

    def __init__(self, *, type: str, location: "raw.base.FileLocation", w: int, h: int, size: int) -> None:
        self.type = type  # string
        self.location = location  # FileLocation
        self.w = w  # int
        self.h = h  # int
        self.size = size  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PhotoSize":
        # No flags

        type = String.read(data)

        location = TLObject.read(data)

        w = Int.read(data)

        h = Int.read(data)

        size = Int.read(data)

        return PhotoSize(type=type, location=location, w=w, h=h, size=size)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.type))

        data.write(self.location.write())

        data.write(Int(self.w))

        data.write(Int(self.h))

        data.write(Int(self.size))

        return data.getvalue()
