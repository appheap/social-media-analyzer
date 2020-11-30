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


class Page(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Page`.

    Details:
        - Layer: ``117``
        - ID: ``0x98657f0d``

    Parameters:
        url: ``str``
        blocks: List of :obj:`PageBlock <pyrogram.raw.base.PageBlock>`
        photos: List of :obj:`Photo <pyrogram.raw.base.Photo>`
        documents: List of :obj:`Document <pyrogram.raw.base.Document>`
        part (optional): ``bool``
        rtl (optional): ``bool``
        v2 (optional): ``bool``
        views (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["url", "blocks", "photos", "documents", "part", "rtl", "v2", "views"]

    ID = 0x98657f0d
    QUALNAME = "types.Page"

    def __init__(self, *, url: str, blocks: List["raw.base.PageBlock"], photos: List["raw.base.Photo"],
                 documents: List["raw.base.Document"], part: Union[None, bool] = None, rtl: Union[None, bool] = None,
                 v2: Union[None, bool] = None, views: Union[None, int] = None) -> None:
        self.url = url  # string
        self.blocks = blocks  # Vector<PageBlock>
        self.photos = photos  # Vector<Photo>
        self.documents = documents  # Vector<Document>
        self.part = part  # flags.0?true
        self.rtl = rtl  # flags.1?true
        self.v2 = v2  # flags.2?true
        self.views = views  # flags.3?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Page":
        flags = Int.read(data)

        part = True if flags & (1 << 0) else False
        rtl = True if flags & (1 << 1) else False
        v2 = True if flags & (1 << 2) else False
        url = String.read(data)

        blocks = TLObject.read(data)

        photos = TLObject.read(data)

        documents = TLObject.read(data)

        views = Int.read(data) if flags & (1 << 3) else None
        return Page(url=url, blocks=blocks, photos=photos, documents=documents, part=part, rtl=rtl, v2=v2, views=views)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.part is not None else 0
        flags |= (1 << 1) if self.rtl is not None else 0
        flags |= (1 << 2) if self.v2 is not None else 0
        flags |= (1 << 3) if self.views is not None else 0
        data.write(Int(flags))

        data.write(String(self.url))

        data.write(Vector(self.blocks))

        data.write(Vector(self.photos))

        data.write(Vector(self.documents))

        if self.views is not None:
            data.write(Int(self.views))

        return data.getvalue()
