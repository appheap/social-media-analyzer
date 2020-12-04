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


class SaveDraft(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0xbc39e14b``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        message: ``str``
        no_webpage (optional): ``bool``
        reply_to_msg_id (optional): ``int`` ``32-bit``
        entities (optional): List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "message", "no_webpage", "reply_to_msg_id", "entities"]

    ID = 0xbc39e14b
    QUALNAME = "functions.messages.SaveDraft"

    def __init__(self, *, peer: "raw.base.InputPeer", message: str, no_webpage: Union[None, bool] = None,
                 reply_to_msg_id: Union[None, int] = None,
                 entities: Union[None, List["raw.base.MessageEntity"]] = None) -> None:
        self.peer = peer  # InputPeer
        self.message = message  # string
        self.no_webpage = no_webpage  # flags.1?true
        self.reply_to_msg_id = reply_to_msg_id  # flags.0?int
        self.entities = entities  # flags.3?Vector<MessageEntity>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SaveDraft":
        flags = Int.read(data)

        no_webpage = True if flags & (1 << 1) else False
        reply_to_msg_id = Int.read(data) if flags & (1 << 0) else None
        peer = TLObject.read(data)

        message = String.read(data)

        entities = TLObject.read(data) if flags & (1 << 3) else []

        return SaveDraft(peer=peer, message=message, no_webpage=no_webpage, reply_to_msg_id=reply_to_msg_id,
                         entities=entities)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.no_webpage is not None else 0
        flags |= (1 << 0) if self.reply_to_msg_id is not None else 0
        flags |= (1 << 3) if self.entities is not None else 0
        data.write(Int(flags))

        if self.reply_to_msg_id is not None:
            data.write(Int(self.reply_to_msg_id))

        data.write(self.peer.write())

        data.write(String(self.message))

        if self.entities is not None:
            data.write(Vector(self.entities))

        return data.getvalue()
