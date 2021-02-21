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


class PhoneCall(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PhoneCall`.

    Details:
        - Layer: ``123``
        - ID: ``0x8742ae7f``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        date: ``int`` ``32-bit``
        admin_id: ``int`` ``32-bit``
        participant_id: ``int`` ``32-bit``
        g_a_or_b: ``bytes``
        key_fingerprint: ``int`` ``64-bit``
        protocol: :obj:`PhoneCallProtocol <pyrogram.raw.base.PhoneCallProtocol>`
        connections: List of :obj:`PhoneConnection <pyrogram.raw.base.PhoneConnection>`
        start_date: ``int`` ``32-bit``
        p2p_allowed (optional): ``bool``
        video (optional): ``bool``
    """

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id", "g_a_or_b", "key_fingerprint",
                            "protocol", "connections", "start_date", "p2p_allowed", "video"]

    ID = 0x8742ae7f
    QUALNAME = "types.PhoneCall"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_a_or_b: bytes,
                 key_fingerprint: int, protocol: "raw.base.PhoneCallProtocol",
                 connections: List["raw.base.PhoneConnection"], start_date: int, p2p_allowed: Union[None, bool] = None,
                 video: Union[None, bool] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # int
        self.participant_id = participant_id  # int
        self.g_a_or_b = g_a_or_b  # bytes
        self.key_fingerprint = key_fingerprint  # long
        self.protocol = protocol  # PhoneCallProtocol
        self.connections = connections  # Vector<PhoneConnection>
        self.start_date = start_date  # int
        self.p2p_allowed = p2p_allowed  # flags.5?true
        self.video = video  # flags.6?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PhoneCall":
        flags = Int.read(data)

        p2p_allowed = True if flags & (1 << 5) else False
        video = True if flags & (1 << 6) else False
        id = Long.read(data)

        access_hash = Long.read(data)

        date = Int.read(data)

        admin_id = Int.read(data)

        participant_id = Int.read(data)

        g_a_or_b = Bytes.read(data)

        key_fingerprint = Long.read(data)

        protocol = TLObject.read(data)

        connections = TLObject.read(data)

        start_date = Int.read(data)

        return PhoneCall(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id,
                         g_a_or_b=g_a_or_b, key_fingerprint=key_fingerprint, protocol=protocol, connections=connections,
                         start_date=start_date, p2p_allowed=p2p_allowed, video=video)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.p2p_allowed else 0
        flags |= (1 << 6) if self.video else 0
        data.write(Int(flags))

        data.write(Long(self.id))

        data.write(Long(self.access_hash))

        data.write(Int(self.date))

        data.write(Int(self.admin_id))

        data.write(Int(self.participant_id))

        data.write(Bytes(self.g_a_or_b))

        data.write(Long(self.key_fingerprint))

        data.write(self.protocol.write())

        data.write(Vector(self.connections))

        data.write(Int(self.start_date))

        return data.getvalue()
