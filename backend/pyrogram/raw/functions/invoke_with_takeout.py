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


class InvokeWithTakeout(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0xaca9fd2e``

    Parameters:
        takeout_id: ``int`` ``64-bit``
        query: Any method from :obj:`~pyrogram.raw.functions`

    Returns:
        Any object from :obj:`~pyrogram.raw.types`
    """

    __slots__: List[str] = ["takeout_id", "query"]

    ID = 0xaca9fd2e
    QUALNAME = "functions.InvokeWithTakeout"

    def __init__(self, *, takeout_id: int, query: TLObject) -> None:
        self.takeout_id = takeout_id  # long
        self.query = query  # !X

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InvokeWithTakeout":
        # No flags

        takeout_id = Long.read(data)

        query = TLObject.read(data)

        return InvokeWithTakeout(takeout_id=takeout_id, query=query)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Long(self.takeout_id))

        data.write(self.query.write())

        return data.getvalue()
