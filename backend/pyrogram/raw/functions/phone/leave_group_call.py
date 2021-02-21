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


class LeaveGroupCall(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x500377f9``

    Parameters:
        call: :obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`
        source: ``int`` ``32-bit``

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "source"]

    ID = 0x500377f9
    QUALNAME = "functions.phone.LeaveGroupCall"

    def __init__(self, *, call: "raw.base.InputGroupCall", source: int) -> None:
        self.call = call  # InputGroupCall
        self.source = source  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "LeaveGroupCall":
        # No flags

        call = TLObject.read(data)

        source = Int.read(data)

        return LeaveGroupCall(call=call, source=source)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.call.write())

        data.write(Int(self.source))

        return data.getvalue()
