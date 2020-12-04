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


class MessagesSlice(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.Messages`.

    Details:
        - Layer: ``120``
        - ID: ``0x3a54685e``

    Parameters:
        count: ``int`` ``32-bit``
        messages: List of :obj:`Message <pyrogram.raw.base.Message>`
        chats: List of :obj:`Chat <pyrogram.raw.base.Chat>`
        users: List of :obj:`User <pyrogram.raw.base.User>`
        inexact (optional): ``bool``
        next_rate (optional): ``int`` ``32-bit``
        offset_id_offset (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by 11 methods:

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
            - :obj:`messages.GetReplies <pyrogram.raw.functions.messages.GetReplies>`
            - :obj:`channels.GetMessages <pyrogram.raw.functions.channels.GetMessages>`
            - :obj:`stats.GetMessagePublicForwards <pyrogram.raw.functions.stats.GetMessagePublicForwards>`
    """

    __slots__: List[str] = ["count", "messages", "chats", "users", "inexact", "next_rate", "offset_id_offset"]

    ID = 0x3a54685e
    QUALNAME = "types.messages.MessagesSlice"

    def __init__(self, *, count: int, messages: List["raw.base.Message"], chats: List["raw.base.Chat"],
                 users: List["raw.base.User"], inexact: Union[None, bool] = None, next_rate: Union[None, int] = None,
                 offset_id_offset: Union[None, int] = None) -> None:
        self.count = count  # int
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.inexact = inexact  # flags.1?true
        self.next_rate = next_rate  # flags.0?int
        self.offset_id_offset = offset_id_offset  # flags.2?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MessagesSlice":
        flags = Int.read(data)

        inexact = True if flags & (1 << 1) else False
        count = Int.read(data)

        next_rate = Int.read(data) if flags & (1 << 0) else None
        offset_id_offset = Int.read(data) if flags & (1 << 2) else None
        messages = TLObject.read(data)

        chats = TLObject.read(data)

        users = TLObject.read(data)

        return MessagesSlice(count=count, messages=messages, chats=chats, users=users, inexact=inexact,
                             next_rate=next_rate, offset_id_offset=offset_id_offset)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.inexact is not None else 0
        flags |= (1 << 0) if self.next_rate is not None else 0
        flags |= (1 << 2) if self.offset_id_offset is not None else 0
        data.write(Int(flags))

        data.write(Int(self.count))

        if self.next_rate is not None:
            data.write(Int(self.next_rate))

        if self.offset_id_offset is not None:
            data.write(Int(self.offset_id_offset))

        data.write(Vector(self.messages))

        data.write(Vector(self.chats))

        data.write(Vector(self.users))

        return data.getvalue()
