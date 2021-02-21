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


class ChatsSlice(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.Chats`.

    Details:
        - Layer: ``123``
        - ID: ``0x9cd81144``

    Parameters:
        count: ``int`` ``32-bit``
        chats: List of :obj:`Chat <pyrogram.raw.base.Chat>`

    See Also:
        This object can be returned by 7 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetChats <pyrogram.raw.functions.messages.GetChats>`
            - :obj:`messages.GetCommonChats <pyrogram.raw.functions.messages.GetCommonChats>`
            - :obj:`messages.GetAllChats <pyrogram.raw.functions.messages.GetAllChats>`
            - :obj:`channels.GetChannels <pyrogram.raw.functions.channels.GetChannels>`
            - :obj:`channels.GetAdminedPublicChannels <pyrogram.raw.functions.channels.GetAdminedPublicChannels>`
            - :obj:`channels.GetLeftChannels <pyrogram.raw.functions.channels.GetLeftChannels>`
            - :obj:`channels.GetGroupsForDiscussion <pyrogram.raw.functions.channels.GetGroupsForDiscussion>`
    """

    __slots__: List[str] = ["count", "chats"]

    ID = 0x9cd81144
    QUALNAME = "types.messages.ChatsSlice"

    def __init__(self, *, count: int, chats: List["raw.base.Chat"]) -> None:
        self.count = count  # int
        self.chats = chats  # Vector<Chat>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChatsSlice":
        # No flags

        count = Int.read(data)

        chats = TLObject.read(data)

        return ChatsSlice(count=count, chats=chats)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.count))

        data.write(Vector(self.chats))

        return data.getvalue()
