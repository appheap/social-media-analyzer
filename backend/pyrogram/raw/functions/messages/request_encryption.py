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


class RequestEncryption(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0xf64daf43``

    Parameters:
        user_id: :obj:`InputUser <pyrogram.raw.base.InputUser>`
        random_id: ``int`` ``32-bit``
        g_a: ``bytes``

    Returns:
        :obj:`EncryptedChat <pyrogram.raw.base.EncryptedChat>`
    """

    __slots__: List[str] = ["user_id", "random_id", "g_a"]

    ID = 0xf64daf43
    QUALNAME = "functions.messages.RequestEncryption"

    def __init__(self, *, user_id: "raw.base.InputUser", random_id: int, g_a: bytes) -> None:
        self.user_id = user_id  # InputUser
        self.random_id = random_id  # int
        self.g_a = g_a  # bytes

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "RequestEncryption":
        # No flags

        user_id = TLObject.read(data)

        random_id = Int.read(data)

        g_a = Bytes.read(data)

        return RequestEncryption(user_id=user_id, random_id=random_id, g_a=g_a)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.user_id.write())

        data.write(Int(self.random_id))

        data.write(Bytes(self.g_a))

        return data.getvalue()
