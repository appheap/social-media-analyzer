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


class WallPaperNoFile(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.WallPaper`.

    Details:
        - Layer: ``122``
        - ID: ``0x8af40b25``

    Parameters:
        default (optional): ``bool``
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

    __slots__: List[str] = ["default", "dark", "settings"]

    ID = 0x8af40b25
    QUALNAME = "types.WallPaperNoFile"

    def __init__(self, *, default: Union[None, bool] = None, dark: Union[None, bool] = None,
                 settings: "raw.base.WallPaperSettings" = None) -> None:
        self.default = default  # flags.1?true
        self.dark = dark  # flags.4?true
        self.settings = settings  # flags.2?WallPaperSettings

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "WallPaperNoFile":
        flags = Int.read(data)

        default = True if flags & (1 << 1) else False
        dark = True if flags & (1 << 4) else False
        settings = TLObject.read(data) if flags & (1 << 2) else None

        return WallPaperNoFile(default=default, dark=dark, settings=settings)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.default else 0
        flags |= (1 << 4) if self.dark else 0
        flags |= (1 << 2) if self.settings is not None else 0
        data.write(Int(flags))

        if self.settings is not None:
            data.write(self.settings.write())

        return data.getvalue()
