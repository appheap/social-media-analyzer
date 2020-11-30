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


class UpdateMessagePoll(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``117``
        - ID: ``0xaca1657b``

    Parameters:
        poll_id: ``int`` ``64-bit``
        results: :obj:`PollResults <pyrogram.raw.base.PollResults>`
        poll (optional): :obj:`Poll <pyrogram.raw.base.Poll>`
    """

    __slots__: List[str] = ["poll_id", "results", "poll"]

    ID = 0xaca1657b
    QUALNAME = "types.UpdateMessagePoll"

    def __init__(self, *, poll_id: int, results: "raw.base.PollResults", poll: "raw.base.Poll" = None) -> None:
        self.poll_id = poll_id  # long
        self.results = results  # PollResults
        self.poll = poll  # flags.0?Poll

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateMessagePoll":
        flags = Int.read(data)

        poll_id = Long.read(data)

        poll = TLObject.read(data) if flags & (1 << 0) else None

        results = TLObject.read(data)

        return UpdateMessagePoll(poll_id=poll_id, results=results, poll=poll)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.poll is not None else 0
        data.write(Int(flags))

        data.write(Long(self.poll_id))

        if self.poll is not None:
            data.write(self.poll.write())

        data.write(self.results.write())

        return data.getvalue()
