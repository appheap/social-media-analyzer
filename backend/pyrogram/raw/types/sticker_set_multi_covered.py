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


class StickerSetMultiCovered(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.StickerSetCovered`.

    Details:
        - Layer: ``123``
        - ID: ``0x3407e51b``

    Parameters:
        set: :obj:`StickerSet <pyrogram.raw.base.StickerSet>`
        covers: List of :obj:`Document <pyrogram.raw.base.Document>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetAttachedStickers <pyrogram.raw.functions.messages.GetAttachedStickers>`
    """

    __slots__: List[str] = ["set", "covers"]

    ID = 0x3407e51b
    QUALNAME = "types.StickerSetMultiCovered"

    def __init__(self, *, set: "raw.base.StickerSet", covers: List["raw.base.Document"]) -> None:
        self.set = set  # StickerSet
        self.covers = covers  # Vector<Document>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StickerSetMultiCovered":
        # No flags

        set = TLObject.read(data)

        covers = TLObject.read(data)

        return StickerSetMultiCovered(set=set, covers=covers)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.set.write())

        data.write(Vector(self.covers))

        return data.getvalue()
