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


class LoadAsyncGraph(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0x621d5fa0``

    Parameters:
        token: ``str``
        x (optional): ``int`` ``64-bit``

    Returns:
        :obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`
    """

    __slots__: List[str] = ["token", "x"]

    ID = 0x621d5fa0
    QUALNAME = "functions.stats.LoadAsyncGraph"

    def __init__(self, *, token: str, x: Union[None, int] = None) -> None:
        self.token = token  # string
        self.x = x  # flags.0?long

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "LoadAsyncGraph":
        flags = Int.read(data)

        token = String.read(data)

        x = Long.read(data) if flags & (1 << 0) else None
        return LoadAsyncGraph(token=token, x=x)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.x is not None else 0
        data.write(Int(flags))

        data.write(String(self.token))

        if self.x is not None:
            data.write(Long(self.x))

        return data.getvalue()
