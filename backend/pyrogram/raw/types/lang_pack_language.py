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


class LangPackLanguage(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.LangPackLanguage`.

    Details:
        - Layer: ``122``
        - ID: ``0xeeca5ce3``

    Parameters:
        name: ``str``
        native_name: ``str``
        lang_code: ``str``
        plural_code: ``str``
        strings_count: ``int`` ``32-bit``
        translated_count: ``int`` ``32-bit``
        translations_url: ``str``
        official (optional): ``bool``
        rtl (optional): ``bool``
        beta (optional): ``bool``
        base_lang_code (optional): ``str``

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`langpack.GetLanguages <pyrogram.raw.functions.langpack.GetLanguages>`
            - :obj:`langpack.GetLanguage <pyrogram.raw.functions.langpack.GetLanguage>`
    """

    __slots__: List[str] = ["name", "native_name", "lang_code", "plural_code", "strings_count", "translated_count",
                            "translations_url", "official", "rtl", "beta", "base_lang_code"]

    ID = 0xeeca5ce3
    QUALNAME = "types.LangPackLanguage"

    def __init__(self, *, name: str, native_name: str, lang_code: str, plural_code: str, strings_count: int,
                 translated_count: int, translations_url: str, official: Union[None, bool] = None,
                 rtl: Union[None, bool] = None, beta: Union[None, bool] = None,
                 base_lang_code: Union[None, str] = None) -> None:
        self.name = name  # string
        self.native_name = native_name  # string
        self.lang_code = lang_code  # string
        self.plural_code = plural_code  # string
        self.strings_count = strings_count  # int
        self.translated_count = translated_count  # int
        self.translations_url = translations_url  # string
        self.official = official  # flags.0?true
        self.rtl = rtl  # flags.2?true
        self.beta = beta  # flags.3?true
        self.base_lang_code = base_lang_code  # flags.1?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "LangPackLanguage":
        flags = Int.read(data)

        official = True if flags & (1 << 0) else False
        rtl = True if flags & (1 << 2) else False
        beta = True if flags & (1 << 3) else False
        name = String.read(data)

        native_name = String.read(data)

        lang_code = String.read(data)

        base_lang_code = String.read(data) if flags & (1 << 1) else None
        plural_code = String.read(data)

        strings_count = Int.read(data)

        translated_count = Int.read(data)

        translations_url = String.read(data)

        return LangPackLanguage(name=name, native_name=native_name, lang_code=lang_code, plural_code=plural_code,
                                strings_count=strings_count, translated_count=translated_count,
                                translations_url=translations_url, official=official, rtl=rtl, beta=beta,
                                base_lang_code=base_lang_code)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.official else 0
        flags |= (1 << 2) if self.rtl else 0
        flags |= (1 << 3) if self.beta else 0
        flags |= (1 << 1) if self.base_lang_code is not None else 0
        data.write(Int(flags))

        data.write(String(self.name))

        data.write(String(self.native_name))

        data.write(String(self.lang_code))

        if self.base_lang_code is not None:
            data.write(String(self.base_lang_code))

        data.write(String(self.plural_code))

        data.write(Int(self.strings_count))

        data.write(Int(self.translated_count))

        data.write(String(self.translations_url))

        return data.getvalue()
