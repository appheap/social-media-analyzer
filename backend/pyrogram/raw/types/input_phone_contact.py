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


class InputPhoneContact(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputContact`.

    Details:
        - Layer: ``120``
        - ID: ``0xf392b7f4``

    Parameters:
        client_id: ``int`` ``64-bit``
        phone: ``str``
        first_name: ``str``
        last_name: ``str``
    """

    __slots__: List[str] = ["client_id", "phone", "first_name", "last_name"]

    ID = 0xf392b7f4
    QUALNAME = "types.InputPhoneContact"

    def __init__(self, *, client_id: int, phone: str, first_name: str, last_name: str) -> None:
        self.client_id = client_id  # long
        self.phone = phone  # string
        self.first_name = first_name  # string
        self.last_name = last_name  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputPhoneContact":
        # No flags

        client_id = Long.read(data)

        phone = String.read(data)

        first_name = String.read(data)

        last_name = String.read(data)

        return InputPhoneContact(client_id=client_id, phone=phone, first_name=first_name, last_name=last_name)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Long(self.client_id))

        data.write(String(self.phone))

        data.write(String(self.first_name))

        data.write(String(self.last_name))

        return data.getvalue()
