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


class AppUpdate(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.help.AppUpdate`.

    Details:
        - Layer: ``122``
        - ID: ``0x1da7158f``

    Parameters:
        id: ``int`` ``32-bit``
        version: ``str``
        text: ``str``
        entities: List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`
        can_not_skip (optional): ``bool``
        document (optional): :obj:`Document <pyrogram.raw.base.Document>`
        url (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`help.GetAppUpdate <pyrogram.raw.functions.help.GetAppUpdate>`
    """

    __slots__: List[str] = ["id", "version", "text", "entities", "can_not_skip", "document", "url"]

    ID = 0x1da7158f
    QUALNAME = "types.help.AppUpdate"

    def __init__(self, *, id: int, version: str, text: str, entities: List["raw.base.MessageEntity"],
                 can_not_skip: Union[None, bool] = None, document: "raw.base.Document" = None,
                 url: Union[None, str] = None) -> None:
        self.id = id  # int
        self.version = version  # string
        self.text = text  # string
        self.entities = entities  # Vector<MessageEntity>
        self.can_not_skip = can_not_skip  # flags.0?true
        self.document = document  # flags.1?Document
        self.url = url  # flags.2?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "AppUpdate":
        flags = Int.read(data)

        can_not_skip = True if flags & (1 << 0) else False
        id = Int.read(data)

        version = String.read(data)

        text = String.read(data)

        entities = TLObject.read(data)

        document = TLObject.read(data) if flags & (1 << 1) else None

        url = String.read(data) if flags & (1 << 2) else None
        return AppUpdate(id=id, version=version, text=text, entities=entities, can_not_skip=can_not_skip,
                         document=document, url=url)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.can_not_skip else 0
        flags |= (1 << 1) if self.document is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        data.write(Int(flags))

        data.write(Int(self.id))

        data.write(String(self.version))

        data.write(String(self.text))

        data.write(Vector(self.entities))

        if self.document is not None:
            data.write(self.document.write())

        if self.url is not None:
            data.write(String(self.url))

        return data.getvalue()
