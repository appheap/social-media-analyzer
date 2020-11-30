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


class ChannelDifference(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.updates.ChannelDifference`.

    Details:
        - Layer: ``117``
        - ID: ``0x2064674e``

    Parameters:
        pts: ``int`` ``32-bit``
        new_messages: List of :obj:`Message <pyrogram.raw.base.Message>`
        other_updates: List of :obj:`Update <pyrogram.raw.base.Update>`
        chats: List of :obj:`Chat <pyrogram.raw.base.Chat>`
        users: List of :obj:`User <pyrogram.raw.base.User>`
        final (optional): ``bool``
        timeout (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`updates.GetChannelDifference <pyrogram.raw.functions.updates.GetChannelDifference>`
    """

    __slots__: List[str] = ["pts", "new_messages", "other_updates", "chats", "users", "final", "timeout"]

    ID = 0x2064674e
    QUALNAME = "types.updates.ChannelDifference"

    def __init__(self, *, pts: int, new_messages: List["raw.base.Message"], other_updates: List["raw.base.Update"],
                 chats: List["raw.base.Chat"], users: List["raw.base.User"], final: Union[None, bool] = None,
                 timeout: Union[None, int] = None) -> None:
        self.pts = pts  # int
        self.new_messages = new_messages  # Vector<Message>
        self.other_updates = other_updates  # Vector<Update>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.final = final  # flags.0?true
        self.timeout = timeout  # flags.1?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChannelDifference":
        flags = Int.read(data)

        final = True if flags & (1 << 0) else False
        pts = Int.read(data)

        timeout = Int.read(data) if flags & (1 << 1) else None
        new_messages = TLObject.read(data)

        other_updates = TLObject.read(data)

        chats = TLObject.read(data)

        users = TLObject.read(data)

        return ChannelDifference(pts=pts, new_messages=new_messages, other_updates=other_updates, chats=chats,
                                 users=users, final=final, timeout=timeout)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.final is not None else 0
        flags |= (1 << 1) if self.timeout is not None else 0
        data.write(Int(flags))

        data.write(Int(self.pts))

        if self.timeout is not None:
            data.write(Int(self.timeout))

        data.write(Vector(self.new_messages))

        data.write(Vector(self.other_updates))

        data.write(Vector(self.chats))

        data.write(Vector(self.users))

        return data.getvalue()
