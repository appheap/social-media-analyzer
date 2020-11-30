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


class Stickers(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.Stickers`.

    Details:
        - Layer: ``117``
        - ID: ``0xe4599bbd``

    Parameters:
        hash: ``int`` ``32-bit``
        stickers: List of :obj:`Document <pyrogram.raw.base.Document>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetStickers <pyrogram.raw.functions.messages.GetStickers>`
    """

    __slots__: List[str] = ["hash", "stickers"]

    ID = 0xe4599bbd
    QUALNAME = "types.messages.Stickers"

    def __init__(self, *, hash: int, stickers: List["raw.base.Document"]) -> None:
        self.hash = hash  # int
        self.stickers = stickers  # Vector<Document>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Stickers":
        # No flags

        hash = Int.read(data)

        stickers = TLObject.read(data)

        return Stickers(hash=hash, stickers=stickers)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.hash))

        data.write(Vector(self.stickers))

        return data.getvalue()
