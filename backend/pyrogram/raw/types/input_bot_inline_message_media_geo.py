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


class InputBotInlineMessageMediaGeo(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputBotInlineMessage`.

    Details:
        - Layer: ``117``
        - ID: ``0xc1b15d65``

    Parameters:
        geo_point: :obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`
        period: ``int`` ``32-bit``
        reply_markup (optional): :obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`
    """

    __slots__: List[str] = ["geo_point", "period", "reply_markup"]

    ID = 0xc1b15d65
    QUALNAME = "types.InputBotInlineMessageMediaGeo"

    def __init__(self, *, geo_point: "raw.base.InputGeoPoint", period: int,
                 reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.geo_point = geo_point  # InputGeoPoint
        self.period = period  # int
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputBotInlineMessageMediaGeo":
        flags = Int.read(data)

        geo_point = TLObject.read(data)

        period = Int.read(data)

        reply_markup = TLObject.read(data) if flags & (1 << 2) else None

        return InputBotInlineMessageMediaGeo(geo_point=geo_point, period=period, reply_markup=reply_markup)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        data.write(Int(flags))

        data.write(self.geo_point.write())

        data.write(Int(self.period))

        if self.reply_markup is not None:
            data.write(self.reply_markup.write())

        return data.getvalue()
