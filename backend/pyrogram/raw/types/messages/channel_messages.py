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


class ChannelMessages(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.Messages`.

    Details:
        - Layer: ``117``
        - ID: ``0x99262e37``

    Parameters:
        pts: ``int`` ``32-bit``
        count: ``int`` ``32-bit``
        messages: List of :obj:`Message <pyrogram.raw.base.Message>`
        chats: List of :obj:`Chat <pyrogram.raw.base.Chat>`
        users: List of :obj:`User <pyrogram.raw.base.User>`
        inexact (optional): ``bool``

    See Also:
        This object can be returned by 9 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetMessages <pyrogram.raw.functions.messages.GetMessages>`
            - :obj:`messages.GetHistory <pyrogram.raw.functions.messages.GetHistory>`
            - :obj:`messages.Search <pyrogram.raw.functions.messages.Search>`
            - :obj:`messages.SearchGlobal <pyrogram.raw.functions.messages.SearchGlobal>`
            - :obj:`messages.GetUnreadMentions <pyrogram.raw.functions.messages.GetUnreadMentions>`
            - :obj:`messages.GetRecentLocations <pyrogram.raw.functions.messages.GetRecentLocations>`
            - :obj:`messages.GetScheduledHistory <pyrogram.raw.functions.messages.GetScheduledHistory>`
            - :obj:`messages.GetScheduledMessages <pyrogram.raw.functions.messages.GetScheduledMessages>`
            - :obj:`channels.GetMessages <pyrogram.raw.functions.channels.GetMessages>`
    """

    __slots__: List[str] = ["pts", "count", "messages", "chats", "users", "inexact"]

    ID = 0x99262e37
    QUALNAME = "types.messages.ChannelMessages"

    def __init__(self, *, pts: int, count: int, messages: List["raw.base.Message"], chats: List["raw.base.Chat"],
                 users: List["raw.base.User"], inexact: Union[None, bool] = None) -> None:
        self.pts = pts  # int
        self.count = count  # int
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.inexact = inexact  # flags.1?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChannelMessages":
        flags = Int.read(data)

        inexact = True if flags & (1 << 1) else False
        pts = Int.read(data)

        count = Int.read(data)

        messages = TLObject.read(data)

        chats = TLObject.read(data)

        users = TLObject.read(data)

        return ChannelMessages(pts=pts, count=count, messages=messages, chats=chats, users=users, inexact=inexact)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.inexact is not None else 0
        data.write(Int(flags))

        data.write(Int(self.pts))

        data.write(Int(self.count))

        data.write(Vector(self.messages))

        data.write(Vector(self.chats))

        data.write(Vector(self.users))

        return data.getvalue()
