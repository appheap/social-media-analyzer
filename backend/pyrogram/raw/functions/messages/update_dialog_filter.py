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


class UpdateDialogFilter(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x1ad4a04a``

    Parameters:
        id: ``int`` ``32-bit``
        filter (optional): :obj:`DialogFilter <pyrogram.raw.base.DialogFilter>`

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "filter"]

    ID = 0x1ad4a04a
    QUALNAME = "functions.messages.UpdateDialogFilter"

    def __init__(self, *, id: int, filter: "raw.base.DialogFilter" = None) -> None:
        self.id = id  # int
        self.filter = filter  # flags.0?DialogFilter

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateDialogFilter":
        flags = Int.read(data)

        id = Int.read(data)

        filter = TLObject.read(data) if flags & (1 << 0) else None

        return UpdateDialogFilter(id=id, filter=filter)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.filter is not None else 0
        data.write(Int(flags))

        data.write(Int(self.id))

        if self.filter is not None:
            data.write(self.filter.write())

        return data.getvalue()
