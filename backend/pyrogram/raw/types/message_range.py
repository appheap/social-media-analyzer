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


class MessageRange(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.MessageRange`.

    Details:
        - Layer: ``120``
        - ID: ``0xae30253``

    Parameters:
        min_id: ``int`` ``32-bit``
        max_id: ``int`` ``32-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetSplitRanges <pyrogram.raw.functions.messages.GetSplitRanges>`
    """

    __slots__: List[str] = ["min_id", "max_id"]

    ID = 0xae30253
    QUALNAME = "types.MessageRange"

    def __init__(self, *, min_id: int, max_id: int) -> None:
        self.min_id = min_id  # int
        self.max_id = max_id  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MessageRange":
        # No flags

        min_id = Int.read(data)

        max_id = Int.read(data)

        return MessageRange(min_id=min_id, max_id=max_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.min_id))

        data.write(Int(self.max_id))

        return data.getvalue()
