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


class PollAnswerVoters(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PollAnswerVoters`.

    Details:
        - Layer: ``120``
        - ID: ``0x3b6ddad2``

    Parameters:
        option: ``bytes``
        voters: ``int`` ``32-bit``
        chosen (optional): ``bool``
        correct (optional): ``bool``
    """

    __slots__: List[str] = ["option", "voters", "chosen", "correct"]

    ID = 0x3b6ddad2
    QUALNAME = "types.PollAnswerVoters"

    def __init__(self, *, option: bytes, voters: int, chosen: Union[None, bool] = None,
                 correct: Union[None, bool] = None) -> None:
        self.option = option  # bytes
        self.voters = voters  # int
        self.chosen = chosen  # flags.0?true
        self.correct = correct  # flags.1?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PollAnswerVoters":
        flags = Int.read(data)

        chosen = True if flags & (1 << 0) else False
        correct = True if flags & (1 << 1) else False
        option = Bytes.read(data)

        voters = Int.read(data)

        return PollAnswerVoters(option=option, voters=voters, chosen=chosen, correct=correct)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.chosen is not None else 0
        flags |= (1 << 1) if self.correct is not None else 0
        data.write(Int(flags))

        data.write(Bytes(self.option))

        data.write(Int(self.voters))

        return data.getvalue()
