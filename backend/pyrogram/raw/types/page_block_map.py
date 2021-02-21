#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
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


class PageBlockMap(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``123``
        - ID: ``0xa44f3ef6``

    Parameters:
        geo: :obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`
        zoom: ``int`` ``32-bit``
        w: ``int`` ``32-bit``
        h: ``int`` ``32-bit``
        caption: :obj:`PageCaption <pyrogram.raw.base.PageCaption>`
    """

    __slots__: List[str] = ["geo", "zoom", "w", "h", "caption"]

    ID = 0xa44f3ef6
    QUALNAME = "types.PageBlockMap"

    def __init__(self, *, geo: "raw.base.GeoPoint", zoom: int, w: int, h: int, caption: "raw.base.PageCaption") -> None:
        self.geo = geo  # GeoPoint
        self.zoom = zoom  # int
        self.w = w  # int
        self.h = h  # int
        self.caption = caption  # PageCaption

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PageBlockMap":
        # No flags

        geo = TLObject.read(data)

        zoom = Int.read(data)

        w = Int.read(data)

        h = Int.read(data)

        caption = TLObject.read(data)

        return PageBlockMap(geo=geo, zoom=zoom, w=w, h=h, caption=caption)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.geo.write())

        data.write(Int(self.zoom))

        data.write(Int(self.w))

        data.write(Int(self.h))

        data.write(self.caption.write())

        return data.getvalue()
