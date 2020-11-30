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


class PageRelatedArticle(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PageRelatedArticle`.

    Details:
        - Layer: ``117``
        - ID: ``0xb390dc08``

    Parameters:
        url: ``str``
        webpage_id: ``int`` ``64-bit``
        title (optional): ``str``
        description (optional): ``str``
        photo_id (optional): ``int`` ``64-bit``
        author (optional): ``str``
        published_date (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["url", "webpage_id", "title", "description", "photo_id", "author", "published_date"]

    ID = 0xb390dc08
    QUALNAME = "types.PageRelatedArticle"

    def __init__(self, *, url: str, webpage_id: int, title: Union[None, str] = None,
                 description: Union[None, str] = None, photo_id: Union[None, int] = None,
                 author: Union[None, str] = None, published_date: Union[None, int] = None) -> None:
        self.url = url  # string
        self.webpage_id = webpage_id  # long
        self.title = title  # flags.0?string
        self.description = description  # flags.1?string
        self.photo_id = photo_id  # flags.2?long
        self.author = author  # flags.3?string
        self.published_date = published_date  # flags.4?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PageRelatedArticle":
        flags = Int.read(data)

        url = String.read(data)

        webpage_id = Long.read(data)

        title = String.read(data) if flags & (1 << 0) else None
        description = String.read(data) if flags & (1 << 1) else None
        photo_id = Long.read(data) if flags & (1 << 2) else None
        author = String.read(data) if flags & (1 << 3) else None
        published_date = Int.read(data) if flags & (1 << 4) else None
        return PageRelatedArticle(url=url, webpage_id=webpage_id, title=title, description=description,
                                  photo_id=photo_id, author=author, published_date=published_date)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.description is not None else 0
        flags |= (1 << 2) if self.photo_id is not None else 0
        flags |= (1 << 3) if self.author is not None else 0
        flags |= (1 << 4) if self.published_date is not None else 0
        data.write(Int(flags))

        data.write(String(self.url))

        data.write(Long(self.webpage_id))

        if self.title is not None:
            data.write(String(self.title))

        if self.description is not None:
            data.write(String(self.description))

        if self.photo_id is not None:
            data.write(Long(self.photo_id))

        if self.author is not None:
            data.write(String(self.author))

        if self.published_date is not None:
            data.write(Int(self.published_date))

        return data.getvalue()
