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


class GetInlineBotResults(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x514e999d``

    Parameters:
        bot: :obj:`InputUser <pyrogram.raw.base.InputUser>`
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        query: ``str``
        offset: ``str``
        geo_point (optional): :obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`

    Returns:
        :obj:`messages.BotResults <pyrogram.raw.base.messages.BotResults>`
    """

    __slots__: List[str] = ["bot", "peer", "query", "offset", "geo_point"]

    ID = 0x514e999d
    QUALNAME = "functions.messages.GetInlineBotResults"

    def __init__(self, *, bot: "raw.base.InputUser", peer: "raw.base.InputPeer", query: str, offset: str,
                 geo_point: "raw.base.InputGeoPoint" = None) -> None:
        self.bot = bot  # InputUser
        self.peer = peer  # InputPeer
        self.query = query  # string
        self.offset = offset  # string
        self.geo_point = geo_point  # flags.0?InputGeoPoint

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetInlineBotResults":
        flags = Int.read(data)

        bot = TLObject.read(data)

        peer = TLObject.read(data)

        geo_point = TLObject.read(data) if flags & (1 << 0) else None

        query = String.read(data)

        offset = String.read(data)

        return GetInlineBotResults(bot=bot, peer=peer, query=query, offset=offset, geo_point=geo_point)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.geo_point is not None else 0
        data.write(Int(flags))

        data.write(self.bot.write())

        data.write(self.peer.write())

        if self.geo_point is not None:
            data.write(self.geo_point.write())

        data.write(String(self.query))

        data.write(String(self.offset))

        return data.getvalue()
