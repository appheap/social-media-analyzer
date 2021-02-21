#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
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


class TextImage(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.RichText`.

    Details:
        - Layer: ``123``
        - ID: ``0x81ccf4f``

    Parameters:
        document_id: ``int`` ``64-bit``
        w: ``int`` ``32-bit``
        h: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["document_id", "w", "h"]

    ID = 0x81ccf4f
    QUALNAME = "types.TextImage"

    def __init__(self, *, document_id: int, w: int, h: int) -> None:
        self.document_id = document_id  # long
        self.w = w  # int
        self.h = h  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "TextImage":
        # No flags

        document_id = Long.read(data)

        w = Int.read(data)

        h = Int.read(data)

        return TextImage(document_id=document_id, w=w, h=h)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Long(self.document_id))

        data.write(Int(self.w))

        data.write(Int(self.h))

        return data.getvalue()
