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


class ServerDHParamsFail(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ServerDHParams`.

    Details:
        - Layer: ``117``
        - ID: ``0x79cb045d``

    Parameters:
        nonce: ``int`` ``128-bit``
        server_nonce: ``int`` ``128-bit``
        new_nonce_hash: ``int`` ``128-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`ReqDHParams <pyrogram.raw.functions.ReqDHParams>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "new_nonce_hash"]

    ID = 0x79cb045d
    QUALNAME = "types.ServerDHParamsFail"

    def __init__(self, *, nonce: int, server_nonce: int, new_nonce_hash: int) -> None:
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.new_nonce_hash = new_nonce_hash  # int128

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ServerDHParamsFail":
        # No flags

        nonce = Int128.read(data)

        server_nonce = Int128.read(data)

        new_nonce_hash = Int128.read(data)

        return ServerDHParamsFail(nonce=nonce, server_nonce=server_nonce, new_nonce_hash=new_nonce_hash)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int128(self.nonce))

        data.write(Int128(self.server_nonce))

        data.write(Int128(self.new_nonce_hash))

        return data.getvalue()
