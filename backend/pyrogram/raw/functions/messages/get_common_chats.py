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


class GetCommonChats(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0xd0a48c4``

    Parameters:
        user_id: :obj:`InputUser <pyrogram.raw.base.InputUser>`
        max_id: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``

    Returns:
        :obj:`messages.Chats <pyrogram.raw.base.messages.Chats>`
    """

    __slots__: List[str] = ["user_id", "max_id", "limit"]

    ID = 0xd0a48c4
    QUALNAME = "functions.messages.GetCommonChats"

    def __init__(self, *, user_id: "raw.base.InputUser", max_id: int, limit: int) -> None:
        self.user_id = user_id  # InputUser
        self.max_id = max_id  # int
        self.limit = limit  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetCommonChats":
        # No flags

        user_id = TLObject.read(data)

        max_id = Int.read(data)

        limit = Int.read(data)

        return GetCommonChats(user_id=user_id, max_id=max_id, limit=limit)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.user_id.write())

        data.write(Int(self.max_id))

        data.write(Int(self.limit))

        return data.getvalue()
