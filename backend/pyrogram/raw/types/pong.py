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


class Pong(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Pong`.

    Details:
        - Layer: ``122``
        - ID: ``0x347773c5``

    Parameters:
        msg_id: ``int`` ``64-bit``
        ping_id: ``int`` ``64-bit``

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`Ping <pyrogram.raw.functions.Ping>`
            - :obj:`PingDelayDisconnect <pyrogram.raw.functions.PingDelayDisconnect>`
    """

    __slots__: List[str] = ["msg_id", "ping_id"]

    ID = 0x347773c5
    QUALNAME = "types.Pong"

    def __init__(self, *, msg_id: int, ping_id: int) -> None:
        self.msg_id = msg_id  # long
        self.ping_id = ping_id  # long

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Pong":
        # No flags

        msg_id = Long.read(data)

        ping_id = Long.read(data)

        return Pong(msg_id=msg_id, ping_id=ping_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Long(self.msg_id))

        data.write(Long(self.ping_id))

        return data.getvalue()
