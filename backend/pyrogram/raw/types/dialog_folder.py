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


class DialogFolder(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Dialog`.

    Details:
        - Layer: ``122``
        - ID: ``0x71bd134c``

    Parameters:
        folder: :obj:`Folder <pyrogram.raw.base.Folder>`
        peer: :obj:`Peer <pyrogram.raw.base.Peer>`
        top_message: ``int`` ``32-bit``
        unread_muted_peers_count: ``int`` ``32-bit``
        unread_unmuted_peers_count: ``int`` ``32-bit``
        unread_muted_messages_count: ``int`` ``32-bit``
        unread_unmuted_messages_count: ``int`` ``32-bit``
        pinned (optional): ``bool``
    """

    __slots__: List[str] = ["folder", "peer", "top_message", "unread_muted_peers_count", "unread_unmuted_peers_count",
                            "unread_muted_messages_count", "unread_unmuted_messages_count", "pinned"]

    ID = 0x71bd134c
    QUALNAME = "types.DialogFolder"

    def __init__(self, *, folder: "raw.base.Folder", peer: "raw.base.Peer", top_message: int,
                 unread_muted_peers_count: int, unread_unmuted_peers_count: int, unread_muted_messages_count: int,
                 unread_unmuted_messages_count: int, pinned: Union[None, bool] = None) -> None:
        self.folder = folder  # Folder
        self.peer = peer  # Peer
        self.top_message = top_message  # int
        self.unread_muted_peers_count = unread_muted_peers_count  # int
        self.unread_unmuted_peers_count = unread_unmuted_peers_count  # int
        self.unread_muted_messages_count = unread_muted_messages_count  # int
        self.unread_unmuted_messages_count = unread_unmuted_messages_count  # int
        self.pinned = pinned  # flags.2?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "DialogFolder":
        flags = Int.read(data)

        pinned = True if flags & (1 << 2) else False
        folder = TLObject.read(data)

        peer = TLObject.read(data)

        top_message = Int.read(data)

        unread_muted_peers_count = Int.read(data)

        unread_unmuted_peers_count = Int.read(data)

        unread_muted_messages_count = Int.read(data)

        unread_unmuted_messages_count = Int.read(data)

        return DialogFolder(folder=folder, peer=peer, top_message=top_message,
                            unread_muted_peers_count=unread_muted_peers_count,
                            unread_unmuted_peers_count=unread_unmuted_peers_count,
                            unread_muted_messages_count=unread_muted_messages_count,
                            unread_unmuted_messages_count=unread_unmuted_messages_count, pinned=pinned)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.pinned else 0
        data.write(Int(flags))

        data.write(self.folder.write())

        data.write(self.peer.write())

        data.write(Int(self.top_message))

        data.write(Int(self.unread_muted_peers_count))

        data.write(Int(self.unread_unmuted_peers_count))

        data.write(Int(self.unread_muted_messages_count))

        data.write(Int(self.unread_unmuted_messages_count))

        return data.getvalue()
