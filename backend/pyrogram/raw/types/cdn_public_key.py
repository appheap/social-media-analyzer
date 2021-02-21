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


class CdnPublicKey(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.CdnPublicKey`.

    Details:
        - Layer: ``123``
        - ID: ``0xc982eaba``

    Parameters:
        dc_id: ``int`` ``32-bit``
        public_key: ``str``
    """

    __slots__: List[str] = ["dc_id", "public_key"]

    ID = 0xc982eaba
    QUALNAME = "types.CdnPublicKey"

    def __init__(self, *, dc_id: int, public_key: str) -> None:
        self.dc_id = dc_id  # int
        self.public_key = public_key  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "CdnPublicKey":
        # No flags

        dc_id = Int.read(data)

        public_key = String.read(data)

        return CdnPublicKey(dc_id=dc_id, public_key=public_key)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.dc_id))

        data.write(String(self.public_key))

        return data.getvalue()
