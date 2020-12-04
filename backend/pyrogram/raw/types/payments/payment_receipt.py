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


class PaymentReceipt(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.payments.PaymentReceipt`.

    Details:
        - Layer: ``120``
        - ID: ``0x500911e1``

    Parameters:
        date: ``int`` ``32-bit``
        bot_id: ``int`` ``32-bit``
        invoice: :obj:`Invoice <pyrogram.raw.base.Invoice>`
        provider_id: ``int`` ``32-bit``
        currency: ``str``
        total_amount: ``int`` ``64-bit``
        credentials_title: ``str``
        users: List of :obj:`User <pyrogram.raw.base.User>`
        info (optional): :obj:`PaymentRequestedInfo <pyrogram.raw.base.PaymentRequestedInfo>`
        shipping (optional): :obj:`ShippingOption <pyrogram.raw.base.ShippingOption>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`payments.GetPaymentReceipt <pyrogram.raw.functions.payments.GetPaymentReceipt>`
    """

    __slots__: List[str] = ["date", "bot_id", "invoice", "provider_id", "currency", "total_amount", "credentials_title",
                            "users", "info", "shipping"]

    ID = 0x500911e1
    QUALNAME = "types.payments.PaymentReceipt"

    def __init__(self, *, date: int, bot_id: int, invoice: "raw.base.Invoice", provider_id: int, currency: str,
                 total_amount: int, credentials_title: str, users: List["raw.base.User"],
                 info: "raw.base.PaymentRequestedInfo" = None, shipping: "raw.base.ShippingOption" = None) -> None:
        self.date = date  # int
        self.bot_id = bot_id  # int
        self.invoice = invoice  # Invoice
        self.provider_id = provider_id  # int
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.credentials_title = credentials_title  # string
        self.users = users  # Vector<User>
        self.info = info  # flags.0?PaymentRequestedInfo
        self.shipping = shipping  # flags.1?ShippingOption

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PaymentReceipt":
        flags = Int.read(data)

        date = Int.read(data)

        bot_id = Int.read(data)

        invoice = TLObject.read(data)

        provider_id = Int.read(data)

        info = TLObject.read(data) if flags & (1 << 0) else None

        shipping = TLObject.read(data) if flags & (1 << 1) else None

        currency = String.read(data)

        total_amount = Long.read(data)

        credentials_title = String.read(data)

        users = TLObject.read(data)

        return PaymentReceipt(date=date, bot_id=bot_id, invoice=invoice, provider_id=provider_id, currency=currency,
                              total_amount=total_amount, credentials_title=credentials_title, users=users, info=info,
                              shipping=shipping)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.info is not None else 0
        flags |= (1 << 1) if self.shipping is not None else 0
        data.write(Int(flags))

        data.write(Int(self.date))

        data.write(Int(self.bot_id))

        data.write(self.invoice.write())

        data.write(Int(self.provider_id))

        if self.info is not None:
            data.write(self.info.write())

        if self.shipping is not None:
            data.write(self.shipping.write())

        data.write(String(self.currency))

        data.write(Long(self.total_amount))

        data.write(String(self.credentials_title))

        data.write(Vector(self.users))

        return data.getvalue()
