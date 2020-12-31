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


class ChatInvite(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChatInvite`.

    Details:
        - Layer: ``122``
        - ID: ``0xdfc2f58e``

    Parameters:
        title: ``str``
        photo: :obj:`Photo <pyrogram.raw.base.Photo>`
        participants_count: ``int`` ``32-bit``
        channel (optional): ``bool``
        broadcast (optional): ``bool``
        public (optional): ``bool``
        megagroup (optional): ``bool``
        participants (optional): List of :obj:`User <pyrogram.raw.base.User>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.CheckChatInvite <pyrogram.raw.functions.messages.CheckChatInvite>`
    """

    __slots__: List[str] = ["title", "photo", "participants_count", "channel", "broadcast", "public", "megagroup",
                            "participants"]

    ID = 0xdfc2f58e
    QUALNAME = "types.ChatInvite"

    def __init__(self, *, title: str, photo: "raw.base.Photo", participants_count: int,
                 channel: Union[None, bool] = None, broadcast: Union[None, bool] = None,
                 public: Union[None, bool] = None, megagroup: Union[None, bool] = None,
                 participants: Union[None, List["raw.base.User"]] = None) -> None:
        self.title = title  # string
        self.photo = photo  # Photo
        self.participants_count = participants_count  # int
        self.channel = channel  # flags.0?true
        self.broadcast = broadcast  # flags.1?true
        self.public = public  # flags.2?true
        self.megagroup = megagroup  # flags.3?true
        self.participants = participants  # flags.4?Vector<User>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChatInvite":
        flags = Int.read(data)

        channel = True if flags & (1 << 0) else False
        broadcast = True if flags & (1 << 1) else False
        public = True if flags & (1 << 2) else False
        megagroup = True if flags & (1 << 3) else False
        title = String.read(data)

        photo = TLObject.read(data)

        participants_count = Int.read(data)

        participants = TLObject.read(data) if flags & (1 << 4) else []

        return ChatInvite(title=title, photo=photo, participants_count=participants_count, channel=channel,
                          broadcast=broadcast, public=public, megagroup=megagroup, participants=participants)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.channel else 0
        flags |= (1 << 1) if self.broadcast else 0
        flags |= (1 << 2) if self.public else 0
        flags |= (1 << 3) if self.megagroup else 0
        flags |= (1 << 4) if self.participants is not None else 0
        data.write(Int(flags))

        data.write(String(self.title))

        data.write(self.photo.write())

        data.write(Int(self.participants_count))

        if self.participants is not None:
            data.write(Vector(self.participants))

        return data.getvalue()
