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


class CreateChannel(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0x3d5fb10f``

    Parameters:
        title: ``str``
        about: ``str``
        broadcast (optional): ``bool``
        megagroup (optional): ``bool``
        geo_point (optional): :obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`
        address (optional): ``str``

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["title", "about", "broadcast", "megagroup", "geo_point", "address"]

    ID = 0x3d5fb10f
    QUALNAME = "functions.channels.CreateChannel"

    def __init__(self, *, title: str, about: str, broadcast: Union[None, bool] = None,
                 megagroup: Union[None, bool] = None, geo_point: "raw.base.InputGeoPoint" = None,
                 address: Union[None, str] = None) -> None:
        self.title = title  # string
        self.about = about  # string
        self.broadcast = broadcast  # flags.0?true
        self.megagroup = megagroup  # flags.1?true
        self.geo_point = geo_point  # flags.2?InputGeoPoint
        self.address = address  # flags.2?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "CreateChannel":
        flags = Int.read(data)

        broadcast = True if flags & (1 << 0) else False
        megagroup = True if flags & (1 << 1) else False
        title = String.read(data)

        about = String.read(data)

        geo_point = TLObject.read(data) if flags & (1 << 2) else None

        address = String.read(data) if flags & (1 << 2) else None
        return CreateChannel(title=title, about=about, broadcast=broadcast, megagroup=megagroup, geo_point=geo_point,
                             address=address)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.broadcast is not None else 0
        flags |= (1 << 1) if self.megagroup is not None else 0
        flags |= (1 << 2) if self.geo_point is not None else 0
        flags |= (1 << 2) if self.address is not None else 0
        data.write(Int(flags))

        data.write(String(self.title))

        data.write(String(self.about))

        if self.geo_point is not None:
            data.write(self.geo_point.write())

        if self.address is not None:
            data.write(String(self.address))

        return data.getvalue()
