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


class SetEncryptedTyping(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0x791451ed``

    Parameters:
        peer: :obj:`InputEncryptedChat <pyrogram.raw.base.InputEncryptedChat>`
        typing: ``bool``

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "typing"]

    ID = 0x791451ed
    QUALNAME = "functions.messages.SetEncryptedTyping"

    def __init__(self, *, peer: "raw.base.InputEncryptedChat", typing: bool) -> None:
        self.peer = peer  # InputEncryptedChat
        self.typing = typing  # Bool

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SetEncryptedTyping":
        # No flags

        peer = TLObject.read(data)

        typing = Bool.read(data)

        return SetEncryptedTyping(peer=peer, typing=typing)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.peer.write())

        data.write(Bool(self.typing))

        return data.getvalue()
