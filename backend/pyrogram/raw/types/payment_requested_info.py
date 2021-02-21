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


class PaymentRequestedInfo(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PaymentRequestedInfo`.

    Details:
        - Layer: ``123``
        - ID: ``0x909c3f94``

    Parameters:
        name (optional): ``str``
        phone (optional): ``str``
        email (optional): ``str``
        shipping_address (optional): :obj:`PostAddress <pyrogram.raw.base.PostAddress>`
    """

    __slots__: List[str] = ["name", "phone", "email", "shipping_address"]

    ID = 0x909c3f94
    QUALNAME = "types.PaymentRequestedInfo"

    def __init__(self, *, name: Union[None, str] = None, phone: Union[None, str] = None, email: Union[None, str] = None,
                 shipping_address: "raw.base.PostAddress" = None) -> None:
        self.name = name  # flags.0?string
        self.phone = phone  # flags.1?string
        self.email = email  # flags.2?string
        self.shipping_address = shipping_address  # flags.3?PostAddress

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PaymentRequestedInfo":
        flags = Int.read(data)

        name = String.read(data) if flags & (1 << 0) else None
        phone = String.read(data) if flags & (1 << 1) else None
        email = String.read(data) if flags & (1 << 2) else None
        shipping_address = TLObject.read(data) if flags & (1 << 3) else None

        return PaymentRequestedInfo(name=name, phone=phone, email=email, shipping_address=shipping_address)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.name is not None else 0
        flags |= (1 << 1) if self.phone is not None else 0
        flags |= (1 << 2) if self.email is not None else 0
        flags |= (1 << 3) if self.shipping_address is not None else 0
        data.write(Int(flags))

        if self.name is not None:
            data.write(String(self.name))

        if self.phone is not None:
            data.write(String(self.phone))

        if self.email is not None:
            data.write(String(self.email))

        if self.shipping_address is not None:
            data.write(self.shipping_address.write())

        return data.getvalue()
