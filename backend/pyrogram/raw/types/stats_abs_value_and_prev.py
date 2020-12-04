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


class StatsAbsValueAndPrev(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.StatsAbsValueAndPrev`.

    Details:
        - Layer: ``120``
        - ID: ``0xcb43acde``

    Parameters:
        current: ``float`` ``64-bit``
        previous: ``float`` ``64-bit``
    """

    __slots__: List[str] = ["current", "previous"]

    ID = 0xcb43acde
    QUALNAME = "types.StatsAbsValueAndPrev"

    def __init__(self, *, current: float, previous: float) -> None:
        self.current = current  # double
        self.previous = previous  # double

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StatsAbsValueAndPrev":
        # No flags

        current = Double.read(data)

        previous = Double.read(data)

        return StatsAbsValueAndPrev(current=current, previous=previous)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Double(self.current))

        data.write(Double(self.previous))

        return data.getvalue()
