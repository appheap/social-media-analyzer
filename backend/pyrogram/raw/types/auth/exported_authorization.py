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


class ExportedAuthorization(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.auth.ExportedAuthorization`.

    Details:
        - Layer: ``120``
        - ID: ``0xdf969c2d``

    Parameters:
        id: ``int`` ``32-bit``
        bytes: ``bytes``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`auth.ExportAuthorization <pyrogram.raw.functions.auth.ExportAuthorization>`
    """

    __slots__: List[str] = ["id", "bytes"]

    ID = 0xdf969c2d
    QUALNAME = "types.auth.ExportedAuthorization"

    def __init__(self, *, id: int, bytes: bytes) -> None:
        self.id = id  # int
        self.bytes = bytes  # bytes

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ExportedAuthorization":
        # No flags

        id = Int.read(data)

        bytes = Bytes.read(data)

        return ExportedAuthorization(id=id, bytes=bytes)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.id))

        data.write(Bytes(self.bytes))

        return data.getvalue()
