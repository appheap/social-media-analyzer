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


class InputMediaPoll(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``120``
        - ID: ``0xf94e5f1``

    Parameters:
        poll: :obj:`Poll <pyrogram.raw.base.Poll>`
        correct_answers (optional): List of ``bytes``
        solution (optional): ``str``
        solution_entities (optional): List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`
    """

    __slots__: List[str] = ["poll", "correct_answers", "solution", "solution_entities"]

    ID = 0xf94e5f1
    QUALNAME = "types.InputMediaPoll"

    def __init__(self, *, poll: "raw.base.Poll", correct_answers: Union[None, List[bytes]] = None,
                 solution: Union[None, str] = None,
                 solution_entities: Union[None, List["raw.base.MessageEntity"]] = None) -> None:
        self.poll = poll  # Poll
        self.correct_answers = correct_answers  # flags.0?Vector<bytes>
        self.solution = solution  # flags.1?string
        self.solution_entities = solution_entities  # flags.1?Vector<MessageEntity>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputMediaPoll":
        flags = Int.read(data)

        poll = TLObject.read(data)

        correct_answers = TLObject.read(data, Bytes) if flags & (1 << 0) else []

        solution = String.read(data) if flags & (1 << 1) else None
        solution_entities = TLObject.read(data) if flags & (1 << 1) else []

        return InputMediaPoll(poll=poll, correct_answers=correct_answers, solution=solution,
                              solution_entities=solution_entities)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.correct_answers is not None else 0
        flags |= (1 << 1) if self.solution is not None else 0
        flags |= (1 << 1) if self.solution_entities is not None else 0
        data.write(Int(flags))

        data.write(self.poll.write())

        if self.correct_answers is not None:
            data.write(Vector(self.correct_answers, Bytes))

        if self.solution is not None:
            data.write(String(self.solution))

        if self.solution_entities is not None:
            data.write(Vector(self.solution_entities))

        return data.getvalue()
