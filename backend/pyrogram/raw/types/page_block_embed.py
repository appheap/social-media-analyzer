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


class PageBlockEmbed(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``122``
        - ID: ``0xa8718dc5``

    Parameters:
        caption: :obj:`PageCaption <pyrogram.raw.base.PageCaption>`
        full_width (optional): ``bool``
        allow_scrolling (optional): ``bool``
        url (optional): ``str``
        html (optional): ``str``
        poster_photo_id (optional): ``int`` ``64-bit``
        w (optional): ``int`` ``32-bit``
        h (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["caption", "full_width", "allow_scrolling", "url", "html", "poster_photo_id", "w", "h"]

    ID = 0xa8718dc5
    QUALNAME = "types.PageBlockEmbed"

    def __init__(self, *, caption: "raw.base.PageCaption", full_width: Union[None, bool] = None,
                 allow_scrolling: Union[None, bool] = None, url: Union[None, str] = None, html: Union[None, str] = None,
                 poster_photo_id: Union[None, int] = None, w: Union[None, int] = None,
                 h: Union[None, int] = None) -> None:
        self.caption = caption  # PageCaption
        self.full_width = full_width  # flags.0?true
        self.allow_scrolling = allow_scrolling  # flags.3?true
        self.url = url  # flags.1?string
        self.html = html  # flags.2?string
        self.poster_photo_id = poster_photo_id  # flags.4?long
        self.w = w  # flags.5?int
        self.h = h  # flags.5?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PageBlockEmbed":
        flags = Int.read(data)

        full_width = True if flags & (1 << 0) else False
        allow_scrolling = True if flags & (1 << 3) else False
        url = String.read(data) if flags & (1 << 1) else None
        html = String.read(data) if flags & (1 << 2) else None
        poster_photo_id = Long.read(data) if flags & (1 << 4) else None
        w = Int.read(data) if flags & (1 << 5) else None
        h = Int.read(data) if flags & (1 << 5) else None
        caption = TLObject.read(data)

        return PageBlockEmbed(caption=caption, full_width=full_width, allow_scrolling=allow_scrolling, url=url,
                              html=html, poster_photo_id=poster_photo_id, w=w, h=h)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.full_width else 0
        flags |= (1 << 3) if self.allow_scrolling else 0
        flags |= (1 << 1) if self.url is not None else 0
        flags |= (1 << 2) if self.html is not None else 0
        flags |= (1 << 4) if self.poster_photo_id is not None else 0
        flags |= (1 << 5) if self.w is not None else 0
        flags |= (1 << 5) if self.h is not None else 0
        data.write(Int(flags))

        if self.url is not None:
            data.write(String(self.url))

        if self.html is not None:
            data.write(String(self.html))

        if self.poster_photo_id is not None:
            data.write(Long(self.poster_photo_id))

        if self.w is not None:
            data.write(Int(self.w))

        if self.h is not None:
            data.write(Int(self.h))

        data.write(self.caption.write())

        return data.getvalue()
