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


class UpdateChannelTooLong(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``122``
        - ID: ``0xeb0467fb``

    Parameters:
        channel_id: ``int`` ``32-bit``
        pts (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["channel_id", "pts"]

    ID = 0xeb0467fb
    QUALNAME = "types.UpdateChannelTooLong"

    def __init__(self, *, channel_id: int, pts: Union[None, int] = None) -> None:
        self.channel_id = channel_id  # int
        self.pts = pts  # flags.0?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateChannelTooLong":
        flags = Int.read(data)

        channel_id = Int.read(data)

        pts = Int.read(data) if flags & (1 << 0) else None
        return UpdateChannelTooLong(channel_id=channel_id, pts=pts)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pts is not None else 0
        data.write(Int(flags))

        data.write(Int(self.channel_id))

        if self.pts is not None:
            data.write(Int(self.pts))

        return data.getvalue()
