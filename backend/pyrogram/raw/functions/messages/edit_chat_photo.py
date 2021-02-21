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


class EditChatPhoto(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0xca4c79d8``

    Parameters:
        chat_id: ``int`` ``32-bit``
        photo: :obj:`InputChatPhoto <pyrogram.raw.base.InputChatPhoto>`

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["chat_id", "photo"]

    ID = 0xca4c79d8
    QUALNAME = "functions.messages.EditChatPhoto"

    def __init__(self, *, chat_id: int, photo: "raw.base.InputChatPhoto") -> None:
        self.chat_id = chat_id  # int
        self.photo = photo  # InputChatPhoto

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "EditChatPhoto":
        # No flags

        chat_id = Int.read(data)

        photo = TLObject.read(data)

        return EditChatPhoto(chat_id=chat_id, photo=photo)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.chat_id))

        data.write(self.photo.write())

        return data.getvalue()
