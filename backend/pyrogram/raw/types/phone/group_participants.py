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


class GroupParticipants(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.phone.GroupParticipants`.

    Details:
        - Layer: ``122``
        - ID: ``0x9cfeb92d``

    Parameters:
        count: ``int`` ``32-bit``
        participants: List of :obj:`GroupCallParticipant <pyrogram.raw.base.GroupCallParticipant>`
        next_offset: ``str``
        users: List of :obj:`User <pyrogram.raw.base.User>`
        version: ``int`` ``32-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`phone.GetGroupParticipants <pyrogram.raw.functions.phone.GetGroupParticipants>`
    """

    __slots__: List[str] = ["count", "participants", "next_offset", "users", "version"]

    ID = 0x9cfeb92d
    QUALNAME = "types.phone.GroupParticipants"

    def __init__(self, *, count: int, participants: List["raw.base.GroupCallParticipant"], next_offset: str,
                 users: List["raw.base.User"], version: int) -> None:
        self.count = count  # int
        self.participants = participants  # Vector<GroupCallParticipant>
        self.next_offset = next_offset  # string
        self.users = users  # Vector<User>
        self.version = version  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GroupParticipants":
        # No flags

        count = Int.read(data)

        participants = TLObject.read(data)

        next_offset = String.read(data)

        users = TLObject.read(data)

        version = Int.read(data)

        return GroupParticipants(count=count, participants=participants, next_offset=next_offset, users=users,
                                 version=version)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.count))

        data.write(Vector(self.participants))

        data.write(String(self.next_offset))

        data.write(Vector(self.users))

        data.write(Int(self.version))

        return data.getvalue()
