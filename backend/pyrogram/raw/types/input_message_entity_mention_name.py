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


class InputMessageEntityMentionName(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``122``
        - ID: ``0x208e68c9``

    Parameters:
        offset: ``int`` ``32-bit``
        length: ``int`` ``32-bit``
        user_id: :obj:`InputUser <pyrogram.raw.base.InputUser>`
    """

    __slots__: List[str] = ["offset", "length", "user_id"]

    ID = 0x208e68c9
    QUALNAME = "types.InputMessageEntityMentionName"

    def __init__(self, *, offset: int, length: int, user_id: "raw.base.InputUser") -> None:
        self.offset = offset  # int
        self.length = length  # int
        self.user_id = user_id  # InputUser

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputMessageEntityMentionName":
        # No flags

        offset = Int.read(data)

        length = Int.read(data)

        user_id = TLObject.read(data)

        return InputMessageEntityMentionName(offset=offset, length=length, user_id=user_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.offset))

        data.write(Int(self.length))

        data.write(self.user_id.write())

        return data.getvalue()
