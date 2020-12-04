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


class SetTyping(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0x58943ee2``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        action: :obj:`SendMessageAction <pyrogram.raw.base.SendMessageAction>`
        top_msg_id (optional): ``int`` ``32-bit``

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "action", "top_msg_id"]

    ID = 0x58943ee2
    QUALNAME = "functions.messages.SetTyping"

    def __init__(self, *, peer: "raw.base.InputPeer", action: "raw.base.SendMessageAction",
                 top_msg_id: Union[None, int] = None) -> None:
        self.peer = peer  # InputPeer
        self.action = action  # SendMessageAction
        self.top_msg_id = top_msg_id  # flags.0?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SetTyping":
        flags = Int.read(data)

        peer = TLObject.read(data)

        top_msg_id = Int.read(data) if flags & (1 << 0) else None
        action = TLObject.read(data)

        return SetTyping(peer=peer, action=action, top_msg_id=top_msg_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        data.write(Int(flags))

        data.write(self.peer.write())

        if self.top_msg_id is not None:
            data.write(Int(self.top_msg_id))

        data.write(self.action.write())

        return data.getvalue()
