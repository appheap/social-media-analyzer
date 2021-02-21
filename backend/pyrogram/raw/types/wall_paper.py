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


class WallPaper(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.WallPaper`.

    Details:
        - Layer: ``123``
        - ID: ``0xa437c3ed``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        slug: ``str``
        document: :obj:`Document <pyrogram.raw.base.Document>`
        creator (optional): ``bool``
        default (optional): ``bool``
        pattern (optional): ``bool``
        dark (optional): ``bool``
        settings (optional): :obj:`WallPaperSettings <pyrogram.raw.base.WallPaperSettings>`

    See Also:
        This object can be returned by 3 methods:

        .. hlist::
            :columns: 2

            - :obj:`account.GetWallPaper <pyrogram.raw.functions.account.GetWallPaper>`
            - :obj:`account.UploadWallPaper <pyrogram.raw.functions.account.UploadWallPaper>`
            - :obj:`account.GetMultiWallPapers <pyrogram.raw.functions.account.GetMultiWallPapers>`
    """

    __slots__: List[str] = ["id", "access_hash", "slug", "document", "creator", "default", "pattern", "dark",
                            "settings"]

    ID = 0xa437c3ed
    QUALNAME = "types.WallPaper"

    def __init__(self, *, id: int, access_hash: int, slug: str, document: "raw.base.Document",
                 creator: Union[None, bool] = None, default: Union[None, bool] = None,
                 pattern: Union[None, bool] = None, dark: Union[None, bool] = None,
                 settings: "raw.base.WallPaperSettings" = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.slug = slug  # string
        self.document = document  # Document
        self.creator = creator  # flags.0?true
        self.default = default  # flags.1?true
        self.pattern = pattern  # flags.3?true
        self.dark = dark  # flags.4?true
        self.settings = settings  # flags.2?WallPaperSettings

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "WallPaper":
        id = Long.read(data)
        flags = Int.read(data)

        creator = True if flags & (1 << 0) else False
        default = True if flags & (1 << 1) else False
        pattern = True if flags & (1 << 3) else False
        dark = True if flags & (1 << 4) else False
        access_hash = Long.read(data)

        slug = String.read(data)

        document = TLObject.read(data)

        settings = TLObject.read(data) if flags & (1 << 2) else None

        return WallPaper(id=id, access_hash=access_hash, slug=slug, document=document, creator=creator, default=default,
                         pattern=pattern, dark=dark, settings=settings)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        data.write(Long(self.id))
        flags = 0
        flags |= (1 << 0) if self.creator else 0
        flags |= (1 << 1) if self.default else 0
        flags |= (1 << 3) if self.pattern else 0
        flags |= (1 << 4) if self.dark else 0
        flags |= (1 << 2) if self.settings is not None else 0
        data.write(Int(flags))

        data.write(Long(self.access_hash))

        data.write(String(self.slug))

        data.write(self.document.write())

        if self.settings is not None:
            data.write(self.settings.write())

        return data.getvalue()
