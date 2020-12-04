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


class ForwardMessages(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0xd9fee60e``

    Parameters:
        from_peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        id: List of ``int`` ``32-bit``
        random_id: List of ``int`` ``64-bit``
        to_peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        silent (optional): ``bool``
        background (optional): ``bool``
        with_my_score (optional): ``bool``
        schedule_date (optional): ``int`` ``32-bit``

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["from_peer", "id", "random_id", "to_peer", "silent", "background", "with_my_score",
                            "schedule_date"]

    ID = 0xd9fee60e
    QUALNAME = "functions.messages.ForwardMessages"

    def __init__(self, *, from_peer: "raw.base.InputPeer", id: List[int], random_id: List[int],
                 to_peer: "raw.base.InputPeer", silent: Union[None, bool] = None, background: Union[None, bool] = None,
                 with_my_score: Union[None, bool] = None, schedule_date: Union[None, int] = None) -> None:
        self.from_peer = from_peer  # InputPeer
        self.id = id  # Vector<int>
        self.random_id = random_id  # Vector<long>
        self.to_peer = to_peer  # InputPeer
        self.silent = silent  # flags.5?true
        self.background = background  # flags.6?true
        self.with_my_score = with_my_score  # flags.8?true
        self.schedule_date = schedule_date  # flags.10?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ForwardMessages":
        flags = Int.read(data)

        silent = True if flags & (1 << 5) else False
        background = True if flags & (1 << 6) else False
        with_my_score = True if flags & (1 << 8) else False
        from_peer = TLObject.read(data)

        id = TLObject.read(data, Int)

        random_id = TLObject.read(data, Long)

        to_peer = TLObject.read(data)

        schedule_date = Int.read(data) if flags & (1 << 10) else None
        return ForwardMessages(from_peer=from_peer, id=id, random_id=random_id, to_peer=to_peer, silent=silent,
                               background=background, with_my_score=with_my_score, schedule_date=schedule_date)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent is not None else 0
        flags |= (1 << 6) if self.background is not None else 0
        flags |= (1 << 8) if self.with_my_score is not None else 0
        flags |= (1 << 10) if self.schedule_date is not None else 0
        data.write(Int(flags))

        data.write(self.from_peer.write())

        data.write(Vector(self.id, Int))

        data.write(Vector(self.random_id, Long))

        data.write(self.to_peer.write())

        if self.schedule_date is not None:
            data.write(Int(self.schedule_date))

        return data.getvalue()
