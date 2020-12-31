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


class ValidateRequestedInfo(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0x770a8e74``

    Parameters:
        msg_id: ``int`` ``32-bit``
        info: :obj:`PaymentRequestedInfo <pyrogram.raw.base.PaymentRequestedInfo>`
        save (optional): ``bool``

    Returns:
        :obj:`payments.ValidatedRequestedInfo <pyrogram.raw.base.payments.ValidatedRequestedInfo>`
    """

    __slots__: List[str] = ["msg_id", "info", "save"]

    ID = 0x770a8e74
    QUALNAME = "functions.payments.ValidateRequestedInfo"

    def __init__(self, *, msg_id: int, info: "raw.base.PaymentRequestedInfo", save: Union[None, bool] = None) -> None:
        self.msg_id = msg_id  # int
        self.info = info  # PaymentRequestedInfo
        self.save = save  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ValidateRequestedInfo":
        flags = Int.read(data)

        save = True if flags & (1 << 0) else False
        msg_id = Int.read(data)

        info = TLObject.read(data)

        return ValidateRequestedInfo(msg_id=msg_id, info=info, save=save)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.save else 0
        data.write(Int(flags))

        data.write(Int(self.msg_id))

        data.write(self.info.write())

        return data.getvalue()
