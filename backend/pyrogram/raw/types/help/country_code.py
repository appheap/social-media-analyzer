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


class CountryCode(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.help.CountryCode`.

    Details:
        - Layer: ``123``
        - ID: ``0x4203c5ef``

    Parameters:
        country_code: ``str``
        prefixes (optional): List of ``str``
        patterns (optional): List of ``str``
    """

    __slots__: List[str] = ["country_code", "prefixes", "patterns"]

    ID = 0x4203c5ef
    QUALNAME = "types.help.CountryCode"

    def __init__(self, *, country_code: str, prefixes: Union[None, List[str]] = None,
                 patterns: Union[None, List[str]] = None) -> None:
        self.country_code = country_code  # string
        self.prefixes = prefixes  # flags.0?Vector<string>
        self.patterns = patterns  # flags.1?Vector<string>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "CountryCode":
        flags = Int.read(data)

        country_code = String.read(data)

        prefixes = TLObject.read(data, String) if flags & (1 << 0) else []

        patterns = TLObject.read(data, String) if flags & (1 << 1) else []

        return CountryCode(country_code=country_code, prefixes=prefixes, patterns=patterns)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.prefixes is not None else 0
        flags |= (1 << 1) if self.patterns is not None else 0
        data.write(Int(flags))

        data.write(String(self.country_code))

        if self.prefixes is not None:
            data.write(Vector(self.prefixes, String))

        if self.patterns is not None:
            data.write(Vector(self.patterns, String))

        return data.getvalue()
