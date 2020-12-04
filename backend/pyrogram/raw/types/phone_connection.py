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


class PhoneConnection(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PhoneConnection`.

    Details:
        - Layer: ``120``
        - ID: ``0x9d4c17c0``

    Parameters:
        id: ``int`` ``64-bit``
        ip: ``str``
        ipv6: ``str``
        port: ``int`` ``32-bit``
        peer_tag: ``bytes``
    """

    __slots__: List[str] = ["id", "ip", "ipv6", "port", "peer_tag"]

    ID = 0x9d4c17c0
    QUALNAME = "types.PhoneConnection"

    def __init__(self, *, id: int, ip: str, ipv6: str, port: int, peer_tag: bytes) -> None:
        self.id = id  # long
        self.ip = ip  # string
        self.ipv6 = ipv6  # string
        self.port = port  # int
        self.peer_tag = peer_tag  # bytes

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PhoneConnection":
        # No flags

        id = Long.read(data)

        ip = String.read(data)

        ipv6 = String.read(data)

        port = Int.read(data)

        peer_tag = Bytes.read(data)

        return PhoneConnection(id=id, ip=ip, ipv6=ipv6, port=port, peer_tag=peer_tag)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Long(self.id))

        data.write(String(self.ip))

        data.write(String(self.ipv6))

        data.write(Int(self.port))

        data.write(Bytes(self.peer_tag))

        return data.getvalue()
