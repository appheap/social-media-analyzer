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


class GetDifference(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0x25939651``

    Parameters:
        pts: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        qts: ``int`` ``32-bit``
        pts_total_limit (optional): ``int`` ``32-bit``

    Returns:
        :obj:`updates.Difference <pyrogram.raw.base.updates.Difference>`
    """

    __slots__: List[str] = ["pts", "date", "qts", "pts_total_limit"]

    ID = 0x25939651
    QUALNAME = "functions.updates.GetDifference"

    def __init__(self, *, pts: int, date: int, qts: int, pts_total_limit: Union[None, int] = None) -> None:
        self.pts = pts  # int
        self.date = date  # int
        self.qts = qts  # int
        self.pts_total_limit = pts_total_limit  # flags.0?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetDifference":
        flags = Int.read(data)

        pts = Int.read(data)

        pts_total_limit = Int.read(data) if flags & (1 << 0) else None
        date = Int.read(data)

        qts = Int.read(data)

        return GetDifference(pts=pts, date=date, qts=qts, pts_total_limit=pts_total_limit)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pts_total_limit is not None else 0
        data.write(Int(flags))

        data.write(Int(self.pts))

        if self.pts_total_limit is not None:
            data.write(Int(self.pts_total_limit))

        data.write(Int(self.date))

        data.write(Int(self.qts))

        return data.getvalue()
