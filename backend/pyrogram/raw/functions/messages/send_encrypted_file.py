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


class SendEncryptedFile(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0x9a901b66``

    Parameters:
        peer: :obj:`InputEncryptedChat <pyrogram.raw.base.InputEncryptedChat>`
        random_id: ``int`` ``64-bit``
        data: ``bytes``
        file: :obj:`InputEncryptedFile <pyrogram.raw.base.InputEncryptedFile>`

    Returns:
        :obj:`messages.SentEncryptedMessage <pyrogram.raw.base.messages.SentEncryptedMessage>`
    """

    __slots__: List[str] = ["peer", "random_id", "data", "file"]

    ID = 0x9a901b66
    QUALNAME = "functions.messages.SendEncryptedFile"

    def __init__(self, *, peer: "raw.base.InputEncryptedChat", random_id: int, data: bytes,
                 file: "raw.base.InputEncryptedFile") -> None:
        self.peer = peer  # InputEncryptedChat
        self.random_id = random_id  # long
        self.data = data  # bytes
        self.file = file  # InputEncryptedFile

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SendEncryptedFile":
        # No flags

        peer = TLObject.read(data)

        random_id = Long.read(data)

        data = Bytes.read(data)

        file = TLObject.read(data)

        return SendEncryptedFile(peer=peer, random_id=random_id, data=data, file=file)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.peer.write())

        data.write(Long(self.random_id))

        data.write(Bytes(self.data))

        data.write(self.file.write())

        return data.getvalue()
