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


class InputMediaVenue(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``120``
        - ID: ``0xc13d1c11``

    Parameters:
        geo_point: :obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`
        title: ``str``
        address: ``str``
        provider: ``str``
        venue_id: ``str``
        venue_type: ``str``
    """

    __slots__: List[str] = ["geo_point", "title", "address", "provider", "venue_id", "venue_type"]

    ID = 0xc13d1c11
    QUALNAME = "types.InputMediaVenue"

    def __init__(self, *, geo_point: "raw.base.InputGeoPoint", title: str, address: str, provider: str, venue_id: str,
                 venue_type: str) -> None:
        self.geo_point = geo_point  # InputGeoPoint
        self.title = title  # string
        self.address = address  # string
        self.provider = provider  # string
        self.venue_id = venue_id  # string
        self.venue_type = venue_type  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputMediaVenue":
        # No flags

        geo_point = TLObject.read(data)

        title = String.read(data)

        address = String.read(data)

        provider = String.read(data)

        venue_id = String.read(data)

        venue_type = String.read(data)

        return InputMediaVenue(geo_point=geo_point, title=title, address=address, provider=provider, venue_id=venue_id,
                               venue_type=venue_type)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.geo_point.write())

        data.write(String(self.title))

        data.write(String(self.address))

        data.write(String(self.provider))

        data.write(String(self.venue_id))

        data.write(String(self.venue_type))

        return data.getvalue()
