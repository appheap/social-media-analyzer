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


class InputFolderPeer(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputFolderPeer`.

    Details:
        - Layer: ``120``
        - ID: ``0xfbd2c296``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        folder_id: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["peer", "folder_id"]

    ID = 0xfbd2c296
    QUALNAME = "types.InputFolderPeer"

    def __init__(self, *, peer: "raw.base.InputPeer", folder_id: int) -> None:
        self.peer = peer  # InputPeer
        self.folder_id = folder_id  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputFolderPeer":
        # No flags

        peer = TLObject.read(data)

        folder_id = Int.read(data)

        return InputFolderPeer(peer=peer, folder_id=folder_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.peer.write())

        data.write(Int(self.folder_id))

        return data.getvalue()
