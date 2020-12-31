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


class GetMessagePublicForwards(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0x5630281b``

    Parameters:
        channel: :obj:`InputChannel <pyrogram.raw.base.InputChannel>`
        msg_id: ``int`` ``32-bit``
        offset_rate: ``int`` ``32-bit``
        offset_peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        offset_id: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["channel", "msg_id", "offset_rate", "offset_peer", "offset_id", "limit"]

    ID = 0x5630281b
    QUALNAME = "functions.stats.GetMessagePublicForwards"

    def __init__(self, *, channel: "raw.base.InputChannel", msg_id: int, offset_rate: int,
                 offset_peer: "raw.base.InputPeer", offset_id: int, limit: int) -> None:
        self.channel = channel  # InputChannel
        self.msg_id = msg_id  # int
        self.offset_rate = offset_rate  # int
        self.offset_peer = offset_peer  # InputPeer
        self.offset_id = offset_id  # int
        self.limit = limit  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetMessagePublicForwards":
        # No flags

        channel = TLObject.read(data)

        msg_id = Int.read(data)

        offset_rate = Int.read(data)

        offset_peer = TLObject.read(data)

        offset_id = Int.read(data)

        limit = Int.read(data)

        return GetMessagePublicForwards(channel=channel, msg_id=msg_id, offset_rate=offset_rate,
                                        offset_peer=offset_peer, offset_id=offset_id, limit=limit)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.channel.write())

        data.write(Int(self.msg_id))

        data.write(Int(self.offset_rate))

        data.write(self.offset_peer.write())

        data.write(Int(self.offset_id))

        data.write(Int(self.limit))

        return data.getvalue()
