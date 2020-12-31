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


class RecentStickers(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.RecentStickers`.

    Details:
        - Layer: ``122``
        - ID: ``0x22f3afb3``

    Parameters:
        hash: ``int`` ``32-bit``
        packs: List of :obj:`StickerPack <pyrogram.raw.base.StickerPack>`
        stickers: List of :obj:`Document <pyrogram.raw.base.Document>`
        dates: List of ``int`` ``32-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetRecentStickers <pyrogram.raw.functions.messages.GetRecentStickers>`
    """

    __slots__: List[str] = ["hash", "packs", "stickers", "dates"]

    ID = 0x22f3afb3
    QUALNAME = "types.messages.RecentStickers"

    def __init__(self, *, hash: int, packs: List["raw.base.StickerPack"], stickers: List["raw.base.Document"],
                 dates: List[int]) -> None:
        self.hash = hash  # int
        self.packs = packs  # Vector<StickerPack>
        self.stickers = stickers  # Vector<Document>
        self.dates = dates  # Vector<int>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "RecentStickers":
        # No flags

        hash = Int.read(data)

        packs = TLObject.read(data)

        stickers = TLObject.read(data)

        dates = TLObject.read(data, Int)

        return RecentStickers(hash=hash, packs=packs, stickers=stickers, dates=dates)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.hash))

        data.write(Vector(self.packs))

        data.write(Vector(self.stickers))

        data.write(Vector(self.dates, Int))

        return data.getvalue()
