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


class ClientDHInnerData(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ClientDHInnerData`.

    Details:
        - Layer: ``120``
        - ID: ``0x6643b654``

    Parameters:
        nonce: ``int`` ``128-bit``
        server_nonce: ``int`` ``128-bit``
        retry_id: ``int`` ``64-bit``
        g_b: ``bytes``
    """

    __slots__: List[str] = ["nonce", "server_nonce", "retry_id", "g_b"]

    ID = 0x6643b654
    QUALNAME = "types.ClientDHInnerData"

    def __init__(self, *, nonce: int, server_nonce: int, retry_id: int, g_b: bytes) -> None:
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.retry_id = retry_id  # long
        self.g_b = g_b  # bytes

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ClientDHInnerData":
        # No flags

        nonce = Int128.read(data)

        server_nonce = Int128.read(data)

        retry_id = Long.read(data)

        g_b = Bytes.read(data)

        return ClientDHInnerData(nonce=nonce, server_nonce=server_nonce, retry_id=retry_id, g_b=g_b)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int128(self.nonce))

        data.write(Int128(self.server_nonce))

        data.write(Long(self.retry_id))

        data.write(Bytes(self.g_b))

        return data.getvalue()
