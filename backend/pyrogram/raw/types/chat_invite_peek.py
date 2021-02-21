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


class ChatInvitePeek(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChatInvite`.

    Details:
        - Layer: ``123``
        - ID: ``0x61695cb0``

    Parameters:
        chat: :obj:`Chat <pyrogram.raw.base.Chat>`
        expires: ``int`` ``32-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.CheckChatInvite <pyrogram.raw.functions.messages.CheckChatInvite>`
    """

    __slots__: List[str] = ["chat", "expires"]

    ID = 0x61695cb0
    QUALNAME = "types.ChatInvitePeek"

    def __init__(self, *, chat: "raw.base.Chat", expires: int) -> None:
        self.chat = chat  # Chat
        self.expires = expires  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChatInvitePeek":
        # No flags

        chat = TLObject.read(data)

        expires = Int.read(data)

        return ChatInvitePeek(chat=chat, expires=expires)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.chat.write())

        data.write(Int(self.expires))

        return data.getvalue()
