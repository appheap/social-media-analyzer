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


class GetDifference(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0xcd984aa5``

    Parameters:
        lang_pack: ``str``
        lang_code: ``str``
        from_version: ``int`` ``32-bit``

    Returns:
        :obj:`LangPackDifference <pyrogram.raw.base.LangPackDifference>`
    """

    __slots__: List[str] = ["lang_pack", "lang_code", "from_version"]

    ID = 0xcd984aa5
    QUALNAME = "functions.langpack.GetDifference"

    def __init__(self, *, lang_pack: str, lang_code: str, from_version: int) -> None:
        self.lang_pack = lang_pack  # string
        self.lang_code = lang_code  # string
        self.from_version = from_version  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetDifference":
        # No flags

        lang_pack = String.read(data)

        lang_code = String.read(data)

        from_version = Int.read(data)

        return GetDifference(lang_pack=lang_pack, lang_code=lang_code, from_version=from_version)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.lang_pack))

        data.write(String(self.lang_code))

        data.write(Int(self.from_version))

        return data.getvalue()
