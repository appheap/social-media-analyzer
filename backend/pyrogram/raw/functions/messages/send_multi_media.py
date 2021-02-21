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


class SendMultiMedia(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0xcc0110cb``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        multi_media: List of :obj:`InputSingleMedia <pyrogram.raw.base.InputSingleMedia>`
        silent (optional): ``bool``
        background (optional): ``bool``
        clear_draft (optional): ``bool``
        reply_to_msg_id (optional): ``int`` ``32-bit``
        schedule_date (optional): ``int`` ``32-bit``

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "multi_media", "silent", "background", "clear_draft", "reply_to_msg_id",
                            "schedule_date"]

    ID = 0xcc0110cb
    QUALNAME = "functions.messages.SendMultiMedia"

    def __init__(self, *, peer: "raw.base.InputPeer", multi_media: List["raw.base.InputSingleMedia"],
                 silent: Union[None, bool] = None, background: Union[None, bool] = None,
                 clear_draft: Union[None, bool] = None, reply_to_msg_id: Union[None, int] = None,
                 schedule_date: Union[None, int] = None) -> None:
        self.peer = peer  # InputPeer
        self.multi_media = multi_media  # Vector<InputSingleMedia>
        self.silent = silent  # flags.5?true
        self.background = background  # flags.6?true
        self.clear_draft = clear_draft  # flags.7?true
        self.reply_to_msg_id = reply_to_msg_id  # flags.0?int
        self.schedule_date = schedule_date  # flags.10?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SendMultiMedia":
        flags = Int.read(data)

        silent = True if flags & (1 << 5) else False
        background = True if flags & (1 << 6) else False
        clear_draft = True if flags & (1 << 7) else False
        peer = TLObject.read(data)

        reply_to_msg_id = Int.read(data) if flags & (1 << 0) else None
        multi_media = TLObject.read(data)

        schedule_date = Int.read(data) if flags & (1 << 10) else None
        return SendMultiMedia(peer=peer, multi_media=multi_media, silent=silent, background=background,
                              clear_draft=clear_draft, reply_to_msg_id=reply_to_msg_id, schedule_date=schedule_date)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 6) if self.background else 0
        flags |= (1 << 7) if self.clear_draft else 0
        flags |= (1 << 0) if self.reply_to_msg_id is not None else 0
        flags |= (1 << 10) if self.schedule_date is not None else 0
        data.write(Int(flags))

        data.write(self.peer.write())

        if self.reply_to_msg_id is not None:
            data.write(Int(self.reply_to_msg_id))

        data.write(Vector(self.multi_media))

        if self.schedule_date is not None:
            data.write(Int(self.schedule_date))

        return data.getvalue()
