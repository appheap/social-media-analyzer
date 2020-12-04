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


class AcceptUrlAuth(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0xf729ea98``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        msg_id: ``int`` ``32-bit``
        button_id: ``int`` ``32-bit``
        write_allowed (optional): ``bool``

    Returns:
        :obj:`UrlAuthResult <pyrogram.raw.base.UrlAuthResult>`
    """

    __slots__: List[str] = ["peer", "msg_id", "button_id", "write_allowed"]

    ID = 0xf729ea98
    QUALNAME = "functions.messages.AcceptUrlAuth"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, button_id: int,
                 write_allowed: Union[None, bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.button_id = button_id  # int
        self.write_allowed = write_allowed  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "AcceptUrlAuth":
        flags = Int.read(data)

        write_allowed = True if flags & (1 << 0) else False
        peer = TLObject.read(data)

        msg_id = Int.read(data)

        button_id = Int.read(data)

        return AcceptUrlAuth(peer=peer, msg_id=msg_id, button_id=button_id, write_allowed=write_allowed)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.write_allowed is not None else 0
        data.write(Int(flags))

        data.write(self.peer.write())

        data.write(Int(self.msg_id))

        data.write(Int(self.button_id))

        return data.getvalue()
