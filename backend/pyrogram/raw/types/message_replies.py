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


class MessageReplies(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.MessageReplies`.

    Details:
        - Layer: ``122``
        - ID: ``0x4128faac``

    Parameters:
        replies: ``int`` ``32-bit``
        replies_pts: ``int`` ``32-bit``
        comments (optional): ``bool``
        recent_repliers (optional): List of :obj:`Peer <pyrogram.raw.base.Peer>`
        channel_id (optional): ``int`` ``32-bit``
        max_id (optional): ``int`` ``32-bit``
        read_max_id (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["replies", "replies_pts", "comments", "recent_repliers", "channel_id", "max_id",
                            "read_max_id"]

    ID = 0x4128faac
    QUALNAME = "types.MessageReplies"

    def __init__(self, *, replies: int, replies_pts: int, comments: Union[None, bool] = None,
                 recent_repliers: Union[None, List["raw.base.Peer"]] = None, channel_id: Union[None, int] = None,
                 max_id: Union[None, int] = None, read_max_id: Union[None, int] = None) -> None:
        self.replies = replies  # int
        self.replies_pts = replies_pts  # int
        self.comments = comments  # flags.0?true
        self.recent_repliers = recent_repliers  # flags.1?Vector<Peer>
        self.channel_id = channel_id  # flags.0?int
        self.max_id = max_id  # flags.2?int
        self.read_max_id = read_max_id  # flags.3?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MessageReplies":
        flags = Int.read(data)

        comments = True if flags & (1 << 0) else False
        replies = Int.read(data)

        replies_pts = Int.read(data)

        recent_repliers = TLObject.read(data) if flags & (1 << 1) else []

        channel_id = Int.read(data) if flags & (1 << 0) else None
        max_id = Int.read(data) if flags & (1 << 2) else None
        read_max_id = Int.read(data) if flags & (1 << 3) else None
        return MessageReplies(replies=replies, replies_pts=replies_pts, comments=comments,
                              recent_repliers=recent_repliers, channel_id=channel_id, max_id=max_id,
                              read_max_id=read_max_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.comments else 0
        flags |= (1 << 1) if self.recent_repliers is not None else 0
        flags |= (1 << 0) if self.channel_id is not None else 0
        flags |= (1 << 2) if self.max_id is not None else 0
        flags |= (1 << 3) if self.read_max_id is not None else 0
        data.write(Int(flags))

        data.write(Int(self.replies))

        data.write(Int(self.replies_pts))

        if self.recent_repliers is not None:
            data.write(Vector(self.recent_repliers))

        if self.channel_id is not None:
            data.write(Int(self.channel_id))

        if self.max_id is not None:
            data.write(Int(self.max_id))

        if self.read_max_id is not None:
            data.write(Int(self.read_max_id))

        return data.getvalue()
