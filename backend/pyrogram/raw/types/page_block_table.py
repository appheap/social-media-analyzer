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


class PageBlockTable(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``123``
        - ID: ``0xbf4dea82``

    Parameters:
        title: :obj:`RichText <pyrogram.raw.base.RichText>`
        rows: List of :obj:`PageTableRow <pyrogram.raw.base.PageTableRow>`
        bordered (optional): ``bool``
        striped (optional): ``bool``
    """

    __slots__: List[str] = ["title", "rows", "bordered", "striped"]

    ID = 0xbf4dea82
    QUALNAME = "types.PageBlockTable"

    def __init__(self, *, title: "raw.base.RichText", rows: List["raw.base.PageTableRow"],
                 bordered: Union[None, bool] = None, striped: Union[None, bool] = None) -> None:
        self.title = title  # RichText
        self.rows = rows  # Vector<PageTableRow>
        self.bordered = bordered  # flags.0?true
        self.striped = striped  # flags.1?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PageBlockTable":
        flags = Int.read(data)

        bordered = True if flags & (1 << 0) else False
        striped = True if flags & (1 << 1) else False
        title = TLObject.read(data)

        rows = TLObject.read(data)

        return PageBlockTable(title=title, rows=rows, bordered=bordered, striped=striped)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.bordered else 0
        flags |= (1 << 1) if self.striped else 0
        data.write(Int(flags))

        data.write(self.title.write())

        data.write(Vector(self.rows))

        return data.getvalue()
