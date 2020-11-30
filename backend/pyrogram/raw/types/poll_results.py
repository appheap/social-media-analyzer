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


class PollResults(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PollResults`.

    Details:
        - Layer: ``117``
        - ID: ``0xbadcc1a3``

    Parameters:
        min (optional): ``bool``
        results (optional): List of :obj:`PollAnswerVoters <pyrogram.raw.base.PollAnswerVoters>`
        total_voters (optional): ``int`` ``32-bit``
        recent_voters (optional): List of ``int`` ``32-bit``
        solution (optional): ``str``
        solution_entities (optional): List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`
    """

    __slots__: List[str] = ["min", "results", "total_voters", "recent_voters", "solution", "solution_entities"]

    ID = 0xbadcc1a3
    QUALNAME = "types.PollResults"

    def __init__(self, *, min: Union[None, bool] = None, results: Union[None, List["raw.base.PollAnswerVoters"]] = None,
                 total_voters: Union[None, int] = None, recent_voters: Union[None, List[int]] = None,
                 solution: Union[None, str] = None,
                 solution_entities: Union[None, List["raw.base.MessageEntity"]] = None) -> None:
        self.min = min  # flags.0?true
        self.results = results  # flags.1?Vector<PollAnswerVoters>
        self.total_voters = total_voters  # flags.2?int
        self.recent_voters = recent_voters  # flags.3?Vector<int>
        self.solution = solution  # flags.4?string
        self.solution_entities = solution_entities  # flags.4?Vector<MessageEntity>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PollResults":
        flags = Int.read(data)

        min = True if flags & (1 << 0) else False
        results = TLObject.read(data) if flags & (1 << 1) else []

        total_voters = Int.read(data) if flags & (1 << 2) else None
        recent_voters = TLObject.read(data, Int) if flags & (1 << 3) else []

        solution = String.read(data) if flags & (1 << 4) else None
        solution_entities = TLObject.read(data) if flags & (1 << 4) else []

        return PollResults(min=min, results=results, total_voters=total_voters, recent_voters=recent_voters,
                           solution=solution, solution_entities=solution_entities)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.min is not None else 0
        flags |= (1 << 1) if self.results is not None else 0
        flags |= (1 << 2) if self.total_voters is not None else 0
        flags |= (1 << 3) if self.recent_voters is not None else 0
        flags |= (1 << 4) if self.solution is not None else 0
        flags |= (1 << 4) if self.solution_entities is not None else 0
        data.write(Int(flags))

        if self.results is not None:
            data.write(Vector(self.results))

        if self.total_voters is not None:
            data.write(Int(self.total_voters))

        if self.recent_voters is not None:
            data.write(Vector(self.recent_voters, Int))

        if self.solution is not None:
            data.write(String(self.solution))

        if self.solution_entities is not None:
            data.write(Vector(self.solution_entities))

        return data.getvalue()
