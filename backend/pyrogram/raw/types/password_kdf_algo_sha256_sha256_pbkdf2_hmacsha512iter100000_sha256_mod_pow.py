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


class PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PasswordKdfAlgo`.

    Details:
        - Layer: ``123``
        - ID: ``0x3a912d4a``

    Parameters:
        salt1: ``bytes``
        salt2: ``bytes``
        g: ``int`` ``32-bit``
        p: ``bytes``
    """

    __slots__: List[str] = ["salt1", "salt2", "g", "p"]

    ID = 0x3a912d4a
    QUALNAME = "types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow"

    def __init__(self, *, salt1: bytes, salt2: bytes, g: int, p: bytes) -> None:
        self.salt1 = salt1  # bytes
        self.salt2 = salt2  # bytes
        self.g = g  # int
        self.p = p  # bytes

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow":
        # No flags

        salt1 = Bytes.read(data)

        salt2 = Bytes.read(data)

        g = Int.read(data)

        p = Bytes.read(data)

        return PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow(salt1=salt1, salt2=salt2, g=g, p=p)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Bytes(self.salt1))

        data.write(Bytes(self.salt2))

        data.write(Int(self.g))

        data.write(Bytes(self.p))

        return data.getvalue()
