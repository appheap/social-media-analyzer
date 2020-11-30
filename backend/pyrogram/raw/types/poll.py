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


class Poll(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Poll`.

    Details:
        - Layer: ``117``
        - ID: ``0x86e18161``

    Parameters:
        id: ``int`` ``64-bit``
        question: ``str``
        answers: List of :obj:`PollAnswer <pyrogram.raw.base.PollAnswer>`
        closed (optional): ``bool``
        public_voters (optional): ``bool``
        multiple_choice (optional): ``bool``
        quiz (optional): ``bool``
        close_period (optional): ``int`` ``32-bit``
        close_date (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["id", "question", "answers", "closed", "public_voters", "multiple_choice", "quiz",
                            "close_period", "close_date"]

    ID = 0x86e18161
    QUALNAME = "types.Poll"

    def __init__(self, *, id: int, question: str, answers: List["raw.base.PollAnswer"],
                 closed: Union[None, bool] = None, public_voters: Union[None, bool] = None,
                 multiple_choice: Union[None, bool] = None, quiz: Union[None, bool] = None,
                 close_period: Union[None, int] = None, close_date: Union[None, int] = None) -> None:
        self.id = id  # long
        self.question = question  # string
        self.answers = answers  # Vector<PollAnswer>
        self.closed = closed  # flags.0?true
        self.public_voters = public_voters  # flags.1?true
        self.multiple_choice = multiple_choice  # flags.2?true
        self.quiz = quiz  # flags.3?true
        self.close_period = close_period  # flags.4?int
        self.close_date = close_date  # flags.5?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Poll":

        id = Long.read(data)
        flags = Int.read(data)

        closed = True if flags & (1 << 0) else False
        public_voters = True if flags & (1 << 1) else False
        multiple_choice = True if flags & (1 << 2) else False
        quiz = True if flags & (1 << 3) else False
        question = String.read(data)

        answers = TLObject.read(data)

        close_period = Int.read(data) if flags & (1 << 4) else None
        close_date = Int.read(data) if flags & (1 << 5) else None
        return Poll(id=id, question=question, answers=answers, closed=closed, public_voters=public_voters,
                    multiple_choice=multiple_choice, quiz=quiz, close_period=close_period, close_date=close_date)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        data.write(Long(self.id))
        flags = 0
        flags |= (1 << 0) if self.closed is not None else 0
        flags |= (1 << 1) if self.public_voters is not None else 0
        flags |= (1 << 2) if self.multiple_choice is not None else 0
        flags |= (1 << 3) if self.quiz is not None else 0
        flags |= (1 << 4) if self.close_period is not None else 0
        flags |= (1 << 5) if self.close_date is not None else 0
        data.write(Int(flags))

        data.write(String(self.question))

        data.write(Vector(self.answers))

        if self.close_period is not None:
            data.write(Int(self.close_period))

        if self.close_date is not None:
            data.write(Int(self.close_date))

        return data.getvalue()
