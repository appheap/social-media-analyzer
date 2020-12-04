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


class LangPackDifference(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.LangPackDifference`.

    Details:
        - Layer: ``120``
        - ID: ``0xf385c1f6``

    Parameters:
        lang_code: ``str``
        from_version: ``int`` ``32-bit``
        version: ``int`` ``32-bit``
        strings: List of :obj:`LangPackString <pyrogram.raw.base.LangPackString>`

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`langpack.GetLangPack <pyrogram.raw.functions.langpack.GetLangPack>`
            - :obj:`langpack.GetDifference <pyrogram.raw.functions.langpack.GetDifference>`
    """

    __slots__: List[str] = ["lang_code", "from_version", "version", "strings"]

    ID = 0xf385c1f6
    QUALNAME = "types.LangPackDifference"

    def __init__(self, *, lang_code: str, from_version: int, version: int,
                 strings: List["raw.base.LangPackString"]) -> None:
        self.lang_code = lang_code  # string
        self.from_version = from_version  # int
        self.version = version  # int
        self.strings = strings  # Vector<LangPackString>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "LangPackDifference":
        # No flags

        lang_code = String.read(data)

        from_version = Int.read(data)

        version = Int.read(data)

        strings = TLObject.read(data)

        return LangPackDifference(lang_code=lang_code, from_version=from_version, version=version, strings=strings)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.lang_code))

        data.write(Int(self.from_version))

        data.write(Int(self.version))

        data.write(Vector(self.strings))

        return data.getvalue()
