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


class Contacts(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.contacts.Contacts`.

    Details:
        - Layer: ``120``
        - ID: ``0xeae87e42``

    Parameters:
        contacts: List of :obj:`Contact <pyrogram.raw.base.Contact>`
        saved_count: ``int`` ``32-bit``
        users: List of :obj:`User <pyrogram.raw.base.User>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`contacts.GetContacts <pyrogram.raw.functions.contacts.GetContacts>`
    """

    __slots__: List[str] = ["contacts", "saved_count", "users"]

    ID = 0xeae87e42
    QUALNAME = "types.contacts.Contacts"

    def __init__(self, *, contacts: List["raw.base.Contact"], saved_count: int, users: List["raw.base.User"]) -> None:
        self.contacts = contacts  # Vector<Contact>
        self.saved_count = saved_count  # int
        self.users = users  # Vector<User>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Contacts":
        # No flags

        contacts = TLObject.read(data)

        saved_count = Int.read(data)

        users = TLObject.read(data)

        return Contacts(contacts=contacts, saved_count=saved_count, users=users)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Vector(self.contacts))

        data.write(Int(self.saved_count))

        data.write(Vector(self.users))

        return data.getvalue()
