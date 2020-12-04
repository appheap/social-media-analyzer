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


class InputSecureFileUploaded(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputSecureFile`.

    Details:
        - Layer: ``120``
        - ID: ``0x3334b0f0``

    Parameters:
        id: ``int`` ``64-bit``
        parts: ``int`` ``32-bit``
        md5_checksum: ``str``
        file_hash: ``bytes``
        secret: ``bytes``
    """

    __slots__: List[str] = ["id", "parts", "md5_checksum", "file_hash", "secret"]

    ID = 0x3334b0f0
    QUALNAME = "types.InputSecureFileUploaded"

    def __init__(self, *, id: int, parts: int, md5_checksum: str, file_hash: bytes, secret: bytes) -> None:
        self.id = id  # long
        self.parts = parts  # int
        self.md5_checksum = md5_checksum  # string
        self.file_hash = file_hash  # bytes
        self.secret = secret  # bytes

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputSecureFileUploaded":
        # No flags

        id = Long.read(data)

        parts = Int.read(data)

        md5_checksum = String.read(data)

        file_hash = Bytes.read(data)

        secret = Bytes.read(data)

        return InputSecureFileUploaded(id=id, parts=parts, md5_checksum=md5_checksum, file_hash=file_hash,
                                       secret=secret)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Long(self.id))

        data.write(Int(self.parts))

        data.write(String(self.md5_checksum))

        data.write(Bytes(self.file_hash))

        data.write(Bytes(self.secret))

        return data.getvalue()
