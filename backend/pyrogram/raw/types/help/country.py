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


class Country(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.help.Country`.

    Details:
        - Layer: ``123``
        - ID: ``0xc3878e23``

    Parameters:
        iso2: ``str``
        default_name: ``str``
        country_codes: List of :obj:`help.CountryCode <pyrogram.raw.base.help.CountryCode>`
        hidden (optional): ``bool``
        name (optional): ``str``
    """

    __slots__: List[str] = ["iso2", "default_name", "country_codes", "hidden", "name"]

    ID = 0xc3878e23
    QUALNAME = "types.help.Country"

    def __init__(self, *, iso2: str, default_name: str, country_codes: List["raw.base.help.CountryCode"],
                 hidden: Union[None, bool] = None, name: Union[None, str] = None) -> None:
        self.iso2 = iso2  # string
        self.default_name = default_name  # string
        self.country_codes = country_codes  # Vector<help.CountryCode>
        self.hidden = hidden  # flags.0?true
        self.name = name  # flags.1?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Country":
        flags = Int.read(data)

        hidden = True if flags & (1 << 0) else False
        iso2 = String.read(data)

        default_name = String.read(data)

        name = String.read(data) if flags & (1 << 1) else None
        country_codes = TLObject.read(data)

        return Country(iso2=iso2, default_name=default_name, country_codes=country_codes, hidden=hidden, name=name)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.hidden else 0
        flags |= (1 << 1) if self.name is not None else 0
        data.write(Int(flags))

        data.write(String(self.iso2))

        data.write(String(self.default_name))

        if self.name is not None:
            data.write(String(self.name))

        data.write(Vector(self.country_codes))

        return data.getvalue()
