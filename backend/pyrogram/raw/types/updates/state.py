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


class State(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.updates.State`.

    Details:
        - Layer: ``122``
        - ID: ``0xa56c2a3e``

    Parameters:
        pts: ``int`` ``32-bit``
        qts: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        seq: ``int`` ``32-bit``
        unread_count: ``int`` ``32-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`updates.GetState <pyrogram.raw.functions.updates.GetState>`
    """

    __slots__: List[str] = ["pts", "qts", "date", "seq", "unread_count"]

    ID = 0xa56c2a3e
    QUALNAME = "types.updates.State"

    def __init__(self, *, pts: int, qts: int, date: int, seq: int, unread_count: int) -> None:
        self.pts = pts  # int
        self.qts = qts  # int
        self.date = date  # int
        self.seq = seq  # int
        self.unread_count = unread_count  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "State":
        # No flags

        pts = Int.read(data)

        qts = Int.read(data)

        date = Int.read(data)

        seq = Int.read(data)

        unread_count = Int.read(data)

        return State(pts=pts, qts=qts, date=date, seq=seq, unread_count=unread_count)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.pts))

        data.write(Int(self.qts))

        data.write(Int(self.date))

        data.write(Int(self.seq))

        data.write(Int(self.unread_count))

        return data.getvalue()
