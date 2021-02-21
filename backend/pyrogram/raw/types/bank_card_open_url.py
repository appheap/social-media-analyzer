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


class BankCardOpenUrl(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.BankCardOpenUrl`.

    Details:
        - Layer: ``123``
        - ID: ``0xf568028a``

    Parameters:
        url: ``str``
        name: ``str``
    """

    __slots__: List[str] = ["url", "name"]

    ID = 0xf568028a
    QUALNAME = "types.BankCardOpenUrl"

    def __init__(self, *, url: str, name: str) -> None:
        self.url = url  # string
        self.name = name  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "BankCardOpenUrl":
        # No flags

        url = String.read(data)

        name = String.read(data)

        return BankCardOpenUrl(url=url, name=name)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.url))

        data.write(String(self.name))

        return data.getvalue()
