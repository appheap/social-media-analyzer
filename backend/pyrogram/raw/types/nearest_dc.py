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


class NearestDc(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.NearestDc`.

    Details:
        - Layer: ``117``
        - ID: ``0x8e1a1775``

    Parameters:
        country: ``str``
        this_dc: ``int`` ``32-bit``
        nearest_dc: ``int`` ``32-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`help.GetNearestDc <pyrogram.raw.functions.help.GetNearestDc>`
    """

    __slots__: List[str] = ["country", "this_dc", "nearest_dc"]

    ID = 0x8e1a1775
    QUALNAME = "types.NearestDc"

    def __init__(self, *, country: str, this_dc: int, nearest_dc: int) -> None:
        self.country = country  # string
        self.this_dc = this_dc  # int
        self.nearest_dc = nearest_dc  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "NearestDc":
        # No flags

        country = String.read(data)

        this_dc = Int.read(data)

        nearest_dc = Int.read(data)

        return NearestDc(country=country, this_dc=this_dc, nearest_dc=nearest_dc)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.country))

        data.write(Int(self.this_dc))

        data.write(Int(self.nearest_dc))

        return data.getvalue()
