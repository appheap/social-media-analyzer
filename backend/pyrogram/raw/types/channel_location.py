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


class ChannelLocation(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChannelLocation`.

    Details:
        - Layer: ``117``
        - ID: ``0x209b82db``

    Parameters:
        geo_point: :obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`
        address: ``str``
    """

    __slots__: List[str] = ["geo_point", "address"]

    ID = 0x209b82db
    QUALNAME = "types.ChannelLocation"

    def __init__(self, *, geo_point: "raw.base.GeoPoint", address: str) -> None:
        self.geo_point = geo_point  # GeoPoint
        self.address = address  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChannelLocation":
        # No flags

        geo_point = TLObject.read(data)

        address = String.read(data)

        return ChannelLocation(geo_point=geo_point, address=address)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.geo_point.write())

        data.write(String(self.address))

        return data.getvalue()
