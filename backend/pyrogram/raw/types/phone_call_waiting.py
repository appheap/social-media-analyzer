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


class PhoneCallWaiting(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PhoneCall`.

    Details:
        - Layer: ``123``
        - ID: ``0x1b8f4ad1``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        date: ``int`` ``32-bit``
        admin_id: ``int`` ``32-bit``
        participant_id: ``int`` ``32-bit``
        protocol: :obj:`PhoneCallProtocol <pyrogram.raw.base.PhoneCallProtocol>`
        video (optional): ``bool``
        receive_date (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id", "protocol", "video",
                            "receive_date"]

    ID = 0x1b8f4ad1
    QUALNAME = "types.PhoneCallWaiting"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int,
                 protocol: "raw.base.PhoneCallProtocol", video: Union[None, bool] = None,
                 receive_date: Union[None, int] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # int
        self.participant_id = participant_id  # int
        self.protocol = protocol  # PhoneCallProtocol
        self.video = video  # flags.6?true
        self.receive_date = receive_date  # flags.0?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PhoneCallWaiting":
        flags = Int.read(data)

        video = True if flags & (1 << 6) else False
        id = Long.read(data)

        access_hash = Long.read(data)

        date = Int.read(data)

        admin_id = Int.read(data)

        participant_id = Int.read(data)

        protocol = TLObject.read(data)

        receive_date = Int.read(data) if flags & (1 << 0) else None
        return PhoneCallWaiting(id=id, access_hash=access_hash, date=date, admin_id=admin_id,
                                participant_id=participant_id, protocol=protocol, video=video,
                                receive_date=receive_date)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 6) if self.video else 0
        flags |= (1 << 0) if self.receive_date is not None else 0
        data.write(Int(flags))

        data.write(Long(self.id))

        data.write(Long(self.access_hash))

        data.write(Int(self.date))

        data.write(Int(self.admin_id))

        data.write(Int(self.participant_id))

        data.write(self.protocol.write())

        if self.receive_date is not None:
            data.write(Int(self.receive_date))

        return data.getvalue()
