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


class DataJSON(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.DataJSON`.

    Details:
        - Layer: ``121``
        - ID: ``0x7d748d04``

    Parameters:
        data: ``str``

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`bots.SendCustomRequest <pyrogram.raw.functions.bots.SendCustomRequest>`
            - :obj:`phone.GetCallConfig <pyrogram.raw.functions.phone.GetCallConfig>`
    """

    __slots__: List[str] = ["data"]

    ID = 0x7d748d04
    QUALNAME = "types.DataJSON"

    def __init__(self, *, data: str) -> None:
        self.data = data  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "DataJSON":
        # No flags

        data = String.read(data)

        return DataJSON(data=data)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.data))

        return data.getvalue()
