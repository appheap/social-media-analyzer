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


class SearchGlobal(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0xbf7225a4``

    Parameters:
        q: ``str``
        offset_rate: ``int`` ``32-bit``
        offset_peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        offset_id: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``
        folder_id (optional): ``int`` ``32-bit``

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["q", "offset_rate", "offset_peer", "offset_id", "limit", "folder_id"]

    ID = 0xbf7225a4
    QUALNAME = "functions.messages.SearchGlobal"

    def __init__(self, *, q: str, offset_rate: int, offset_peer: "raw.base.InputPeer", offset_id: int, limit: int,
                 folder_id: Union[None, int] = None) -> None:
        self.q = q  # string
        self.offset_rate = offset_rate  # int
        self.offset_peer = offset_peer  # InputPeer
        self.offset_id = offset_id  # int
        self.limit = limit  # int
        self.folder_id = folder_id  # flags.0?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SearchGlobal":
        flags = Int.read(data)

        folder_id = Int.read(data) if flags & (1 << 0) else None
        q = String.read(data)

        offset_rate = Int.read(data)

        offset_peer = TLObject.read(data)

        offset_id = Int.read(data)

        limit = Int.read(data)

        return SearchGlobal(q=q, offset_rate=offset_rate, offset_peer=offset_peer, offset_id=offset_id, limit=limit,
                            folder_id=folder_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.folder_id is not None else 0
        data.write(Int(flags))

        if self.folder_id is not None:
            data.write(Int(self.folder_id))

        data.write(String(self.q))

        data.write(Int(self.offset_rate))

        data.write(self.offset_peer.write())

        data.write(Int(self.offset_id))

        data.write(Int(self.limit))

        return data.getvalue()
