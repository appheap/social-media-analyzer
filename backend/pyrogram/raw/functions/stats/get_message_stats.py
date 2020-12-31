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


class GetMessageStats(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0xb6e0a3f5``

    Parameters:
        channel: :obj:`InputChannel <pyrogram.raw.base.InputChannel>`
        msg_id: ``int`` ``32-bit``
        dark (optional): ``bool``

    Returns:
        :obj:`stats.MessageStats <pyrogram.raw.base.stats.MessageStats>`
    """

    __slots__: List[str] = ["channel", "msg_id", "dark"]

    ID = 0xb6e0a3f5
    QUALNAME = "functions.stats.GetMessageStats"

    def __init__(self, *, channel: "raw.base.InputChannel", msg_id: int, dark: Union[None, bool] = None) -> None:
        self.channel = channel  # InputChannel
        self.msg_id = msg_id  # int
        self.dark = dark  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetMessageStats":
        flags = Int.read(data)

        dark = True if flags & (1 << 0) else False
        channel = TLObject.read(data)

        msg_id = Int.read(data)

        return GetMessageStats(channel=channel, msg_id=msg_id, dark=dark)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark else 0
        data.write(Int(flags))

        data.write(self.channel.write())

        data.write(Int(self.msg_id))

        return data.getvalue()
