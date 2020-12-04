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


class UpdateReadHistoryInbox(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``120``
        - ID: ``0x9c974fdf``

    Parameters:
        peer: :obj:`Peer <pyrogram.raw.base.Peer>`
        max_id: ``int`` ``32-bit``
        still_unread_count: ``int`` ``32-bit``
        pts: ``int`` ``32-bit``
        pts_count: ``int`` ``32-bit``
        folder_id (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["peer", "max_id", "still_unread_count", "pts", "pts_count", "folder_id"]

    ID = 0x9c974fdf
    QUALNAME = "types.UpdateReadHistoryInbox"

    def __init__(self, *, peer: "raw.base.Peer", max_id: int, still_unread_count: int, pts: int, pts_count: int,
                 folder_id: Union[None, int] = None) -> None:
        self.peer = peer  # Peer
        self.max_id = max_id  # int
        self.still_unread_count = still_unread_count  # int
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.folder_id = folder_id  # flags.0?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateReadHistoryInbox":
        flags = Int.read(data)

        folder_id = Int.read(data) if flags & (1 << 0) else None
        peer = TLObject.read(data)

        max_id = Int.read(data)

        still_unread_count = Int.read(data)

        pts = Int.read(data)

        pts_count = Int.read(data)

        return UpdateReadHistoryInbox(peer=peer, max_id=max_id, still_unread_count=still_unread_count, pts=pts,
                                      pts_count=pts_count, folder_id=folder_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.folder_id is not None else 0
        data.write(Int(flags))

        if self.folder_id is not None:
            data.write(Int(self.folder_id))

        data.write(self.peer.write())

        data.write(Int(self.max_id))

        data.write(Int(self.still_unread_count))

        data.write(Int(self.pts))

        data.write(Int(self.pts_count))

        return data.getvalue()
