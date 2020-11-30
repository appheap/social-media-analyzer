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


class Theme(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Theme`.

    Details:
        - Layer: ``117``
        - ID: ``0x28f1114``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        slug: ``str``
        title: ``str``
        installs_count: ``int`` ``32-bit``
        creator (optional): ``bool``
        default (optional): ``bool``
        document (optional): :obj:`Document <pyrogram.raw.base.Document>`
        settings (optional): :obj:`ThemeSettings <pyrogram.raw.base.ThemeSettings>`

    See Also:
        This object can be returned by 3 methods:

        .. hlist::
            :columns: 2

            - :obj:`account.CreateTheme <pyrogram.raw.functions.account.CreateTheme>`
            - :obj:`account.UpdateTheme <pyrogram.raw.functions.account.UpdateTheme>`
            - :obj:`account.GetTheme <pyrogram.raw.functions.account.GetTheme>`
    """

    __slots__: List[str] = ["id", "access_hash", "slug", "title", "installs_count", "creator", "default", "document",
                            "settings"]

    ID = 0x28f1114
    QUALNAME = "types.Theme"

    def __init__(self, *, id: int, access_hash: int, slug: str, title: str, installs_count: int,
                 creator: Union[None, bool] = None, default: Union[None, bool] = None,
                 document: "raw.base.Document" = None, settings: "raw.base.ThemeSettings" = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.slug = slug  # string
        self.title = title  # string
        self.installs_count = installs_count  # int
        self.creator = creator  # flags.0?true
        self.default = default  # flags.1?true
        self.document = document  # flags.2?Document
        self.settings = settings  # flags.3?ThemeSettings

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Theme":
        flags = Int.read(data)

        creator = True if flags & (1 << 0) else False
        default = True if flags & (1 << 1) else False
        id = Long.read(data)

        access_hash = Long.read(data)

        slug = String.read(data)

        title = String.read(data)

        document = TLObject.read(data) if flags & (1 << 2) else None

        settings = TLObject.read(data) if flags & (1 << 3) else None

        installs_count = Int.read(data)

        return Theme(id=id, access_hash=access_hash, slug=slug, title=title, installs_count=installs_count,
                     creator=creator, default=default, document=document, settings=settings)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator is not None else 0
        flags |= (1 << 1) if self.default is not None else 0
        flags |= (1 << 2) if self.document is not None else 0
        flags |= (1 << 3) if self.settings is not None else 0
        data.write(Int(flags))

        data.write(Long(self.id))

        data.write(Long(self.access_hash))

        data.write(String(self.slug))

        data.write(String(self.title))

        if self.document is not None:
            data.write(self.document.write())

        if self.settings is not None:
            data.write(self.settings.write())

        data.write(Int(self.installs_count))

        return data.getvalue()
