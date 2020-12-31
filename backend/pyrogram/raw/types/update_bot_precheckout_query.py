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


class UpdateBotPrecheckoutQuery(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``122``
        - ID: ``0x5d2f3aa9``

    Parameters:
        query_id: ``int`` ``64-bit``
        user_id: ``int`` ``32-bit``
        payload: ``bytes``
        currency: ``str``
        total_amount: ``int`` ``64-bit``
        info (optional): :obj:`PaymentRequestedInfo <pyrogram.raw.base.PaymentRequestedInfo>`
        shipping_option_id (optional): ``str``
    """

    __slots__: List[str] = ["query_id", "user_id", "payload", "currency", "total_amount", "info", "shipping_option_id"]

    ID = 0x5d2f3aa9
    QUALNAME = "types.UpdateBotPrecheckoutQuery"

    def __init__(self, *, query_id: int, user_id: int, payload: bytes, currency: str, total_amount: int,
                 info: "raw.base.PaymentRequestedInfo" = None, shipping_option_id: Union[None, str] = None) -> None:
        self.query_id = query_id  # long
        self.user_id = user_id  # int
        self.payload = payload  # bytes
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.info = info  # flags.0?PaymentRequestedInfo
        self.shipping_option_id = shipping_option_id  # flags.1?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateBotPrecheckoutQuery":
        flags = Int.read(data)

        query_id = Long.read(data)

        user_id = Int.read(data)

        payload = Bytes.read(data)

        info = TLObject.read(data) if flags & (1 << 0) else None

        shipping_option_id = String.read(data) if flags & (1 << 1) else None
        currency = String.read(data)

        total_amount = Long.read(data)

        return UpdateBotPrecheckoutQuery(query_id=query_id, user_id=user_id, payload=payload, currency=currency,
                                         total_amount=total_amount, info=info, shipping_option_id=shipping_option_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.info is not None else 0
        flags |= (1 << 1) if self.shipping_option_id is not None else 0
        data.write(Int(flags))

        data.write(Long(self.query_id))

        data.write(Int(self.user_id))

        data.write(Bytes(self.payload))

        if self.info is not None:
            data.write(self.info.write())

        if self.shipping_option_id is not None:
            data.write(String(self.shipping_option_id))

        data.write(String(self.currency))

        data.write(Long(self.total_amount))

        return data.getvalue()
