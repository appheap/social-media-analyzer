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


class BotInlineMessageMediaContact(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.BotInlineMessage`.

    Details:
        - Layer: ``117``
        - ID: ``0x18d1cdc2``

    Parameters:
        phone_number: ``str``
        first_name: ``str``
        last_name: ``str``
        vcard: ``str``
        reply_markup (optional): :obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`
    """

    __slots__: List[str] = ["phone_number", "first_name", "last_name", "vcard", "reply_markup"]

    ID = 0x18d1cdc2
    QUALNAME = "types.BotInlineMessageMediaContact"

    def __init__(self, *, phone_number: str, first_name: str, last_name: str, vcard: str,
                 reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.phone_number = phone_number  # string
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.vcard = vcard  # string
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "BotInlineMessageMediaContact":
        flags = Int.read(data)

        phone_number = String.read(data)

        first_name = String.read(data)

        last_name = String.read(data)

        vcard = String.read(data)

        reply_markup = TLObject.read(data) if flags & (1 << 2) else None

        return BotInlineMessageMediaContact(phone_number=phone_number, first_name=first_name, last_name=last_name,
                                            vcard=vcard, reply_markup=reply_markup)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        data.write(Int(flags))

        data.write(String(self.phone_number))

        data.write(String(self.first_name))

        data.write(String(self.last_name))

        data.write(String(self.vcard))

        if self.reply_markup is not None:
            data.write(self.reply_markup.write())

        return data.getvalue()
