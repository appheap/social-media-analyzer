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


class InputBotInlineMessageText(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputBotInlineMessage`.

    Details:
        - Layer: ``117``
        - ID: ``0x3dcd7a87``

    Parameters:
        message: ``str``
        no_webpage (optional): ``bool``
        entities (optional): List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`
        reply_markup (optional): :obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`
    """

    __slots__: List[str] = ["message", "no_webpage", "entities", "reply_markup"]

    ID = 0x3dcd7a87
    QUALNAME = "types.InputBotInlineMessageText"

    def __init__(self, *, message: str, no_webpage: Union[None, bool] = None,
                 entities: Union[None, List["raw.base.MessageEntity"]] = None,
                 reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.message = message  # string
        self.no_webpage = no_webpage  # flags.0?true
        self.entities = entities  # flags.1?Vector<MessageEntity>
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputBotInlineMessageText":
        flags = Int.read(data)

        no_webpage = True if flags & (1 << 0) else False
        message = String.read(data)

        entities = TLObject.read(data) if flags & (1 << 1) else []

        reply_markup = TLObject.read(data) if flags & (1 << 2) else None

        return InputBotInlineMessageText(message=message, no_webpage=no_webpage, entities=entities,
                                         reply_markup=reply_markup)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.no_webpage is not None else 0
        flags |= (1 << 1) if self.entities is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        data.write(Int(flags))

        data.write(String(self.message))

        if self.entities is not None:
            data.write(Vector(self.entities))

        if self.reply_markup is not None:
            data.write(self.reply_markup.write())

        return data.getvalue()
