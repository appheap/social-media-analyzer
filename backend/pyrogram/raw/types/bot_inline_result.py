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


class BotInlineResult(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.BotInlineResult`.

    Details:
        - Layer: ``117``
        - ID: ``0x11965f3a``

    Parameters:
        id: ``str``
        type: ``str``
        send_message: :obj:`BotInlineMessage <pyrogram.raw.base.BotInlineMessage>`
        title (optional): ``str``
        description (optional): ``str``
        url (optional): ``str``
        thumb (optional): :obj:`WebDocument <pyrogram.raw.base.WebDocument>`
        content (optional): :obj:`WebDocument <pyrogram.raw.base.WebDocument>`
    """

    __slots__: List[str] = ["id", "type", "send_message", "title", "description", "url", "thumb", "content"]

    ID = 0x11965f3a
    QUALNAME = "types.BotInlineResult"

    def __init__(self, *, id: str, type: str, send_message: "raw.base.BotInlineMessage", title: Union[None, str] = None,
                 description: Union[None, str] = None, url: Union[None, str] = None,
                 thumb: "raw.base.WebDocument" = None, content: "raw.base.WebDocument" = None) -> None:
        self.id = id  # string
        self.type = type  # string
        self.send_message = send_message  # BotInlineMessage
        self.title = title  # flags.1?string
        self.description = description  # flags.2?string
        self.url = url  # flags.3?string
        self.thumb = thumb  # flags.4?WebDocument
        self.content = content  # flags.5?WebDocument

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "BotInlineResult":
        flags = Int.read(data)

        id = String.read(data)

        type = String.read(data)

        title = String.read(data) if flags & (1 << 1) else None
        description = String.read(data) if flags & (1 << 2) else None
        url = String.read(data) if flags & (1 << 3) else None
        thumb = TLObject.read(data) if flags & (1 << 4) else None

        content = TLObject.read(data) if flags & (1 << 5) else None

        send_message = TLObject.read(data)

        return BotInlineResult(id=id, type=type, send_message=send_message, title=title, description=description,
                               url=url, thumb=thumb, content=content)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 2) if self.description is not None else 0
        flags |= (1 << 3) if self.url is not None else 0
        flags |= (1 << 4) if self.thumb is not None else 0
        flags |= (1 << 5) if self.content is not None else 0
        data.write(Int(flags))

        data.write(String(self.id))

        data.write(String(self.type))

        if self.title is not None:
            data.write(String(self.title))

        if self.description is not None:
            data.write(String(self.description))

        if self.url is not None:
            data.write(String(self.url))

        if self.thumb is not None:
            data.write(self.thumb.write())

        if self.content is not None:
            data.write(self.content.write())

        data.write(self.send_message.write())

        return data.getvalue()
