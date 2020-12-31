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


class SendInlineBotResult(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0x220815b0``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        random_id: ``int`` ``64-bit``
        query_id: ``int`` ``64-bit``
        id: ``str``
        silent (optional): ``bool``
        background (optional): ``bool``
        clear_draft (optional): ``bool``
        hide_via (optional): ``bool``
        reply_to_msg_id (optional): ``int`` ``32-bit``
        schedule_date (optional): ``int`` ``32-bit``

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "random_id", "query_id", "id", "silent", "background", "clear_draft", "hide_via",
                            "reply_to_msg_id", "schedule_date"]

    ID = 0x220815b0
    QUALNAME = "functions.messages.SendInlineBotResult"

    def __init__(self, *, peer: "raw.base.InputPeer", random_id: int, query_id: int, id: str,
                 silent: Union[None, bool] = None, background: Union[None, bool] = None,
                 clear_draft: Union[None, bool] = None, hide_via: Union[None, bool] = None,
                 reply_to_msg_id: Union[None, int] = None, schedule_date: Union[None, int] = None) -> None:
        self.peer = peer  # InputPeer
        self.random_id = random_id  # long
        self.query_id = query_id  # long
        self.id = id  # string
        self.silent = silent  # flags.5?true
        self.background = background  # flags.6?true
        self.clear_draft = clear_draft  # flags.7?true
        self.hide_via = hide_via  # flags.11?true
        self.reply_to_msg_id = reply_to_msg_id  # flags.0?int
        self.schedule_date = schedule_date  # flags.10?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SendInlineBotResult":
        flags = Int.read(data)

        silent = True if flags & (1 << 5) else False
        background = True if flags & (1 << 6) else False
        clear_draft = True if flags & (1 << 7) else False
        hide_via = True if flags & (1 << 11) else False
        peer = TLObject.read(data)

        reply_to_msg_id = Int.read(data) if flags & (1 << 0) else None
        random_id = Long.read(data)

        query_id = Long.read(data)

        id = String.read(data)

        schedule_date = Int.read(data) if flags & (1 << 10) else None
        return SendInlineBotResult(peer=peer, random_id=random_id, query_id=query_id, id=id, silent=silent,
                                   background=background, clear_draft=clear_draft, hide_via=hide_via,
                                   reply_to_msg_id=reply_to_msg_id, schedule_date=schedule_date)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 6) if self.background else 0
        flags |= (1 << 7) if self.clear_draft else 0
        flags |= (1 << 11) if self.hide_via else 0
        flags |= (1 << 0) if self.reply_to_msg_id is not None else 0
        flags |= (1 << 10) if self.schedule_date is not None else 0
        data.write(Int(flags))

        data.write(self.peer.write())

        if self.reply_to_msg_id is not None:
            data.write(Int(self.reply_to_msg_id))

        data.write(Long(self.random_id))

        data.write(Long(self.query_id))

        data.write(String(self.id))

        if self.schedule_date is not None:
            data.write(Int(self.schedule_date))

        return data.getvalue()
