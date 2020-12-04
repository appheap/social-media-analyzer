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


class UpdateServiceNotification(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``120``
        - ID: ``0xebe46819``

    Parameters:
        type: ``str``
        message: ``str``
        media: :obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`
        entities: List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`
        popup (optional): ``bool``
        inbox_date (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["type", "message", "media", "entities", "popup", "inbox_date"]

    ID = 0xebe46819
    QUALNAME = "types.UpdateServiceNotification"

    def __init__(self, *, type: str, message: str, media: "raw.base.MessageMedia",
                 entities: List["raw.base.MessageEntity"], popup: Union[None, bool] = None,
                 inbox_date: Union[None, int] = None) -> None:
        self.type = type  # string
        self.message = message  # string
        self.media = media  # MessageMedia
        self.entities = entities  # Vector<MessageEntity>
        self.popup = popup  # flags.0?true
        self.inbox_date = inbox_date  # flags.1?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateServiceNotification":
        flags = Int.read(data)

        popup = True if flags & (1 << 0) else False
        inbox_date = Int.read(data) if flags & (1 << 1) else None
        type = String.read(data)

        message = String.read(data)

        media = TLObject.read(data)

        entities = TLObject.read(data)

        return UpdateServiceNotification(type=type, message=message, media=media, entities=entities, popup=popup,
                                         inbox_date=inbox_date)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.popup is not None else 0
        flags |= (1 << 1) if self.inbox_date is not None else 0
        data.write(Int(flags))

        if self.inbox_date is not None:
            data.write(Int(self.inbox_date))

        data.write(String(self.type))

        data.write(String(self.message))

        data.write(self.media.write())

        data.write(Vector(self.entities))

        return data.getvalue()
