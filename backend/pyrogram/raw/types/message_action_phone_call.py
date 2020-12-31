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


class MessageActionPhoneCall(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``122``
        - ID: ``0x80e11a7f``

    Parameters:
        call_id: ``int`` ``64-bit``
        video (optional): ``bool``
        reason (optional): :obj:`PhoneCallDiscardReason <pyrogram.raw.base.PhoneCallDiscardReason>`
        duration (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["call_id", "video", "reason", "duration"]

    ID = 0x80e11a7f
    QUALNAME = "types.MessageActionPhoneCall"

    def __init__(self, *, call_id: int, video: Union[None, bool] = None,
                 reason: "raw.base.PhoneCallDiscardReason" = None, duration: Union[None, int] = None) -> None:
        self.call_id = call_id  # long
        self.video = video  # flags.2?true
        self.reason = reason  # flags.0?PhoneCallDiscardReason
        self.duration = duration  # flags.1?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MessageActionPhoneCall":
        flags = Int.read(data)

        video = True if flags & (1 << 2) else False
        call_id = Long.read(data)

        reason = TLObject.read(data) if flags & (1 << 0) else None

        duration = Int.read(data) if flags & (1 << 1) else None
        return MessageActionPhoneCall(call_id=call_id, video=video, reason=reason, duration=duration)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.video else 0
        flags |= (1 << 0) if self.reason is not None else 0
        flags |= (1 << 1) if self.duration is not None else 0
        data.write(Int(flags))

        data.write(Long(self.call_id))

        if self.reason is not None:
            data.write(self.reason.write())

        if self.duration is not None:
            data.write(Int(self.duration))

        return data.getvalue()
