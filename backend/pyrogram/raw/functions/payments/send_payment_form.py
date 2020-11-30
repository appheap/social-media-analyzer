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


class SendPaymentForm(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0x2b8879b3``

    Parameters:
        msg_id: ``int`` ``32-bit``
        credentials: :obj:`InputPaymentCredentials <pyrogram.raw.base.InputPaymentCredentials>`
        requested_info_id (optional): ``str``
        shipping_option_id (optional): ``str``

    Returns:
        :obj:`payments.PaymentResult <pyrogram.raw.base.payments.PaymentResult>`
    """

    __slots__: List[str] = ["msg_id", "credentials", "requested_info_id", "shipping_option_id"]

    ID = 0x2b8879b3
    QUALNAME = "functions.payments.SendPaymentForm"

    def __init__(self, *, msg_id: int, credentials: "raw.base.InputPaymentCredentials",
                 requested_info_id: Union[None, str] = None, shipping_option_id: Union[None, str] = None) -> None:
        self.msg_id = msg_id  # int
        self.credentials = credentials  # InputPaymentCredentials
        self.requested_info_id = requested_info_id  # flags.0?string
        self.shipping_option_id = shipping_option_id  # flags.1?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SendPaymentForm":
        flags = Int.read(data)

        msg_id = Int.read(data)

        requested_info_id = String.read(data) if flags & (1 << 0) else None
        shipping_option_id = String.read(data) if flags & (1 << 1) else None
        credentials = TLObject.read(data)

        return SendPaymentForm(msg_id=msg_id, credentials=credentials, requested_info_id=requested_info_id,
                               shipping_option_id=shipping_option_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.requested_info_id is not None else 0
        flags |= (1 << 1) if self.shipping_option_id is not None else 0
        data.write(Int(flags))

        data.write(Int(self.msg_id))

        if self.requested_info_id is not None:
            data.write(String(self.requested_info_id))

        if self.shipping_option_id is not None:
            data.write(String(self.shipping_option_id))

        data.write(self.credentials.write())

        return data.getvalue()
