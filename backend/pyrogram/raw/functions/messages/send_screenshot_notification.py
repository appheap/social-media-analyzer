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


class SendScreenshotNotification(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0xc97df020``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        reply_to_msg_id: ``int`` ``32-bit``
        random_id: ``int`` ``64-bit``

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "reply_to_msg_id", "random_id"]

    ID = 0xc97df020
    QUALNAME = "functions.messages.SendScreenshotNotification"

    def __init__(self, *, peer: "raw.base.InputPeer", reply_to_msg_id: int, random_id: int) -> None:
        self.peer = peer  # InputPeer
        self.reply_to_msg_id = reply_to_msg_id  # int
        self.random_id = random_id  # long

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SendScreenshotNotification":
        # No flags

        peer = TLObject.read(data)

        reply_to_msg_id = Int.read(data)

        random_id = Long.read(data)

        return SendScreenshotNotification(peer=peer, reply_to_msg_id=reply_to_msg_id, random_id=random_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.peer.write())

        data.write(Int(self.reply_to_msg_id))

        data.write(Long(self.random_id))

        return data.getvalue()
