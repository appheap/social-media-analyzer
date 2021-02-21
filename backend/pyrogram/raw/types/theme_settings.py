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


class ThemeSettings(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ThemeSettings`.

    Details:
        - Layer: ``123``
        - ID: ``0x9c14984a``

    Parameters:
        base_theme: :obj:`BaseTheme <pyrogram.raw.base.BaseTheme>`
        accent_color: ``int`` ``32-bit``
        message_top_color (optional): ``int`` ``32-bit``
        message_bottom_color (optional): ``int`` ``32-bit``
        wallpaper (optional): :obj:`WallPaper <pyrogram.raw.base.WallPaper>`
    """

    __slots__: List[str] = ["base_theme", "accent_color", "message_top_color", "message_bottom_color", "wallpaper"]

    ID = 0x9c14984a
    QUALNAME = "types.ThemeSettings"

    def __init__(self, *, base_theme: "raw.base.BaseTheme", accent_color: int,
                 message_top_color: Union[None, int] = None, message_bottom_color: Union[None, int] = None,
                 wallpaper: "raw.base.WallPaper" = None) -> None:
        self.base_theme = base_theme  # BaseTheme
        self.accent_color = accent_color  # int
        self.message_top_color = message_top_color  # flags.0?int
        self.message_bottom_color = message_bottom_color  # flags.0?int
        self.wallpaper = wallpaper  # flags.1?WallPaper

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ThemeSettings":
        flags = Int.read(data)

        base_theme = TLObject.read(data)

        accent_color = Int.read(data)

        message_top_color = Int.read(data) if flags & (1 << 0) else None
        message_bottom_color = Int.read(data) if flags & (1 << 0) else None
        wallpaper = TLObject.read(data) if flags & (1 << 1) else None

        return ThemeSettings(base_theme=base_theme, accent_color=accent_color, message_top_color=message_top_color,
                             message_bottom_color=message_bottom_color, wallpaper=wallpaper)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.message_top_color is not None else 0
        flags |= (1 << 0) if self.message_bottom_color is not None else 0
        flags |= (1 << 1) if self.wallpaper is not None else 0
        data.write(Int(flags))

        data.write(self.base_theme.write())

        data.write(Int(self.accent_color))

        if self.message_top_color is not None:
            data.write(Int(self.message_top_color))

        if self.message_bottom_color is not None:
            data.write(Int(self.message_bottom_color))

        if self.wallpaper is not None:
            data.write(self.wallpaper.write())

        return data.getvalue()
