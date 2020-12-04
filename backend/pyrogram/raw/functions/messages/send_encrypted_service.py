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


class SendEncryptedService(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0x32d439a4``

    Parameters:
        peer: :obj:`InputEncryptedChat <pyrogram.raw.base.InputEncryptedChat>`
        random_id: ``int`` ``64-bit``
        data: ``bytes``

    Returns:
        :obj:`messages.SentEncryptedMessage <pyrogram.raw.base.messages.SentEncryptedMessage>`
    """

    __slots__: List[str] = ["peer", "random_id", "data"]

    ID = 0x32d439a4
    QUALNAME = "functions.messages.SendEncryptedService"

    def __init__(self, *, peer: "raw.base.InputEncryptedChat", random_id: int, data: bytes) -> None:
        self.peer = peer  # InputEncryptedChat
        self.random_id = random_id  # long
        self.data = data  # bytes

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SendEncryptedService":
        # No flags

        peer = TLObject.read(data)

        random_id = Long.read(data)

        data = Bytes.read(data)

        return SendEncryptedService(peer=peer, random_id=random_id, data=data)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.peer.write())

        data.write(Long(self.random_id))

        data.write(Bytes(self.data))

        return data.getvalue()
