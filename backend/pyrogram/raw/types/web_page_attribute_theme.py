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


class WebPageAttributeTheme(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.WebPageAttribute`.

    Details:
        - Layer: ``122``
        - ID: ``0x54b56617``

    Parameters:
        documents (optional): List of :obj:`Document <pyrogram.raw.base.Document>`
        settings (optional): :obj:`ThemeSettings <pyrogram.raw.base.ThemeSettings>`
    """

    __slots__: List[str] = ["documents", "settings"]

    ID = 0x54b56617
    QUALNAME = "types.WebPageAttributeTheme"

    def __init__(self, *, documents: Union[None, List["raw.base.Document"]] = None,
                 settings: "raw.base.ThemeSettings" = None) -> None:
        self.documents = documents  # flags.0?Vector<Document>
        self.settings = settings  # flags.1?ThemeSettings

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "WebPageAttributeTheme":
        flags = Int.read(data)

        documents = TLObject.read(data) if flags & (1 << 0) else []

        settings = TLObject.read(data) if flags & (1 << 1) else None

        return WebPageAttributeTheme(documents=documents, settings=settings)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.documents is not None else 0
        flags |= (1 << 1) if self.settings is not None else 0
        data.write(Int(flags))

        if self.documents is not None:
            data.write(Vector(self.documents))

        if self.settings is not None:
            data.write(self.settings.write())

        return data.getvalue()
