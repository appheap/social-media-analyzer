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


class InputPaymentCredentialsAndroidPay(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputPaymentCredentials`.

    Details:
        - Layer: ``122``
        - ID: ``0xca05d50e``

    Parameters:
        payment_token: :obj:`DataJSON <pyrogram.raw.base.DataJSON>`
        google_transaction_id: ``str``
    """

    __slots__: List[str] = ["payment_token", "google_transaction_id"]

    ID = 0xca05d50e
    QUALNAME = "types.InputPaymentCredentialsAndroidPay"

    def __init__(self, *, payment_token: "raw.base.DataJSON", google_transaction_id: str) -> None:
        self.payment_token = payment_token  # DataJSON
        self.google_transaction_id = google_transaction_id  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputPaymentCredentialsAndroidPay":
        # No flags

        payment_token = TLObject.read(data)

        google_transaction_id = String.read(data)

        return InputPaymentCredentialsAndroidPay(payment_token=payment_token,
                                                 google_transaction_id=google_transaction_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.payment_token.write())

        data.write(String(self.google_transaction_id))

        return data.getvalue()
