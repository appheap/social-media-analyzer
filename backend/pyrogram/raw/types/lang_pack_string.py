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


class LangPackString(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.LangPackString`.

    Details:
        - Layer: ``120``
        - ID: ``0xcad181f6``

    Parameters:
        key: ``str``
        value: ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`langpack.GetStrings <pyrogram.raw.functions.langpack.GetStrings>`
    """

    __slots__: List[str] = ["key", "value"]

    ID = 0xcad181f6
    QUALNAME = "types.LangPackString"

    def __init__(self, *, key: str, value: str) -> None:
        self.key = key  # string
        self.value = value  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "LangPackString":
        # No flags

        key = String.read(data)

        value = String.read(data)

        return LangPackString(key=key, value=value)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.key))

        data.write(String(self.value))

        return data.getvalue()
