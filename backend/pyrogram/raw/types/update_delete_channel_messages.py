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


class UpdateDeleteChannelMessages(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``123``
        - ID: ``0xc37521c9``

    Parameters:
        channel_id: ``int`` ``32-bit``
        messages: List of ``int`` ``32-bit``
        pts: ``int`` ``32-bit``
        pts_count: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["channel_id", "messages", "pts", "pts_count"]

    ID = 0xc37521c9
    QUALNAME = "types.UpdateDeleteChannelMessages"

    def __init__(self, *, channel_id: int, messages: List[int], pts: int, pts_count: int) -> None:
        self.channel_id = channel_id  # int
        self.messages = messages  # Vector<int>
        self.pts = pts  # int
        self.pts_count = pts_count  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateDeleteChannelMessages":
        # No flags

        channel_id = Int.read(data)

        messages = TLObject.read(data, Int)

        pts = Int.read(data)

        pts_count = Int.read(data)

        return UpdateDeleteChannelMessages(channel_id=channel_id, messages=messages, pts=pts, pts_count=pts_count)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.channel_id))

        data.write(Vector(self.messages, Int))

        data.write(Int(self.pts))

        data.write(Int(self.pts_count))

        return data.getvalue()
