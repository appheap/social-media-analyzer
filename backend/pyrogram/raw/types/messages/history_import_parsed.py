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


class HistoryImportParsed(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.HistoryImportParsed`.

    Details:
        - Layer: ``123``
        - ID: ``0x5e0fb7b9``

    Parameters:
        pm (optional): ``bool``
        group (optional): ``bool``
        title (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.CheckHistoryImport <pyrogram.raw.functions.messages.CheckHistoryImport>`
    """

    __slots__: List[str] = ["pm", "group", "title"]

    ID = 0x5e0fb7b9
    QUALNAME = "types.messages.HistoryImportParsed"

    def __init__(self, *, pm: Union[None, bool] = None, group: Union[None, bool] = None,
                 title: Union[None, str] = None) -> None:
        self.pm = pm  # flags.0?true
        self.group = group  # flags.1?true
        self.title = title  # flags.2?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "HistoryImportParsed":
        flags = Int.read(data)

        pm = True if flags & (1 << 0) else False
        group = True if flags & (1 << 1) else False
        title = String.read(data) if flags & (1 << 2) else None
        return HistoryImportParsed(pm=pm, group=group, title=title)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pm else 0
        flags |= (1 << 1) if self.group else 0
        flags |= (1 << 2) if self.title is not None else 0
        data.write(Int(flags))

        if self.title is not None:
            data.write(String(self.title))

        return data.getvalue()
