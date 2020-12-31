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


class SearchStickerSets(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0xc2b7d08b``

    Parameters:
        q: ``str``
        hash: ``int`` ``32-bit``
        exclude_featured (optional): ``bool``

    Returns:
        :obj:`messages.FoundStickerSets <pyrogram.raw.base.messages.FoundStickerSets>`
    """

    __slots__: List[str] = ["q", "hash", "exclude_featured"]

    ID = 0xc2b7d08b
    QUALNAME = "functions.messages.SearchStickerSets"

    def __init__(self, *, q: str, hash: int, exclude_featured: Union[None, bool] = None) -> None:
        self.q = q  # string
        self.hash = hash  # int
        self.exclude_featured = exclude_featured  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SearchStickerSets":
        flags = Int.read(data)

        exclude_featured = True if flags & (1 << 0) else False
        q = String.read(data)

        hash = Int.read(data)

        return SearchStickerSets(q=q, hash=hash, exclude_featured=exclude_featured)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.exclude_featured else 0
        data.write(Int(flags))

        data.write(String(self.q))

        data.write(Int(self.hash))

        return data.getvalue()
