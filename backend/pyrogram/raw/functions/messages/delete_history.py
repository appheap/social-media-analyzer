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


class DeleteHistory(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0x1c015b09``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        max_id: ``int`` ``32-bit``
        just_clear (optional): ``bool``
        revoke (optional): ``bool``

    Returns:
        :obj:`messages.AffectedHistory <pyrogram.raw.base.messages.AffectedHistory>`
    """

    __slots__: List[str] = ["peer", "max_id", "just_clear", "revoke"]

    ID = 0x1c015b09
    QUALNAME = "functions.messages.DeleteHistory"

    def __init__(self, *, peer: "raw.base.InputPeer", max_id: int, just_clear: Union[None, bool] = None,
                 revoke: Union[None, bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.max_id = max_id  # int
        self.just_clear = just_clear  # flags.0?true
        self.revoke = revoke  # flags.1?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "DeleteHistory":
        flags = Int.read(data)

        just_clear = True if flags & (1 << 0) else False
        revoke = True if flags & (1 << 1) else False
        peer = TLObject.read(data)

        max_id = Int.read(data)

        return DeleteHistory(peer=peer, max_id=max_id, just_clear=just_clear, revoke=revoke)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.just_clear is not None else 0
        flags |= (1 << 1) if self.revoke is not None else 0
        data.write(Int(flags))

        data.write(self.peer.write())

        data.write(Int(self.max_id))

        return data.getvalue()
