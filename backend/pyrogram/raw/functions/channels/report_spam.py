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


class ReportSpam(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0xfe087810``

    Parameters:
        channel: :obj:`InputChannel <pyrogram.raw.base.InputChannel>`
        user_id: :obj:`InputUser <pyrogram.raw.base.InputUser>`
        id: List of ``int`` ``32-bit``

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "user_id", "id"]

    ID = 0xfe087810
    QUALNAME = "functions.channels.ReportSpam"

    def __init__(self, *, channel: "raw.base.InputChannel", user_id: "raw.base.InputUser", id: List[int]) -> None:
        self.channel = channel  # InputChannel
        self.user_id = user_id  # InputUser
        self.id = id  # Vector<int>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ReportSpam":
        # No flags

        channel = TLObject.read(data)

        user_id = TLObject.read(data)

        id = TLObject.read(data, Int)

        return ReportSpam(channel=channel, user_id=user_id, id=id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.channel.write())

        data.write(self.user_id.write())

        data.write(Vector(self.id, Int))

        return data.getvalue()
