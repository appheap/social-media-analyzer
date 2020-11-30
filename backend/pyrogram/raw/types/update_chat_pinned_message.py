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


class UpdateChatPinnedMessage(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``117``
        - ID: ``0xe10db349``

    Parameters:
        chat_id: ``int`` ``32-bit``
        id: ``int`` ``32-bit``
        version: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["chat_id", "id", "version"]

    ID = 0xe10db349
    QUALNAME = "types.UpdateChatPinnedMessage"

    def __init__(self, *, chat_id: int, id: int, version: int) -> None:
        self.chat_id = chat_id  # int
        self.id = id  # int
        self.version = version  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateChatPinnedMessage":
        # No flags

        chat_id = Int.read(data)

        id = Int.read(data)

        version = Int.read(data)

        return UpdateChatPinnedMessage(chat_id=chat_id, id=id, version=version)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.chat_id))

        data.write(Int(self.id))

        data.write(Int(self.version))

        return data.getvalue()
