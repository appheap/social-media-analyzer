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


class ServerDHInnerData(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ServerDHInnerData`.

    Details:
        - Layer: ``122``
        - ID: ``0xb5890dba``

    Parameters:
        nonce: ``int`` ``128-bit``
        server_nonce: ``int`` ``128-bit``
        g: ``int`` ``32-bit``
        dh_prime: ``bytes``
        g_a: ``bytes``
        server_time: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["nonce", "server_nonce", "g", "dh_prime", "g_a", "server_time"]

    ID = 0xb5890dba
    QUALNAME = "types.ServerDHInnerData"

    def __init__(self, *, nonce: int, server_nonce: int, g: int, dh_prime: bytes, g_a: bytes, server_time: int) -> None:
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.g = g  # int
        self.dh_prime = dh_prime  # bytes
        self.g_a = g_a  # bytes
        self.server_time = server_time  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ServerDHInnerData":
        # No flags

        nonce = Int128.read(data)

        server_nonce = Int128.read(data)

        g = Int.read(data)

        dh_prime = Bytes.read(data)

        g_a = Bytes.read(data)

        server_time = Int.read(data)

        return ServerDHInnerData(nonce=nonce, server_nonce=server_nonce, g=g, dh_prime=dh_prime, g_a=g_a,
                                 server_time=server_time)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int128(self.nonce))

        data.write(Int128(self.server_nonce))

        data.write(Int(self.g))

        data.write(Bytes(self.dh_prime))

        data.write(Bytes(self.g_a))

        data.write(Int(self.server_time))

        return data.getvalue()
