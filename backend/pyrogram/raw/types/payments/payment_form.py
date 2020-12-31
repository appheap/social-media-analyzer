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


class PaymentForm(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.payments.PaymentForm`.

    Details:
        - Layer: ``122``
        - ID: ``0x3f56aea3``

    Parameters:
        bot_id: ``int`` ``32-bit``
        invoice: :obj:`Invoice <pyrogram.raw.base.Invoice>`
        provider_id: ``int`` ``32-bit``
        url: ``str``
        users: List of :obj:`User <pyrogram.raw.base.User>`
        can_save_credentials (optional): ``bool``
        password_missing (optional): ``bool``
        native_provider (optional): ``str``
        native_params (optional): :obj:`DataJSON <pyrogram.raw.base.DataJSON>`
        saved_info (optional): :obj:`PaymentRequestedInfo <pyrogram.raw.base.PaymentRequestedInfo>`
        saved_credentials (optional): :obj:`PaymentSavedCredentials <pyrogram.raw.base.PaymentSavedCredentials>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`payments.GetPaymentForm <pyrogram.raw.functions.payments.GetPaymentForm>`
    """

    __slots__: List[str] = ["bot_id", "invoice", "provider_id", "url", "users", "can_save_credentials",
                            "password_missing", "native_provider", "native_params", "saved_info", "saved_credentials"]

    ID = 0x3f56aea3
    QUALNAME = "types.payments.PaymentForm"

    def __init__(self, *, bot_id: int, invoice: "raw.base.Invoice", provider_id: int, url: str,
                 users: List["raw.base.User"], can_save_credentials: Union[None, bool] = None,
                 password_missing: Union[None, bool] = None, native_provider: Union[None, str] = None,
                 native_params: "raw.base.DataJSON" = None, saved_info: "raw.base.PaymentRequestedInfo" = None,
                 saved_credentials: "raw.base.PaymentSavedCredentials" = None) -> None:
        self.bot_id = bot_id  # int
        self.invoice = invoice  # Invoice
        self.provider_id = provider_id  # int
        self.url = url  # string
        self.users = users  # Vector<User>
        self.can_save_credentials = can_save_credentials  # flags.2?true
        self.password_missing = password_missing  # flags.3?true
        self.native_provider = native_provider  # flags.4?string
        self.native_params = native_params  # flags.4?DataJSON
        self.saved_info = saved_info  # flags.0?PaymentRequestedInfo
        self.saved_credentials = saved_credentials  # flags.1?PaymentSavedCredentials

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PaymentForm":
        flags = Int.read(data)

        can_save_credentials = True if flags & (1 << 2) else False
        password_missing = True if flags & (1 << 3) else False
        bot_id = Int.read(data)

        invoice = TLObject.read(data)

        provider_id = Int.read(data)

        url = String.read(data)

        native_provider = String.read(data) if flags & (1 << 4) else None
        native_params = TLObject.read(data) if flags & (1 << 4) else None

        saved_info = TLObject.read(data) if flags & (1 << 0) else None

        saved_credentials = TLObject.read(data) if flags & (1 << 1) else None

        users = TLObject.read(data)

        return PaymentForm(bot_id=bot_id, invoice=invoice, provider_id=provider_id, url=url, users=users,
                           can_save_credentials=can_save_credentials, password_missing=password_missing,
                           native_provider=native_provider, native_params=native_params, saved_info=saved_info,
                           saved_credentials=saved_credentials)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.can_save_credentials else 0
        flags |= (1 << 3) if self.password_missing else 0
        flags |= (1 << 4) if self.native_provider is not None else 0
        flags |= (1 << 4) if self.native_params is not None else 0
        flags |= (1 << 0) if self.saved_info is not None else 0
        flags |= (1 << 1) if self.saved_credentials is not None else 0
        data.write(Int(flags))

        data.write(Int(self.bot_id))

        data.write(self.invoice.write())

        data.write(Int(self.provider_id))

        data.write(String(self.url))

        if self.native_provider is not None:
            data.write(String(self.native_provider))

        if self.native_params is not None:
            data.write(self.native_params.write())

        if self.saved_info is not None:
            data.write(self.saved_info.write())

        if self.saved_credentials is not None:
            data.write(self.saved_credentials.write())

        data.write(Vector(self.users))

        return data.getvalue()
