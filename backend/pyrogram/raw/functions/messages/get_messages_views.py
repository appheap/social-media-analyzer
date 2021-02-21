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


class GetMessagesViews(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x5784d3e1``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        id: List of ``int`` ``32-bit``
        increment: ``bool``

    Returns:
        :obj:`messages.MessageViews <pyrogram.raw.base.messages.MessageViews>`
    """

    __slots__: List[str] = ["peer", "id", "increment"]

    ID = 0x5784d3e1
    QUALNAME = "functions.messages.GetMessagesViews"

    def __init__(self, *, peer: "raw.base.InputPeer", id: List[int], increment: bool) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # Vector<int>
        self.increment = increment  # Bool

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetMessagesViews":
        # No flags

        peer = TLObject.read(data)

        id = TLObject.read(data, Int)

        increment = Bool.read(data)

        return GetMessagesViews(peer=peer, id=id, increment=increment)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.peer.write())

        data.write(Vector(self.id, Int))

        data.write(Bool(self.increment))

        return data.getvalue()
