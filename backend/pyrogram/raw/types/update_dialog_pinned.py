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


class UpdateDialogPinned(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``120``
        - ID: ``0x6e6fe51c``

    Parameters:
        peer: :obj:`DialogPeer <pyrogram.raw.base.DialogPeer>`
        pinned (optional): ``bool``
        folder_id (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["peer", "pinned", "folder_id"]

    ID = 0x6e6fe51c
    QUALNAME = "types.UpdateDialogPinned"

    def __init__(self, *, peer: "raw.base.DialogPeer", pinned: Union[None, bool] = None,
                 folder_id: Union[None, int] = None) -> None:
        self.peer = peer  # DialogPeer
        self.pinned = pinned  # flags.0?true
        self.folder_id = folder_id  # flags.1?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateDialogPinned":
        flags = Int.read(data)

        pinned = True if flags & (1 << 0) else False
        folder_id = Int.read(data) if flags & (1 << 1) else None
        peer = TLObject.read(data)

        return UpdateDialogPinned(peer=peer, pinned=pinned, folder_id=folder_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pinned is not None else 0
        flags |= (1 << 1) if self.folder_id is not None else 0
        data.write(Int(flags))

        if self.folder_id is not None:
            data.write(Int(self.folder_id))

        data.write(self.peer.write())

        return data.getvalue()
