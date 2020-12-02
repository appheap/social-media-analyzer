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


class MessageMediaInvoice(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``121``
        - ID: ``0x84551347``

    Parameters:
        title: ``str``
        description: ``str``
        currency: ``str``
        total_amount: ``int`` ``64-bit``
        start_param: ``str``
        shipping_address_requested (optional): ``bool``
        test (optional): ``bool``
        photo (optional): :obj:`WebDocument <pyrogram.raw.base.WebDocument>`
        receipt_msg_id (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetWebPagePreview <pyrogram.raw.functions.messages.GetWebPagePreview>`
            - :obj:`messages.UploadMedia <pyrogram.raw.functions.messages.UploadMedia>`
    """

    __slots__: List[str] = ["title", "description", "currency", "total_amount", "start_param",
                            "shipping_address_requested", "test", "photo", "receipt_msg_id"]

    ID = 0x84551347
    QUALNAME = "types.MessageMediaInvoice"

    def __init__(self, *, title: str, description: str, currency: str, total_amount: int, start_param: str,
                 shipping_address_requested: Union[None, bool] = None, test: Union[None, bool] = None,
                 photo: "raw.base.WebDocument" = None, receipt_msg_id: Union[None, int] = None) -> None:
        self.title = title  # string
        self.description = description  # string
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.start_param = start_param  # string
        self.shipping_address_requested = shipping_address_requested  # flags.1?true
        self.test = test  # flags.3?true
        self.photo = photo  # flags.0?WebDocument
        self.receipt_msg_id = receipt_msg_id  # flags.2?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MessageMediaInvoice":
        flags = Int.read(data)

        shipping_address_requested = True if flags & (1 << 1) else False
        test = True if flags & (1 << 3) else False
        title = String.read(data)

        description = String.read(data)

        photo = TLObject.read(data) if flags & (1 << 0) else None

        receipt_msg_id = Int.read(data) if flags & (1 << 2) else None
        currency = String.read(data)

        total_amount = Long.read(data)

        start_param = String.read(data)

        return MessageMediaInvoice(title=title, description=description, currency=currency, total_amount=total_amount,
                                   start_param=start_param, shipping_address_requested=shipping_address_requested,
                                   test=test, photo=photo, receipt_msg_id=receipt_msg_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.shipping_address_requested is not None else 0
        flags |= (1 << 3) if self.test is not None else 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 2) if self.receipt_msg_id is not None else 0
        data.write(Int(flags))

        data.write(String(self.title))

        data.write(String(self.description))

        if self.photo is not None:
            data.write(self.photo.write())

        if self.receipt_msg_id is not None:
            data.write(Int(self.receipt_msg_id))

        data.write(String(self.currency))

        data.write(Long(self.total_amount))

        data.write(String(self.start_param))

        return data.getvalue()
