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


class AcceptCall(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x3bd2b4a0``

    Parameters:
        peer: :obj:`InputPhoneCall <pyrogram.raw.base.InputPhoneCall>`
        g_b: ``bytes``
        protocol: :obj:`PhoneCallProtocol <pyrogram.raw.base.PhoneCallProtocol>`

    Returns:
        :obj:`phone.PhoneCall <pyrogram.raw.base.phone.PhoneCall>`
    """

    __slots__: List[str] = ["peer", "g_b", "protocol"]

    ID = 0x3bd2b4a0
    QUALNAME = "functions.phone.AcceptCall"

    def __init__(self, *, peer: "raw.base.InputPhoneCall", g_b: bytes, protocol: "raw.base.PhoneCallProtocol") -> None:
        self.peer = peer  # InputPhoneCall
        self.g_b = g_b  # bytes
        self.protocol = protocol  # PhoneCallProtocol

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "AcceptCall":
        # No flags

        peer = TLObject.read(data)

        g_b = Bytes.read(data)

        protocol = TLObject.read(data)

        return AcceptCall(peer=peer, g_b=g_b, protocol=protocol)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.peer.write())

        data.write(Bytes(self.g_b))

        data.write(self.protocol.write())

        return data.getvalue()
