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


class DeleteChatUser(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0xc534459a``

    Parameters:
        chat_id: ``int`` ``32-bit``
        user_id: :obj:`InputUser <pyrogram.raw.base.InputUser>`
        revoke_history (optional): ``bool``

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["chat_id", "user_id", "revoke_history"]

    ID = 0xc534459a
    QUALNAME = "functions.messages.DeleteChatUser"

    def __init__(self, *, chat_id: int, user_id: "raw.base.InputUser",
                 revoke_history: Union[None, bool] = None) -> None:
        self.chat_id = chat_id  # int
        self.user_id = user_id  # InputUser
        self.revoke_history = revoke_history  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "DeleteChatUser":
        flags = Int.read(data)

        revoke_history = True if flags & (1 << 0) else False
        chat_id = Int.read(data)

        user_id = TLObject.read(data)

        return DeleteChatUser(chat_id=chat_id, user_id=user_id, revoke_history=revoke_history)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoke_history else 0
        data.write(Int(flags))

        data.write(Int(self.chat_id))

        data.write(self.user_id.write())

        return data.getvalue()
