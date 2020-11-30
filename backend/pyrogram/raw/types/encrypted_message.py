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


class EncryptedMessage(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.EncryptedMessage`.

    Details:
        - Layer: ``117``
        - ID: ``0xed18c118``

    Parameters:
        random_id: ``int`` ``64-bit``
        chat_id: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        bytes: ``bytes``
        file: :obj:`EncryptedFile <pyrogram.raw.base.EncryptedFile>`
    """

    __slots__: List[str] = ["random_id", "chat_id", "date", "bytes", "file"]

    ID = 0xed18c118
    QUALNAME = "types.EncryptedMessage"

    def __init__(self, *, random_id: int, chat_id: int, date: int, bytes: bytes,
                 file: "raw.base.EncryptedFile") -> None:
        self.random_id = random_id  # long
        self.chat_id = chat_id  # int
        self.date = date  # int
        self.bytes = bytes  # bytes
        self.file = file  # EncryptedFile

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "EncryptedMessage":
        # No flags

        random_id = Long.read(data)

        chat_id = Int.read(data)

        date = Int.read(data)

        bytes = Bytes.read(data)

        file = TLObject.read(data)

        return EncryptedMessage(random_id=random_id, chat_id=chat_id, date=date, bytes=bytes, file=file)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Long(self.random_id))

        data.write(Int(self.chat_id))

        data.write(Int(self.date))

        data.write(Bytes(self.bytes))

        data.write(self.file.write())

        return data.getvalue()
