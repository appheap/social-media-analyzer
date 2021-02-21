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


class ImportedContacts(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.contacts.ImportedContacts`.

    Details:
        - Layer: ``123``
        - ID: ``0x77d01c3b``

    Parameters:
        imported: List of :obj:`ImportedContact <pyrogram.raw.base.ImportedContact>`
        popular_invites: List of :obj:`PopularContact <pyrogram.raw.base.PopularContact>`
        retry_contacts: List of ``int`` ``64-bit``
        users: List of :obj:`User <pyrogram.raw.base.User>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`contacts.ImportContacts <pyrogram.raw.functions.contacts.ImportContacts>`
    """

    __slots__: List[str] = ["imported", "popular_invites", "retry_contacts", "users"]

    ID = 0x77d01c3b
    QUALNAME = "types.contacts.ImportedContacts"

    def __init__(self, *, imported: List["raw.base.ImportedContact"], popular_invites: List["raw.base.PopularContact"],
                 retry_contacts: List[int], users: List["raw.base.User"]) -> None:
        self.imported = imported  # Vector<ImportedContact>
        self.popular_invites = popular_invites  # Vector<PopularContact>
        self.retry_contacts = retry_contacts  # Vector<long>
        self.users = users  # Vector<User>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ImportedContacts":
        # No flags

        imported = TLObject.read(data)

        popular_invites = TLObject.read(data)

        retry_contacts = TLObject.read(data, Long)

        users = TLObject.read(data)

        return ImportedContacts(imported=imported, popular_invites=popular_invites, retry_contacts=retry_contacts,
                                users=users)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Vector(self.imported))

        data.write(Vector(self.popular_invites))

        data.write(Vector(self.retry_contacts, Long))

        data.write(Vector(self.users))

        return data.getvalue()
