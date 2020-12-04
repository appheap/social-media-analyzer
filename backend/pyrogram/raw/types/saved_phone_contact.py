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


class SavedPhoneContact(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.SavedContact`.

    Details:
        - Layer: ``120``
        - ID: ``0x1142bd56``

    Parameters:
        phone: ``str``
        first_name: ``str``
        last_name: ``str``
        date: ``int`` ``32-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`contacts.GetSaved <pyrogram.raw.functions.contacts.GetSaved>`
    """

    __slots__: List[str] = ["phone", "first_name", "last_name", "date"]

    ID = 0x1142bd56
    QUALNAME = "types.SavedPhoneContact"

    def __init__(self, *, phone: str, first_name: str, last_name: str, date: int) -> None:
        self.phone = phone  # string
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.date = date  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SavedPhoneContact":
        # No flags

        phone = String.read(data)

        first_name = String.read(data)

        last_name = String.read(data)

        date = Int.read(data)

        return SavedPhoneContact(phone=phone, first_name=first_name, last_name=last_name, date=date)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.phone))

        data.write(String(self.first_name))

        data.write(String(self.last_name))

        data.write(Int(self.date))

        return data.getvalue()
