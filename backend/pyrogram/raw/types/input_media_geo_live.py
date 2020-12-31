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
        - Layer: ``122``
        - ID: ``0x971fa843``

    Parameters:
        geo_point: :obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`
        stopped (optional): ``bool``
        heading (optional): ``int`` ``32-bit``
        period (optional): ``int`` ``32-bit``
        proximity_notification_radius (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["geo_point", "stopped", "heading", "period", "proximity_notification_radius"]

    ID = 0x971fa843
    QUALNAME = "types.InputMediaGeoLive"

    def __init__(self, *, geo_point: "raw.base.InputGeoPoint", stopped: Union[None, bool] = None,
                 heading: Union[None, int] = None, period: Union[None, int] = None,
                 proximity_notification_radius: Union[None, int] = None) -> None:
        self.geo_point = geo_point  # InputGeoPoint
        self.stopped = stopped  # flags.0?true
        self.heading = heading  # flags.2?int
        self.period = period  # flags.1?int
        self.proximity_notification_radius = proximity_notification_radius  # flags.3?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputMediaGeoLive":
        flags = Int.read(data)

        stopped = True if flags & (1 << 0) else False
        geo_point = TLObject.read(data)

        heading = Int.read(data) if flags & (1 << 2) else None
        period = Int.read(data) if flags & (1 << 1) else None
        proximity_notification_radius = Int.read(data) if flags & (1 << 3) else None
        return InputMediaGeoLive(geo_point=geo_point, stopped=stopped, heading=heading, period=period,
                                 proximity_notification_radius=proximity_notification_radius)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.stopped else 0
        flags |= (1 << 2) if self.heading is not None else 0
        flags |= (1 << 1) if self.period is not None else 0
        flags |= (1 << 3) if self.proximity_notification_radius is not None else 0
        data.write(Int(flags))

        data.write(self.geo_point.write())

        if self.heading is not None:
            data.write(Int(self.heading))

        if self.period is not None:
            data.write(Int(self.period))

        if self.proximity_notification_radius is not None:
            data.write(Int(self.proximity_notification_radius))

        return data.getvalue()
