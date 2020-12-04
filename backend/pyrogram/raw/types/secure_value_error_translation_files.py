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


class SecureValueErrorTranslationFiles(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.SecureValueError`.

    Details:
        - Layer: ``120``
        - ID: ``0x34636dd8``

    Parameters:
        type: :obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`
        file_hash: List of ``bytes``
        text: ``str``
    """

    __slots__: List[str] = ["type", "file_hash", "text"]

    ID = 0x34636dd8
    QUALNAME = "types.SecureValueErrorTranslationFiles"

    def __init__(self, *, type: "raw.base.SecureValueType", file_hash: List[bytes], text: str) -> None:
        self.type = type  # SecureValueType
        self.file_hash = file_hash  # Vector<bytes>
        self.text = text  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SecureValueErrorTranslationFiles":
        # No flags

        type = TLObject.read(data)

        file_hash = TLObject.read(data, Bytes)

        text = String.read(data)

        return SecureValueErrorTranslationFiles(type=type, file_hash=file_hash, text=text)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.type.write())

        data.write(Vector(self.file_hash, Bytes))

        data.write(String(self.text))

        return data.getvalue()
