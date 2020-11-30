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


class InputBotInlineResultDocument(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputBotInlineResult`.

    Details:
        - Layer: ``117``
        - ID: ``0xfff8fdc4``

    Parameters:
        id: ``str``
        type: ``str``
        document: :obj:`InputDocument <pyrogram.raw.base.InputDocument>`
        send_message: :obj:`InputBotInlineMessage <pyrogram.raw.base.InputBotInlineMessage>`
        title (optional): ``str``
        description (optional): ``str``
    """

    __slots__: List[str] = ["id", "type", "document", "send_message", "title", "description"]

    ID = 0xfff8fdc4
    QUALNAME = "types.InputBotInlineResultDocument"

    def __init__(self, *, id: str, type: str, document: "raw.base.InputDocument",
                 send_message: "raw.base.InputBotInlineMessage", title: Union[None, str] = None,
                 description: Union[None, str] = None) -> None:
        self.id = id  # string
        self.type = type  # string
        self.document = document  # InputDocument
        self.send_message = send_message  # InputBotInlineMessage
        self.title = title  # flags.1?string
        self.description = description  # flags.2?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputBotInlineResultDocument":
        flags = Int.read(data)

        id = String.read(data)

        type = String.read(data)

        title = String.read(data) if flags & (1 << 1) else None
        description = String.read(data) if flags & (1 << 2) else None
        document = TLObject.read(data)

        send_message = TLObject.read(data)

        return InputBotInlineResultDocument(id=id, type=type, document=document, send_message=send_message, title=title,
                                            description=description)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 2) if self.description is not None else 0
        data.write(Int(flags))

        data.write(String(self.id))

        data.write(String(self.type))

        if self.title is not None:
            data.write(String(self.title))

        if self.description is not None:
            data.write(String(self.description))

        data.write(self.document.write())

        data.write(self.send_message.write())

        return data.getvalue()
