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


class MarkDialogUnread(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0xc286d98f``

    Parameters:
        peer: :obj:`InputDialogPeer <pyrogram.raw.base.InputDialogPeer>`
        unread (optional): ``bool``

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "unread"]

    ID = 0xc286d98f
    QUALNAME = "functions.messages.MarkDialogUnread"

    def __init__(self, *, peer: "raw.base.InputDialogPeer", unread: Union[None, bool] = None) -> None:
        self.peer = peer  # InputDialogPeer
        self.unread = unread  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MarkDialogUnread":
        flags = Int.read(data)

        unread = True if flags & (1 << 0) else False
        peer = TLObject.read(data)

        return MarkDialogUnread(peer=peer, unread=unread)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.unread is not None else 0
        data.write(Int(flags))

        data.write(self.peer.write())

        return data.getvalue()
