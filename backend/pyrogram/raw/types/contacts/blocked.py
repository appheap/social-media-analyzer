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


class Blocked(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.contacts.Blocked`.

    Details:
        - Layer: ``122``
        - ID: ``0xade1591``

    Parameters:
        blocked: List of :obj:`PeerBlocked <pyrogram.raw.base.PeerBlocked>`
        chats: List of :obj:`Chat <pyrogram.raw.base.Chat>`
        users: List of :obj:`User <pyrogram.raw.base.User>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`contacts.GetBlocked <pyrogram.raw.functions.contacts.GetBlocked>`
    """

    __slots__: List[str] = ["blocked", "chats", "users"]

    ID = 0xade1591
    QUALNAME = "types.contacts.Blocked"

    def __init__(self, *, blocked: List["raw.base.PeerBlocked"], chats: List["raw.base.Chat"],
                 users: List["raw.base.User"]) -> None:
        self.blocked = blocked  # Vector<PeerBlocked>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Blocked":
        # No flags

        blocked = TLObject.read(data)

        chats = TLObject.read(data)

        users = TLObject.read(data)

        return Blocked(blocked=blocked, chats=chats, users=users)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Vector(self.blocked))

        data.write(Vector(self.chats))

        data.write(Vector(self.users))

        return data.getvalue()
