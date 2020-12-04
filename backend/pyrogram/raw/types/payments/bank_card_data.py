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


class BankCardData(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.payments.BankCardData`.

    Details:
        - Layer: ``120``
        - ID: ``0x3e24e573``

    Parameters:
        title: ``str``
        open_urls: List of :obj:`BankCardOpenUrl <pyrogram.raw.base.BankCardOpenUrl>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`payments.GetBankCardData <pyrogram.raw.functions.payments.GetBankCardData>`
    """

    __slots__: List[str] = ["title", "open_urls"]

    ID = 0x3e24e573
    QUALNAME = "types.payments.BankCardData"

    def __init__(self, *, title: str, open_urls: List["raw.base.BankCardOpenUrl"]) -> None:
        self.title = title  # string
        self.open_urls = open_urls  # Vector<BankCardOpenUrl>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "BankCardData":
        # No flags

        title = String.read(data)

        open_urls = TLObject.read(data)

        return BankCardData(title=title, open_urls=open_urls)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.title))

        data.write(Vector(self.open_urls))

        return data.getvalue()
