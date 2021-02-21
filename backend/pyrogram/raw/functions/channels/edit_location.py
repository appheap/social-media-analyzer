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


class EditLocation(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x58e63f6d``

    Parameters:
        channel: :obj:`InputChannel <pyrogram.raw.base.InputChannel>`
        geo_point: :obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`
        address: ``str``

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "geo_point", "address"]

    ID = 0x58e63f6d
    QUALNAME = "functions.channels.EditLocation"

    def __init__(self, *, channel: "raw.base.InputChannel", geo_point: "raw.base.InputGeoPoint", address: str) -> None:
        self.channel = channel  # InputChannel
        self.geo_point = geo_point  # InputGeoPoint
        self.address = address  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "EditLocation":
        # No flags

        channel = TLObject.read(data)

        geo_point = TLObject.read(data)

        address = String.read(data)

        return EditLocation(channel=channel, geo_point=geo_point, address=address)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.channel.write())

        data.write(self.geo_point.write())

        data.write(String(self.address))

        return data.getvalue()
