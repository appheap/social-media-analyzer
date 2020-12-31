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


class HttpWait(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.HttpWait`.

    Details:
        - Layer: ``122``
        - ID: ``0x9299359f``

    Parameters:
        max_delay: ``int`` ``32-bit``
        wait_after: ``int`` ``32-bit``
        max_wait: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["max_delay", "wait_after", "max_wait"]

    ID = 0x9299359f
    QUALNAME = "types.HttpWait"

    def __init__(self, *, max_delay: int, wait_after: int, max_wait: int) -> None:
        self.max_delay = max_delay  # int
        self.wait_after = wait_after  # int
        self.max_wait = max_wait  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "HttpWait":
        # No flags

        max_delay = Int.read(data)

        wait_after = Int.read(data)

        max_wait = Int.read(data)

        return HttpWait(max_delay=max_delay, wait_after=wait_after, max_wait=max_wait)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.max_delay))

        data.write(Int(self.wait_after))

        data.write(Int(self.max_wait))

        return data.getvalue()
