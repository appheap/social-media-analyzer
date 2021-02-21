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


class MessageMediaGeoLive(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``123``
        - ID: ``0xb940c666``

    Parameters:
        geo: :obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`
        period: ``int`` ``32-bit``
        heading (optional): ``int`` ``32-bit``
        proximity_notification_radius (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by 3 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetWebPagePreview <pyrogram.raw.functions.messages.GetWebPagePreview>`
            - :obj:`messages.UploadMedia <pyrogram.raw.functions.messages.UploadMedia>`
            - :obj:`messages.UploadImportedMedia <pyrogram.raw.functions.messages.UploadImportedMedia>`
    """

    __slots__: List[str] = ["geo", "period", "heading", "proximity_notification_radius"]

    ID = 0xb940c666
    QUALNAME = "types.MessageMediaGeoLive"

    def __init__(self, *, geo: "raw.base.GeoPoint", period: int, heading: Union[None, int] = None,
                 proximity_notification_radius: Union[None, int] = None) -> None:
        self.geo = geo  # GeoPoint
        self.period = period  # int
        self.heading = heading  # flags.0?int
        self.proximity_notification_radius = proximity_notification_radius  # flags.1?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MessageMediaGeoLive":
        flags = Int.read(data)

        geo = TLObject.read(data)

        heading = Int.read(data) if flags & (1 << 0) else None
        period = Int.read(data)

        proximity_notification_radius = Int.read(data) if flags & (1 << 1) else None
        return MessageMediaGeoLive(geo=geo, period=period, heading=heading,
                                   proximity_notification_radius=proximity_notification_radius)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.heading is not None else 0
        flags |= (1 << 1) if self.proximity_notification_radius is not None else 0
        data.write(Int(flags))

        data.write(self.geo.write())

        if self.heading is not None:
            data.write(Int(self.heading))

        data.write(Int(self.period))

        if self.proximity_notification_radius is not None:
            data.write(Int(self.proximity_notification_radius))

        return data.getvalue()
