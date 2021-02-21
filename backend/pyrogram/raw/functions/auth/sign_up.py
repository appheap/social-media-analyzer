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


class SignUp(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x80eee427``

    Parameters:
        phone_number: ``str``
        phone_code_hash: ``str``
        first_name: ``str``
        last_name: ``str``

    Returns:
        :obj:`auth.Authorization <pyrogram.raw.base.auth.Authorization>`
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "first_name", "last_name"]

    ID = 0x80eee427
    QUALNAME = "functions.auth.SignUp"

    def __init__(self, *, phone_number: str, phone_code_hash: str, first_name: str, last_name: str) -> None:
        self.phone_number = phone_number  # string
        self.phone_code_hash = phone_code_hash  # string
        self.first_name = first_name  # string
        self.last_name = last_name  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SignUp":
        # No flags

        phone_number = String.read(data)

        phone_code_hash = String.read(data)

        first_name = String.read(data)

        last_name = String.read(data)

        return SignUp(phone_number=phone_number, phone_code_hash=phone_code_hash, first_name=first_name,
                      last_name=last_name)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.phone_number))

        data.write(String(self.phone_code_hash))

        data.write(String(self.first_name))

        data.write(String(self.last_name))

        return data.getvalue()
