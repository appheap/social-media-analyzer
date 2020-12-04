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


class GetHistory(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0xdcbb8260``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        offset_id: ``int`` ``32-bit``
        offset_date: ``int`` ``32-bit``
        add_offset: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``
        max_id: ``int`` ``32-bit``
        min_id: ``int`` ``32-bit``
        hash: ``int`` ``32-bit``

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["peer", "offset_id", "offset_date", "add_offset", "limit", "max_id", "min_id", "hash"]

    ID = 0xdcbb8260
    QUALNAME = "functions.messages.GetHistory"

    def __init__(self, *, peer: "raw.base.InputPeer", offset_id: int, offset_date: int, add_offset: int, limit: int,
                 max_id: int, min_id: int, hash: int) -> None:
        self.peer = peer  # InputPeer
        self.offset_id = offset_id  # int
        self.offset_date = offset_date  # int
        self.add_offset = add_offset  # int
        self.limit = limit  # int
        self.max_id = max_id  # int
        self.min_id = min_id  # int
        self.hash = hash  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetHistory":
        # No flags

        peer = TLObject.read(data)

        offset_id = Int.read(data)

        offset_date = Int.read(data)

        add_offset = Int.read(data)

        limit = Int.read(data)

        max_id = Int.read(data)

        min_id = Int.read(data)

        hash = Int.read(data)

        return GetHistory(peer=peer, offset_id=offset_id, offset_date=offset_date, add_offset=add_offset, limit=limit,
                          max_id=max_id, min_id=min_id, hash=hash)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.peer.write())

        data.write(Int(self.offset_id))

        data.write(Int(self.offset_date))

        data.write(Int(self.add_offset))

        data.write(Int(self.limit))

        data.write(Int(self.max_id))

        data.write(Int(self.min_id))

        data.write(Int(self.hash))

        return data.getvalue()
