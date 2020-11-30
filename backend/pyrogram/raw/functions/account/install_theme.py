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


class InstallTheme(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0x7ae43737``

    Parameters:
        dark (optional): ``bool``
        format (optional): ``str``
        theme (optional): :obj:`InputTheme <pyrogram.raw.base.InputTheme>`

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["dark", "format", "theme"]

    ID = 0x7ae43737
    QUALNAME = "functions.account.InstallTheme"

    def __init__(self, *, dark: Union[None, bool] = None, format: Union[None, str] = None,
                 theme: "raw.base.InputTheme" = None) -> None:
        self.dark = dark  # flags.0?true
        self.format = format  # flags.1?string
        self.theme = theme  # flags.1?InputTheme

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InstallTheme":
        flags = Int.read(data)

        dark = True if flags & (1 << 0) else False
        format = String.read(data) if flags & (1 << 1) else None
        theme = TLObject.read(data) if flags & (1 << 1) else None

        return InstallTheme(dark=dark, format=format, theme=theme)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark is not None else 0
        flags |= (1 << 1) if self.format is not None else 0
        flags |= (1 << 1) if self.theme is not None else 0
        data.write(Int(flags))

        if self.format is not None:
            data.write(String(self.format))

        if self.theme is not None:
            data.write(self.theme.write())

        return data.getvalue()
