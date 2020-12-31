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


class EditMessage(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0x48f71778``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        id: ``int`` ``32-bit``
        no_webpage (optional): ``bool``
        message (optional): ``str``
        media (optional): :obj:`InputMedia <pyrogram.raw.base.InputMedia>`
        reply_markup (optional): :obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`
        entities (optional): List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`
        schedule_date (optional): ``int`` ``32-bit``

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "id", "no_webpage", "message", "media", "reply_markup", "entities", "schedule_date"]

    ID = 0x48f71778
    QUALNAME = "functions.messages.EditMessage"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, no_webpage: Union[None, bool] = None,
                 message: Union[None, str] = None, media: "raw.base.InputMedia" = None,
                 reply_markup: "raw.base.ReplyMarkup" = None,
                 entities: Union[None, List["raw.base.MessageEntity"]] = None,
                 schedule_date: Union[None, int] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.no_webpage = no_webpage  # flags.1?true
        self.message = message  # flags.11?string
        self.media = media  # flags.14?InputMedia
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup
        self.entities = entities  # flags.3?Vector<MessageEntity>
        self.schedule_date = schedule_date  # flags.15?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "EditMessage":
        flags = Int.read(data)

        no_webpage = True if flags & (1 << 1) else False
        peer = TLObject.read(data)

        id = Int.read(data)

        message = String.read(data) if flags & (1 << 11) else None
        media = TLObject.read(data) if flags & (1 << 14) else None

        reply_markup = TLObject.read(data) if flags & (1 << 2) else None

        entities = TLObject.read(data) if flags & (1 << 3) else []

        schedule_date = Int.read(data) if flags & (1 << 15) else None
        return EditMessage(peer=peer, id=id, no_webpage=no_webpage, message=message, media=media,
                           reply_markup=reply_markup, entities=entities, schedule_date=schedule_date)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.no_webpage else 0
        flags |= (1 << 11) if self.message is not None else 0
        flags |= (1 << 14) if self.media is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        flags |= (1 << 3) if self.entities is not None else 0
        flags |= (1 << 15) if self.schedule_date is not None else 0
        data.write(Int(flags))

        data.write(self.peer.write())

        data.write(Int(self.id))

        if self.message is not None:
            data.write(String(self.message))

        if self.media is not None:
            data.write(self.media.write())

        if self.reply_markup is not None:
            data.write(self.reply_markup.write())

        if self.entities is not None:
            data.write(Vector(self.entities))

        if self.schedule_date is not None:
            data.write(Int(self.schedule_date))

        return data.getvalue()
