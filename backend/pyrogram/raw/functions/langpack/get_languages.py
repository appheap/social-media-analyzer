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


class GetLanguages(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0x42c6978f``

    Parameters:
        lang_pack: ``str``

    Returns:
        List of :obj:`LangPackLanguage <pyrogram.raw.base.LangPackLanguage>`
    """

    __slots__: List[str] = ["lang_pack"]

    ID = 0x42c6978f
    QUALNAME = "functions.langpack.GetLanguages"

    def __init__(self, *, lang_pack: str) -> None:
        self.lang_pack = lang_pack  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetLanguages":
        # No flags

        lang_pack = String.read(data)

        return GetLanguages(lang_pack=lang_pack)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.lang_pack))

        return data.getvalue()
