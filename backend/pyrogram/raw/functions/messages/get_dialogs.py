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


class GetDialogs(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0xa0ee3b73``

    Parameters:
        offset_date: ``int`` ``32-bit``
        offset_id: ``int`` ``32-bit``
        offset_peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        limit: ``int`` ``32-bit``
        hash: ``int`` ``32-bit``
        exclude_pinned (optional): ``bool``
        folder_id (optional): ``int`` ``32-bit``

    Returns:
        :obj:`messages.Dialogs <pyrogram.raw.base.messages.Dialogs>`
    """

    __slots__: List[str] = ["offset_date", "offset_id", "offset_peer", "limit", "hash", "exclude_pinned", "folder_id"]

    ID = 0xa0ee3b73
    QUALNAME = "functions.messages.GetDialogs"

    def __init__(self, *, offset_date: int, offset_id: int, offset_peer: "raw.base.InputPeer", limit: int, hash: int,
                 exclude_pinned: Union[None, bool] = None, folder_id: Union[None, int] = None) -> None:
        self.offset_date = offset_date  # int
        self.offset_id = offset_id  # int
        self.offset_peer = offset_peer  # InputPeer
        self.limit = limit  # int
        self.hash = hash  # int
        self.exclude_pinned = exclude_pinned  # flags.0?true
        self.folder_id = folder_id  # flags.1?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetDialogs":
        flags = Int.read(data)

        exclude_pinned = True if flags & (1 << 0) else False
        folder_id = Int.read(data) if flags & (1 << 1) else None
        offset_date = Int.read(data)

        offset_id = Int.read(data)

        offset_peer = TLObject.read(data)

        limit = Int.read(data)

        hash = Int.read(data)

        return GetDialogs(offset_date=offset_date, offset_id=offset_id, offset_peer=offset_peer, limit=limit, hash=hash,
                          exclude_pinned=exclude_pinned, folder_id=folder_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.exclude_pinned is not None else 0
        flags |= (1 << 1) if self.folder_id is not None else 0
        data.write(Int(flags))

        if self.folder_id is not None:
            data.write(Int(self.folder_id))

        data.write(Int(self.offset_date))

        data.write(Int(self.offset_id))

        data.write(self.offset_peer.write())

        data.write(Int(self.limit))

        data.write(Int(self.hash))

        return data.getvalue()
