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


class UpdateBotInlineQuery(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``123``
        - ID: ``0x3f2038db``

    Parameters:
        query_id: ``int`` ``64-bit``
        user_id: ``int`` ``32-bit``
        query: ``str``
        offset: ``str``
        geo (optional): :obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`
        peer_type (optional): :obj:`InlineQueryPeerType <pyrogram.raw.base.InlineQueryPeerType>`
    """

    __slots__: List[str] = ["query_id", "user_id", "query", "offset", "geo", "peer_type"]

    ID = 0x3f2038db
    QUALNAME = "types.UpdateBotInlineQuery"

    def __init__(self, *, query_id: int, user_id: int, query: str, offset: str, geo: "raw.base.GeoPoint" = None,
                 peer_type: "raw.base.InlineQueryPeerType" = None) -> None:
        self.query_id = query_id  # long
        self.user_id = user_id  # int
        self.query = query  # string
        self.offset = offset  # string
        self.geo = geo  # flags.0?GeoPoint
        self.peer_type = peer_type  # flags.1?InlineQueryPeerType

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateBotInlineQuery":
        flags = Int.read(data)

        query_id = Long.read(data)

        user_id = Int.read(data)

        query = String.read(data)

        geo = TLObject.read(data) if flags & (1 << 0) else None

        peer_type = TLObject.read(data) if flags & (1 << 1) else None

        offset = String.read(data)

        return UpdateBotInlineQuery(query_id=query_id, user_id=user_id, query=query, offset=offset, geo=geo,
                                    peer_type=peer_type)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.geo is not None else 0
        flags |= (1 << 1) if self.peer_type is not None else 0
        data.write(Int(flags))

        data.write(Long(self.query_id))

        data.write(Int(self.user_id))

        data.write(String(self.query))

        if self.geo is not None:
            data.write(self.geo.write())

        if self.peer_type is not None:
            data.write(self.peer_type.write())

        data.write(String(self.offset))

        return data.getvalue()
