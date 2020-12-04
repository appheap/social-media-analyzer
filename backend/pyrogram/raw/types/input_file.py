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


class InputFile(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputFile`.

    Details:
        - Layer: ``120``
        - ID: ``0xf52ff27f``

    Parameters:
        id: ``int`` ``64-bit``
        parts: ``int`` ``32-bit``
        name: ``str``
        md5_checksum: ``str``
    """

    __slots__: List[str] = ["id", "parts", "name", "md5_checksum"]

    ID = 0xf52ff27f
    QUALNAME = "types.InputFile"

    def __init__(self, *, id: int, parts: int, name: str, md5_checksum: str) -> None:
        self.id = id  # long
        self.parts = parts  # int
        self.name = name  # string
        self.md5_checksum = md5_checksum  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputFile":
        # No flags

        id = Long.read(data)

        parts = Int.read(data)

        name = String.read(data)

        md5_checksum = String.read(data)

        return InputFile(id=id, parts=parts, name=name, md5_checksum=md5_checksum)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Long(self.id))

        data.write(Int(self.parts))

        data.write(String(self.name))

        data.write(String(self.md5_checksum))

        return data.getvalue()
