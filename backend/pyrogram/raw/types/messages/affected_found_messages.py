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


class AffectedFoundMessages(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.AffectedFoundMessages`.

    Details:
        - Layer: ``123``
        - ID: ``0xef8d3e6c``

    Parameters:
        pts: ``int`` ``32-bit``
        pts_count: ``int`` ``32-bit``
        offset: ``int`` ``32-bit``
        messages: List of ``int`` ``32-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.DeletePhoneCallHistory <pyrogram.raw.functions.messages.DeletePhoneCallHistory>`
    """

    __slots__: List[str] = ["pts", "pts_count", "offset", "messages"]

    ID = 0xef8d3e6c
    QUALNAME = "types.messages.AffectedFoundMessages"

    def __init__(self, *, pts: int, pts_count: int, offset: int, messages: List[int]) -> None:
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.offset = offset  # int
        self.messages = messages  # Vector<int>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "AffectedFoundMessages":
        # No flags

        pts = Int.read(data)

        pts_count = Int.read(data)

        offset = Int.read(data)

        messages = TLObject.read(data, Int)

        return AffectedFoundMessages(pts=pts, pts_count=pts_count, offset=offset, messages=messages)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.pts))

        data.write(Int(self.pts_count))

        data.write(Int(self.offset))

        data.write(Vector(self.messages, Int))

        return data.getvalue()
