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


class DhGenFail(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.SetClientDHParamsAnswer`.

    Details:
        - Layer: ``123``
        - ID: ``0xa69dae02``

    Parameters:
        nonce: ``int`` ``128-bit``
        server_nonce: ``int`` ``128-bit``
        new_nonce_hash3: ``int`` ``128-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`SetClientDHParams <pyrogram.raw.functions.SetClientDHParams>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "new_nonce_hash3"]

    ID = 0xa69dae02
    QUALNAME = "types.DhGenFail"

    def __init__(self, *, nonce: int, server_nonce: int, new_nonce_hash3: int) -> None:
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.new_nonce_hash3 = new_nonce_hash3  # int128

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "DhGenFail":
        # No flags

        nonce = Int128.read(data)

        server_nonce = Int128.read(data)

        new_nonce_hash3 = Int128.read(data)

        return DhGenFail(nonce=nonce, server_nonce=server_nonce, new_nonce_hash3=new_nonce_hash3)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int128(self.nonce))

        data.write(Int128(self.server_nonce))

        data.write(Int128(self.new_nonce_hash3))

        return data.getvalue()
