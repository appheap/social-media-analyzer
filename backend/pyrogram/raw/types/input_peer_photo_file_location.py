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


class InputPeerPhotoFileLocation(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``123``
        - ID: ``0x27d69997``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        volume_id: ``int`` ``64-bit``
        local_id: ``int`` ``32-bit``
        big (optional): ``bool``
    """

    __slots__: List[str] = ["peer", "volume_id", "local_id", "big"]

    ID = 0x27d69997
    QUALNAME = "types.InputPeerPhotoFileLocation"

    def __init__(self, *, peer: "raw.base.InputPeer", volume_id: int, local_id: int,
                 big: Union[None, bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.volume_id = volume_id  # long
        self.local_id = local_id  # int
        self.big = big  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputPeerPhotoFileLocation":
        flags = Int.read(data)

        big = True if flags & (1 << 0) else False
        peer = TLObject.read(data)

        volume_id = Long.read(data)

        local_id = Int.read(data)

        return InputPeerPhotoFileLocation(peer=peer, volume_id=volume_id, local_id=local_id, big=big)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.big else 0
        data.write(Int(flags))

        data.write(self.peer.write())

        data.write(Long(self.volume_id))

        data.write(Int(self.local_id))

        return data.getvalue()
