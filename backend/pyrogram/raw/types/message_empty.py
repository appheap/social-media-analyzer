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


class MessageEmpty(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Message`.

    Details:
        - Layer: ``123``
        - ID: ``0x90a6ca84``

    Parameters:
        id: ``int`` ``32-bit``
        peer_id (optional): :obj:`Peer <pyrogram.raw.base.Peer>`
    """

    __slots__: List[str] = ["id", "peer_id"]

    ID = 0x90a6ca84
    QUALNAME = "types.MessageEmpty"

    def __init__(self, *, id: int, peer_id: "raw.base.Peer" = None) -> None:
        self.id = id  # int
        self.peer_id = peer_id  # flags.0?Peer

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MessageEmpty":
        flags = Int.read(data)

        id = Int.read(data)

        peer_id = TLObject.read(data) if flags & (1 << 0) else None

        return MessageEmpty(id=id, peer_id=peer_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.peer_id is not None else 0
        data.write(Int(flags))

        data.write(Int(self.id))

        if self.peer_id is not None:
            data.write(self.peer_id.write())

        return data.getvalue()
