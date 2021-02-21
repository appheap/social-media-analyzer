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


class PostAddress(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PostAddress`.

    Details:
        - Layer: ``123``
        - ID: ``0x1e8caaeb``

    Parameters:
        street_line1: ``str``
        street_line2: ``str``
        city: ``str``
        state: ``str``
        country_iso2: ``str``
        post_code: ``str``
    """

    __slots__: List[str] = ["street_line1", "street_line2", "city", "state", "country_iso2", "post_code"]

    ID = 0x1e8caaeb
    QUALNAME = "types.PostAddress"

    def __init__(self, *, street_line1: str, street_line2: str, city: str, state: str, country_iso2: str,
                 post_code: str) -> None:
        self.street_line1 = street_line1  # string
        self.street_line2 = street_line2  # string
        self.city = city  # string
        self.state = state  # string
        self.country_iso2 = country_iso2  # string
        self.post_code = post_code  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PostAddress":
        # No flags

        street_line1 = String.read(data)

        street_line2 = String.read(data)

        city = String.read(data)

        state = String.read(data)

        country_iso2 = String.read(data)

        post_code = String.read(data)

        return PostAddress(street_line1=street_line1, street_line2=street_line2, city=city, state=state,
                           country_iso2=country_iso2, post_code=post_code)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.street_line1))

        data.write(String(self.street_line2))

        data.write(String(self.city))

        data.write(String(self.state))

        data.write(String(self.country_iso2))

        data.write(String(self.post_code))

        return data.getvalue()
