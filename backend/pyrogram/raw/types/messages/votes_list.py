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


class VotesList(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.VotesList`.

    Details:
        - Layer: ``123``
        - ID: ``0x823f649``

    Parameters:
        count: ``int`` ``32-bit``
        votes: List of :obj:`MessageUserVote <pyrogram.raw.base.MessageUserVote>`
        users: List of :obj:`User <pyrogram.raw.base.User>`
        next_offset (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetPollVotes <pyrogram.raw.functions.messages.GetPollVotes>`
    """

    __slots__: List[str] = ["count", "votes", "users", "next_offset"]

    ID = 0x823f649
    QUALNAME = "types.messages.VotesList"

    def __init__(self, *, count: int, votes: List["raw.base.MessageUserVote"], users: List["raw.base.User"],
                 next_offset: Union[None, str] = None) -> None:
        self.count = count  # int
        self.votes = votes  # Vector<MessageUserVote>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "VotesList":
        flags = Int.read(data)

        count = Int.read(data)

        votes = TLObject.read(data)

        users = TLObject.read(data)

        next_offset = String.read(data) if flags & (1 << 0) else None
        return VotesList(count=count, votes=votes, users=users, next_offset=next_offset)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        data.write(Int(flags))

        data.write(Int(self.count))

        data.write(Vector(self.votes))

        data.write(Vector(self.users))

        if self.next_offset is not None:
            data.write(String(self.next_offset))

        return data.getvalue()
