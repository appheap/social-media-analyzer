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


class MessageFwdHeader(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.MessageFwdHeader`.

    Details:
        - Layer: ``120``
        - ID: ``0x5f777dce``

    Parameters:
        date: ``int`` ``32-bit``
        from_id (optional): :obj:`Peer <pyrogram.raw.base.Peer>`
        from_name (optional): ``str``
        channel_post (optional): ``int`` ``32-bit``
        post_author (optional): ``str``
        saved_from_peer (optional): :obj:`Peer <pyrogram.raw.base.Peer>`
        saved_from_msg_id (optional): ``int`` ``32-bit``
        psa_type (optional): ``str``
    """

    __slots__: List[str] = ["date", "from_id", "from_name", "channel_post", "post_author", "saved_from_peer",
                            "saved_from_msg_id", "psa_type"]

    ID = 0x5f777dce
    QUALNAME = "types.MessageFwdHeader"

    def __init__(self, *, date: int, from_id: "raw.base.Peer" = None, from_name: Union[None, str] = None,
                 channel_post: Union[None, int] = None, post_author: Union[None, str] = None,
                 saved_from_peer: "raw.base.Peer" = None, saved_from_msg_id: Union[None, int] = None,
                 psa_type: Union[None, str] = None) -> None:
        self.date = date  # int
        self.from_id = from_id  # flags.0?Peer
        self.from_name = from_name  # flags.5?string
        self.channel_post = channel_post  # flags.2?int
        self.post_author = post_author  # flags.3?string
        self.saved_from_peer = saved_from_peer  # flags.4?Peer
        self.saved_from_msg_id = saved_from_msg_id  # flags.4?int
        self.psa_type = psa_type  # flags.6?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MessageFwdHeader":
        flags = Int.read(data)

        from_id = TLObject.read(data) if flags & (1 << 0) else None

        from_name = String.read(data) if flags & (1 << 5) else None
        date = Int.read(data)

        channel_post = Int.read(data) if flags & (1 << 2) else None
        post_author = String.read(data) if flags & (1 << 3) else None
        saved_from_peer = TLObject.read(data) if flags & (1 << 4) else None

        saved_from_msg_id = Int.read(data) if flags & (1 << 4) else None
        psa_type = String.read(data) if flags & (1 << 6) else None
        return MessageFwdHeader(date=date, from_id=from_id, from_name=from_name, channel_post=channel_post,
                                post_author=post_author, saved_from_peer=saved_from_peer,
                                saved_from_msg_id=saved_from_msg_id, psa_type=psa_type)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.from_id is not None else 0
        flags |= (1 << 5) if self.from_name is not None else 0
        flags |= (1 << 2) if self.channel_post is not None else 0
        flags |= (1 << 3) if self.post_author is not None else 0
        flags |= (1 << 4) if self.saved_from_peer is not None else 0
        flags |= (1 << 4) if self.saved_from_msg_id is not None else 0
        flags |= (1 << 6) if self.psa_type is not None else 0
        data.write(Int(flags))

        if self.from_id is not None:
            data.write(self.from_id.write())

        if self.from_name is not None:
            data.write(String(self.from_name))

        data.write(Int(self.date))

        if self.channel_post is not None:
            data.write(Int(self.channel_post))

        if self.post_author is not None:
            data.write(String(self.post_author))

        if self.saved_from_peer is not None:
            data.write(self.saved_from_peer.write())

        if self.saved_from_msg_id is not None:
            data.write(Int(self.saved_from_msg_id))

        if self.psa_type is not None:
            data.write(String(self.psa_type))

        return data.getvalue()
