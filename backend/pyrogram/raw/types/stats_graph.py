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


class StatsGraph(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.StatsGraph`.

    Details:
        - Layer: ``123``
        - ID: ``0x8ea464b6``

    Parameters:
        json: :obj:`DataJSON <pyrogram.raw.base.DataJSON>`
        zoom_token (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`stats.LoadAsyncGraph <pyrogram.raw.functions.stats.LoadAsyncGraph>`
    """

    __slots__: List[str] = ["json", "zoom_token"]

    ID = 0x8ea464b6
    QUALNAME = "types.StatsGraph"

    def __init__(self, *, json: "raw.base.DataJSON", zoom_token: Union[None, str] = None) -> None:
        self.json = json  # DataJSON
        self.zoom_token = zoom_token  # flags.0?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StatsGraph":
        flags = Int.read(data)

        json = TLObject.read(data)

        zoom_token = String.read(data) if flags & (1 << 0) else None
        return StatsGraph(json=json, zoom_token=zoom_token)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.zoom_token is not None else 0
        data.write(Int(flags))

        data.write(self.json.write())

        if self.zoom_token is not None:
            data.write(String(self.zoom_token))

        return data.getvalue()
