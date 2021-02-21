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


class PageBlockPhoto(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``123``
        - ID: ``0x1759c560``

    Parameters:
        photo_id: ``int`` ``64-bit``
        caption: :obj:`PageCaption <pyrogram.raw.base.PageCaption>`
        url (optional): ``str``
        webpage_id (optional): ``int`` ``64-bit``
    """

    __slots__: List[str] = ["photo_id", "caption", "url", "webpage_id"]

    ID = 0x1759c560
    QUALNAME = "types.PageBlockPhoto"

    def __init__(self, *, photo_id: int, caption: "raw.base.PageCaption", url: Union[None, str] = None,
                 webpage_id: Union[None, int] = None) -> None:
        self.photo_id = photo_id  # long
        self.caption = caption  # PageCaption
        self.url = url  # flags.0?string
        self.webpage_id = webpage_id  # flags.0?long

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PageBlockPhoto":
        flags = Int.read(data)

        photo_id = Long.read(data)

        caption = TLObject.read(data)

        url = String.read(data) if flags & (1 << 0) else None
        webpage_id = Long.read(data) if flags & (1 << 0) else None
        return PageBlockPhoto(photo_id=photo_id, caption=caption, url=url, webpage_id=webpage_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.url is not None else 0
        flags |= (1 << 0) if self.webpage_id is not None else 0
        data.write(Int(flags))

        data.write(Long(self.photo_id))

        data.write(self.caption.write())

        if self.url is not None:
            data.write(String(self.url))

        if self.webpage_id is not None:
            data.write(Long(self.webpage_id))

        return data.getvalue()
