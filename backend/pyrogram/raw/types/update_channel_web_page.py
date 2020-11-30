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


class UpdateChannelWebPage(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``117``
        - ID: ``0x40771900``

    Parameters:
        channel_id: ``int`` ``32-bit``
        webpage: :obj:`WebPage <pyrogram.raw.base.WebPage>`
        pts: ``int`` ``32-bit``
        pts_count: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["channel_id", "webpage", "pts", "pts_count"]

    ID = 0x40771900
    QUALNAME = "types.UpdateChannelWebPage"

    def __init__(self, *, channel_id: int, webpage: "raw.base.WebPage", pts: int, pts_count: int) -> None:
        self.channel_id = channel_id  # int
        self.webpage = webpage  # WebPage
        self.pts = pts  # int
        self.pts_count = pts_count  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateChannelWebPage":
        # No flags

        channel_id = Int.read(data)

        webpage = TLObject.read(data)

        pts = Int.read(data)

        pts_count = Int.read(data)

        return UpdateChannelWebPage(channel_id=channel_id, webpage=webpage, pts=pts, pts_count=pts_count)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.channel_id))

        data.write(self.webpage.write())

        data.write(Int(self.pts))

        data.write(Int(self.pts_count))

        return data.getvalue()
