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


class PageTableRow(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PageTableRow`.

    Details:
        - Layer: ``123``
        - ID: ``0xe0c0c5e5``

    Parameters:
        cells: List of :obj:`PageTableCell <pyrogram.raw.base.PageTableCell>`
    """

    __slots__: List[str] = ["cells"]

    ID = 0xe0c0c5e5
    QUALNAME = "types.PageTableRow"

    def __init__(self, *, cells: List["raw.base.PageTableCell"]) -> None:
        self.cells = cells  # Vector<PageTableCell>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PageTableRow":
        # No flags

        cells = TLObject.read(data)

        return PageTableRow(cells=cells)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Vector(self.cells))

        return data.getvalue()
