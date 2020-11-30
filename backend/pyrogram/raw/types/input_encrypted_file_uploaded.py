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


class InputEncryptedFileUploaded(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputEncryptedFile`.

    Details:
        - Layer: ``117``
        - ID: ``0x64bd0306``

    Parameters:
        id: ``int`` ``64-bit``
        parts: ``int`` ``32-bit``
        md5_checksum: ``str``
        key_fingerprint: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["id", "parts", "md5_checksum", "key_fingerprint"]

    ID = 0x64bd0306
    QUALNAME = "types.InputEncryptedFileUploaded"

    def __init__(self, *, id: int, parts: int, md5_checksum: str, key_fingerprint: int) -> None:
        self.id = id  # long
        self.parts = parts  # int
        self.md5_checksum = md5_checksum  # string
        self.key_fingerprint = key_fingerprint  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputEncryptedFileUploaded":
        # No flags

        id = Long.read(data)

        parts = Int.read(data)

        md5_checksum = String.read(data)

        key_fingerprint = Int.read(data)

        return InputEncryptedFileUploaded(id=id, parts=parts, md5_checksum=md5_checksum,
                                          key_fingerprint=key_fingerprint)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Long(self.id))

        data.write(Int(self.parts))

        data.write(String(self.md5_checksum))

        data.write(Int(self.key_fingerprint))

        return data.getvalue()
