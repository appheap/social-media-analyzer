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


class SaveSecureValue(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x899fe31d``

    Parameters:
        value: :obj:`InputSecureValue <pyrogram.raw.base.InputSecureValue>`
        secure_secret_id: ``int`` ``64-bit``

    Returns:
        :obj:`SecureValue <pyrogram.raw.base.SecureValue>`
    """

    __slots__: List[str] = ["value", "secure_secret_id"]

    ID = 0x899fe31d
    QUALNAME = "functions.account.SaveSecureValue"

    def __init__(self, *, value: "raw.base.InputSecureValue", secure_secret_id: int) -> None:
        self.value = value  # InputSecureValue
        self.secure_secret_id = secure_secret_id  # long

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SaveSecureValue":
        # No flags

        value = TLObject.read(data)

        secure_secret_id = Long.read(data)

        return SaveSecureValue(value=value, secure_secret_id=secure_secret_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.value.write())

        data.write(Long(self.secure_secret_id))

        return data.getvalue()
