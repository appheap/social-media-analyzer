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


class InputBotInlineMessageID(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputBotInlineMessageID`.

    Details:
        - Layer: ``123``
        - ID: ``0x890c3d89``

    Parameters:
        dc_id: ``int`` ``32-bit``
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
    """

    __slots__: List[str] = ["dc_id", "id", "access_hash"]

    ID = 0x890c3d89
    QUALNAME = "types.InputBotInlineMessageID"

    def __init__(self, *, dc_id: int, id: int, access_hash: int) -> None:
        self.dc_id = dc_id  # int
        self.id = id  # long
        self.access_hash = access_hash  # long

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputBotInlineMessageID":
        # No flags

        dc_id = Int.read(data)

        id = Long.read(data)

        access_hash = Long.read(data)

        return InputBotInlineMessageID(dc_id=dc_id, id=id, access_hash=access_hash)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.dc_id))

        data.write(Long(self.id))

        data.write(Long(self.access_hash))

        return data.getvalue()
