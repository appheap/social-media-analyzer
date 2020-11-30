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


class InputMediaGeoLive(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``117``
        - ID: ``0xce4e82fd``

    Parameters:
        geo_point: :obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`
        stopped (optional): ``bool``
        period (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["geo_point", "stopped", "period"]

    ID = 0xce4e82fd
    QUALNAME = "types.InputMediaGeoLive"

    def __init__(self, *, geo_point: "raw.base.InputGeoPoint", stopped: Union[None, bool] = None,
                 period: Union[None, int] = None) -> None:
        self.geo_point = geo_point  # InputGeoPoint
        self.stopped = stopped  # flags.0?true
        self.period = period  # flags.1?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputMediaGeoLive":
        flags = Int.read(data)

        stopped = True if flags & (1 << 0) else False
        geo_point = TLObject.read(data)

        period = Int.read(data) if flags & (1 << 1) else None
        return InputMediaGeoLive(geo_point=geo_point, stopped=stopped, period=period)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.stopped is not None else 0
        flags |= (1 << 1) if self.period is not None else 0
        data.write(Int(flags))

        data.write(self.geo_point.write())

        if self.period is not None:
            data.write(Int(self.period))

        return data.getvalue()
