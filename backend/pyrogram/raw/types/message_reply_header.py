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


class MessageReplyHeader(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.MessageReplyHeader`.

    Details:
        - Layer: ``120``
        - ID: ``0xa6d57763``

    Parameters:
        reply_to_msg_id: ``int`` ``32-bit``
        reply_to_peer_id (optional): :obj:`Peer <pyrogram.raw.base.Peer>`
        reply_to_top_id (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["reply_to_msg_id", "reply_to_peer_id", "reply_to_top_id"]

    ID = 0xa6d57763
    QUALNAME = "types.MessageReplyHeader"

    def __init__(self, *, reply_to_msg_id: int, reply_to_peer_id: "raw.base.Peer" = None,
                 reply_to_top_id: Union[None, int] = None) -> None:
        self.reply_to_msg_id = reply_to_msg_id  # int
        self.reply_to_peer_id = reply_to_peer_id  # flags.0?Peer
        self.reply_to_top_id = reply_to_top_id  # flags.1?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MessageReplyHeader":
        flags = Int.read(data)

        reply_to_msg_id = Int.read(data)

        reply_to_peer_id = TLObject.read(data) if flags & (1 << 0) else None

        reply_to_top_id = Int.read(data) if flags & (1 << 1) else None
        return MessageReplyHeader(reply_to_msg_id=reply_to_msg_id, reply_to_peer_id=reply_to_peer_id,
                                  reply_to_top_id=reply_to_top_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.reply_to_peer_id is not None else 0
        flags |= (1 << 1) if self.reply_to_top_id is not None else 0
        data.write(Int(flags))

        data.write(Int(self.reply_to_msg_id))

        if self.reply_to_peer_id is not None:
            data.write(self.reply_to_peer_id.write())

        if self.reply_to_top_id is not None:
            data.write(Int(self.reply_to_top_id))

        return data.getvalue()
