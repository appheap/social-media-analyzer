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

import pyrogram

from pyrogram import raw
from ..object import Object
from pyrogram import types


class Invoice(Object):
    """A point on the map.

    # todo: update docs

    Parameters:


    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,

            title: str,
            description: str,
            currency: str,
            total_amount: int,
            start_param: str,
            shipping_address_requested: bool = None,
            test: bool = None,
            photo: "types.WebDocument" = None,
            receipt_message_id: int = None,

    ):
        super().__init__(client)

        self.title = title
        self.description = description
        self.currency = currency
        self.total_amount = total_amount
        self.start_param = start_param
        self.shipping_address_requested = shipping_address_requested
        self.test = test
        self.photo = photo
        self.receipt_message_id = receipt_message_id

    @staticmethod
    def _parse(client, invoice: "raw.types.MessageMediaInvoice") -> "Invoice":
        if isinstance(invoice, raw.types.MessageMediaInvoice):
            return Invoice(
                client=client,

                title=invoice.title,
                description=invoice.description,
                currency=invoice.currency,
                total_amount=invoice.total_amount,
                start_param=invoice.start_param,
                shipping_address_requested=getattr(invoice, 'shipping_address_requested', None),
                test=getattr(invoice, 'test', None),
                photo=types.WebDocument._parse(client, getattr(invoice, 'photo', None)),
                receipt_message_id=getattr(invoice, 'receipt_msg_id')

            )
