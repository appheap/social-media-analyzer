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


class UserInfo(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.help.UserInfo`.

    Details:
        - Layer: ``123``
        - ID: ``0x1eb3758``

    Parameters:
        message: ``str``
        entities: List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`
        author: ``str``
        date: ``int`` ``32-bit``

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`help.GetUserInfo <pyrogram.raw.functions.help.GetUserInfo>`
            - :obj:`help.EditUserInfo <pyrogram.raw.functions.help.EditUserInfo>`
    """

    __slots__: List[str] = ["message", "entities", "author", "date"]

    ID = 0x1eb3758
    QUALNAME = "types.help.UserInfo"

    def __init__(self, *, message: str, entities: List["raw.base.MessageEntity"], author: str, date: int) -> None:
        self.message = message  # string
        self.entities = entities  # Vector<MessageEntity>
        self.author = author  # string
        self.date = date  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UserInfo":
        # No flags

        message = String.read(data)

        entities = TLObject.read(data)

        author = String.read(data)

        date = Int.read(data)

        return UserInfo(message=message, entities=entities, author=author, date=date)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.message))

        data.write(Vector(self.entities))

        data.write(String(self.author))

        data.write(Int(self.date))

        return data.getvalue()
