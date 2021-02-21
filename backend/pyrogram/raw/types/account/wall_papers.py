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


class WallPapers(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.account.WallPapers`.

    Details:
        - Layer: ``123``
        - ID: ``0x702b65a9``

    Parameters:
        hash: ``int`` ``32-bit``
        wallpapers: List of :obj:`WallPaper <pyrogram.raw.base.WallPaper>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`account.GetWallPapers <pyrogram.raw.functions.account.GetWallPapers>`
    """

    __slots__: List[str] = ["hash", "wallpapers"]

    ID = 0x702b65a9
    QUALNAME = "types.account.WallPapers"

    def __init__(self, *, hash: int, wallpapers: List["raw.base.WallPaper"]) -> None:
        self.hash = hash  # int
        self.wallpapers = wallpapers  # Vector<WallPaper>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "WallPapers":
        # No flags

        hash = Int.read(data)

        wallpapers = TLObject.read(data)

        return WallPapers(hash=hash, wallpapers=wallpapers)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.hash))

        data.write(Vector(self.wallpapers))

        return data.getvalue()
