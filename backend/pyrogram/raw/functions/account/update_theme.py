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


class UpdateTheme(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x5cb367d5``

    Parameters:
        format: ``str``
        theme: :obj:`InputTheme <pyrogram.raw.base.InputTheme>`
        slug (optional): ``str``
        title (optional): ``str``
        document (optional): :obj:`InputDocument <pyrogram.raw.base.InputDocument>`
        settings (optional): :obj:`InputThemeSettings <pyrogram.raw.base.InputThemeSettings>`

    Returns:
        :obj:`Theme <pyrogram.raw.base.Theme>`
    """

    __slots__: List[str] = ["format", "theme", "slug", "title", "document", "settings"]

    ID = 0x5cb367d5
    QUALNAME = "functions.account.UpdateTheme"

    def __init__(self, *, format: str, theme: "raw.base.InputTheme", slug: Union[None, str] = None,
                 title: Union[None, str] = None, document: "raw.base.InputDocument" = None,
                 settings: "raw.base.InputThemeSettings" = None) -> None:
        self.format = format  # string
        self.theme = theme  # InputTheme
        self.slug = slug  # flags.0?string
        self.title = title  # flags.1?string
        self.document = document  # flags.2?InputDocument
        self.settings = settings  # flags.3?InputThemeSettings

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateTheme":
        flags = Int.read(data)

        format = String.read(data)

        theme = TLObject.read(data)

        slug = String.read(data) if flags & (1 << 0) else None
        title = String.read(data) if flags & (1 << 1) else None
        document = TLObject.read(data) if flags & (1 << 2) else None

        settings = TLObject.read(data) if flags & (1 << 3) else None

        return UpdateTheme(format=format, theme=theme, slug=slug, title=title, document=document, settings=settings)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.slug is not None else 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 2) if self.document is not None else 0
        flags |= (1 << 3) if self.settings is not None else 0
        data.write(Int(flags))

        data.write(String(self.format))

        data.write(self.theme.write())

        if self.slug is not None:
            data.write(String(self.slug))

        if self.title is not None:
            data.write(String(self.title))

        if self.document is not None:
            data.write(self.document.write())

        if self.settings is not None:
            data.write(self.settings.write())

        return data.getvalue()
