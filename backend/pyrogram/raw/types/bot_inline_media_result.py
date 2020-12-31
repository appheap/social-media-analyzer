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


class BotInlineMediaResult(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.BotInlineResult`.

    Details:
        - Layer: ``122``
        - ID: ``0x17db940b``

    Parameters:
        id: ``str``
        type: ``str``
        send_message: :obj:`BotInlineMessage <pyrogram.raw.base.BotInlineMessage>`
        photo (optional): :obj:`Photo <pyrogram.raw.base.Photo>`
        document (optional): :obj:`Document <pyrogram.raw.base.Document>`
        title (optional): ``str``
        description (optional): ``str``
    """

    __slots__: List[str] = ["id", "type", "send_message", "photo", "document", "title", "description"]

    ID = 0x17db940b
    QUALNAME = "types.BotInlineMediaResult"

    def __init__(self, *, id: str, type: str, send_message: "raw.base.BotInlineMessage", photo: "raw.base.Photo" = None,
                 document: "raw.base.Document" = None, title: Union[None, str] = None,
                 description: Union[None, str] = None) -> None:
        self.id = id  # string
        self.type = type  # string
        self.send_message = send_message  # BotInlineMessage
        self.photo = photo  # flags.0?Photo
        self.document = document  # flags.1?Document
        self.title = title  # flags.2?string
        self.description = description  # flags.3?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "BotInlineMediaResult":
        flags = Int.read(data)

        id = String.read(data)

        type = String.read(data)

        photo = TLObject.read(data) if flags & (1 << 0) else None

        document = TLObject.read(data) if flags & (1 << 1) else None

        title = String.read(data) if flags & (1 << 2) else None
        description = String.read(data) if flags & (1 << 3) else None
        send_message = TLObject.read(data)

        return BotInlineMediaResult(id=id, type=type, send_message=send_message, photo=photo, document=document,
                                    title=title, description=description)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 1) if self.document is not None else 0
        flags |= (1 << 2) if self.title is not None else 0
        flags |= (1 << 3) if self.description is not None else 0
        data.write(Int(flags))

        data.write(String(self.id))

        data.write(String(self.type))

        if self.photo is not None:
            data.write(self.photo.write())

        if self.document is not None:
            data.write(self.document.write())

        if self.title is not None:
            data.write(String(self.title))

        if self.description is not None:
            data.write(String(self.description))

        data.write(self.send_message.write())

        return data.getvalue()
