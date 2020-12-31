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


class PageBlockRelatedArticles(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``122``
        - ID: ``0x16115a96``

    Parameters:
        title: :obj:`RichText <pyrogram.raw.base.RichText>`
        articles: List of :obj:`PageRelatedArticle <pyrogram.raw.base.PageRelatedArticle>`
    """

    __slots__: List[str] = ["title", "articles"]

    ID = 0x16115a96
    QUALNAME = "types.PageBlockRelatedArticles"

    def __init__(self, *, title: "raw.base.RichText", articles: List["raw.base.PageRelatedArticle"]) -> None:
        self.title = title  # RichText
        self.articles = articles  # Vector<PageRelatedArticle>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PageBlockRelatedArticles":
        # No flags

        title = TLObject.read(data)

        articles = TLObject.read(data)

        return PageBlockRelatedArticles(title=title, articles=articles)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.title.write())

        data.write(Vector(self.articles))

        return data.getvalue()
