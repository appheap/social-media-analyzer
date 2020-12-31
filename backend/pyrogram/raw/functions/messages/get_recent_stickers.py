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


class GetRecentStickers(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0x5ea192c9``

    Parameters:
        hash: ``int`` ``32-bit``
        attached (optional): ``bool``

    Returns:
        :obj:`messages.RecentStickers <pyrogram.raw.base.messages.RecentStickers>`
    """

    __slots__: List[str] = ["hash", "attached"]

    ID = 0x5ea192c9
    QUALNAME = "functions.messages.GetRecentStickers"

    def __init__(self, *, hash: int, attached: Union[None, bool] = None) -> None:
        self.hash = hash  # int
        self.attached = attached  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetRecentStickers":
        flags = Int.read(data)

        attached = True if flags & (1 << 0) else False
        hash = Int.read(data)

        return GetRecentStickers(hash=hash, attached=attached)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.attached else 0
        data.write(Int(flags))

        data.write(Int(self.hash))

        return data.getvalue()
