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


class SetInlineGameScore(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x15ad9f64``

    Parameters:
        id: :obj:`InputBotInlineMessageID <pyrogram.raw.base.InputBotInlineMessageID>`
        user_id: :obj:`InputUser <pyrogram.raw.base.InputUser>`
        score: ``int`` ``32-bit``
        edit_message (optional): ``bool``
        force (optional): ``bool``

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "user_id", "score", "edit_message", "force"]

    ID = 0x15ad9f64
    QUALNAME = "functions.messages.SetInlineGameScore"

    def __init__(self, *, id: "raw.base.InputBotInlineMessageID", user_id: "raw.base.InputUser", score: int,
                 edit_message: Union[None, bool] = None, force: Union[None, bool] = None) -> None:
        self.id = id  # InputBotInlineMessageID
        self.user_id = user_id  # InputUser
        self.score = score  # int
        self.edit_message = edit_message  # flags.0?true
        self.force = force  # flags.1?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SetInlineGameScore":
        flags = Int.read(data)

        edit_message = True if flags & (1 << 0) else False
        force = True if flags & (1 << 1) else False
        id = TLObject.read(data)

        user_id = TLObject.read(data)

        score = Int.read(data)

        return SetInlineGameScore(id=id, user_id=user_id, score=score, edit_message=edit_message, force=force)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.edit_message else 0
        flags |= (1 << 1) if self.force else 0
        data.write(Int(flags))

        data.write(self.id.write())

        data.write(self.user_id.write())

        data.write(Int(self.score))

        return data.getvalue()
