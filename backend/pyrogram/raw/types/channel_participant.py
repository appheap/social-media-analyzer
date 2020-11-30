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


class ChannelParticipant(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChannelParticipant`.

    Details:
        - Layer: ``117``
        - ID: ``0x15ebac1d``

    Parameters:
        user_id: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["user_id", "date"]

    ID = 0x15ebac1d
    QUALNAME = "types.ChannelParticipant"

    def __init__(self, *, user_id: int, date: int) -> None:
        self.user_id = user_id  # int
        self.date = date  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChannelParticipant":
        # No flags

        user_id = Int.read(data)

        date = Int.read(data)

        return ChannelParticipant(user_id=user_id, date=date)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.user_id))

        data.write(Int(self.date))

        return data.getvalue()
