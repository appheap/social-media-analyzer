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


class DhConfig(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.DhConfig`.

    Details:
        - Layer: ``123``
        - ID: ``0x2c221edd``

    Parameters:
        g: ``int`` ``32-bit``
        p: ``bytes``
        version: ``int`` ``32-bit``
        random: ``bytes``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetDhConfig <pyrogram.raw.functions.messages.GetDhConfig>`
    """

    __slots__: List[str] = ["g", "p", "version", "random"]

    ID = 0x2c221edd
    QUALNAME = "types.messages.DhConfig"

    def __init__(self, *, g: int, p: bytes, version: int, random: bytes) -> None:
        self.g = g  # int
        self.p = p  # bytes
        self.version = version  # int
        self.random = random  # bytes

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "DhConfig":
        # No flags

        g = Int.read(data)

        p = Bytes.read(data)

        version = Int.read(data)

        random = Bytes.read(data)

        return DhConfig(g=g, p=p, version=version, random=random)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.g))

        data.write(Bytes(self.p))

        data.write(Int(self.version))

        data.write(Bytes(self.random))

        return data.getvalue()
