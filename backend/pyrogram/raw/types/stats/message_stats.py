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


class MessageStats(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.stats.MessageStats`.

    Details:
        - Layer: ``123``
        - ID: ``0x8999f295``

    Parameters:
        views_graph: :obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`stats.GetMessageStats <pyrogram.raw.functions.stats.GetMessageStats>`
    """

    __slots__: List[str] = ["views_graph"]

    ID = 0x8999f295
    QUALNAME = "types.stats.MessageStats"

    def __init__(self, *, views_graph: "raw.base.StatsGraph") -> None:
        self.views_graph = views_graph  # StatsGraph

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MessageStats":
        # No flags

        views_graph = TLObject.read(data)

        return MessageStats(views_graph=views_graph)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.views_graph.write())

        return data.getvalue()
