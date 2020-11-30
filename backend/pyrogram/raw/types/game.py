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


class Game(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Game`.

    Details:
        - Layer: ``117``
        - ID: ``0xbdf9653b``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        short_name: ``str``
        title: ``str``
        description: ``str``
        photo: :obj:`Photo <pyrogram.raw.base.Photo>`
        document (optional): :obj:`Document <pyrogram.raw.base.Document>`
    """

    __slots__: List[str] = ["id", "access_hash", "short_name", "title", "description", "photo", "document"]

    ID = 0xbdf9653b
    QUALNAME = "types.Game"

    def __init__(self, *, id: int, access_hash: int, short_name: str, title: str, description: str,
                 photo: "raw.base.Photo", document: "raw.base.Document" = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.short_name = short_name  # string
        self.title = title  # string
        self.description = description  # string
        self.photo = photo  # Photo
        self.document = document  # flags.0?Document

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Game":
        flags = Int.read(data)

        id = Long.read(data)

        access_hash = Long.read(data)

        short_name = String.read(data)

        title = String.read(data)

        description = String.read(data)

        photo = TLObject.read(data)

        document = TLObject.read(data) if flags & (1 << 0) else None

        return Game(id=id, access_hash=access_hash, short_name=short_name, title=title, description=description,
                    photo=photo, document=document)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.document is not None else 0
        data.write(Int(flags))

        data.write(Long(self.id))

        data.write(Long(self.access_hash))

        data.write(String(self.short_name))

        data.write(String(self.title))

        data.write(String(self.description))

        data.write(self.photo.write())

        if self.document is not None:
            data.write(self.document.write())

        return data.getvalue()
