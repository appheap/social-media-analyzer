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


class HighScore(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.HighScore`.

    Details:
        - Layer: ``123``
        - ID: ``0x58fffcd0``

    Parameters:
        pos: ``int`` ``32-bit``
        user_id: ``int`` ``32-bit``
        score: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["pos", "user_id", "score"]

    ID = 0x58fffcd0
    QUALNAME = "types.HighScore"

    def __init__(self, *, pos: int, user_id: int, score: int) -> None:
        self.pos = pos  # int
        self.user_id = user_id  # int
        self.score = score  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "HighScore":
        # No flags

        pos = Int.read(data)

        user_id = Int.read(data)

        score = Int.read(data)

        return HighScore(pos=pos, user_id=user_id, score=score)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.pos))

        data.write(Int(self.user_id))

        data.write(Int(self.score))

        return data.getvalue()
