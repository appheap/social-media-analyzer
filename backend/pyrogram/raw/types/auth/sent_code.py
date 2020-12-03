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


class SentCode(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.auth.SentCode`.

    Details:
        - Layer: ``121``
        - ID: ``0x5e002502``

    Parameters:
        type: :obj:`auth.SentCodeType <pyrogram.raw.base.auth.SentCodeType>`
        phone_code_hash: ``str``
        next_type (optional): :obj:`auth.CodeType <pyrogram.raw.base.auth.CodeType>`
        timeout (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by 5 methods:

        .. hlist::
            :columns: 2

            - :obj:`auth.SendCode <pyrogram.raw.functions.auth.SendCode>`
            - :obj:`auth.ResendCode <pyrogram.raw.functions.auth.ResendCode>`
            - :obj:`account.SendChangePhoneCode <pyrogram.raw.functions.account.SendChangePhoneCode>`
            - :obj:`account.SendConfirmPhoneCode <pyrogram.raw.functions.account.SendConfirmPhoneCode>`
            - :obj:`account.SendVerifyPhoneCode <pyrogram.raw.functions.account.SendVerifyPhoneCode>`
    """

    __slots__: List[str] = ["type", "phone_code_hash", "next_type", "timeout"]

    ID = 0x5e002502
    QUALNAME = "types.auth.SentCode"

    def __init__(self, *, type: "raw.base.auth.SentCodeType", phone_code_hash: str,
                 next_type: "raw.base.auth.CodeType" = None, timeout: Union[None, int] = None) -> None:
        self.type = type  # auth.SentCodeType
        self.phone_code_hash = phone_code_hash  # string
        self.next_type = next_type  # flags.1?auth.CodeType
        self.timeout = timeout  # flags.2?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SentCode":
        flags = Int.read(data)

        type = TLObject.read(data)

        phone_code_hash = String.read(data)

        next_type = TLObject.read(data) if flags & (1 << 1) else None

        timeout = Int.read(data) if flags & (1 << 2) else None
        return SentCode(type=type, phone_code_hash=phone_code_hash, next_type=next_type, timeout=timeout)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.next_type is not None else 0
        flags |= (1 << 2) if self.timeout is not None else 0
        data.write(Int(flags))

        data.write(self.type.write())

        data.write(String(self.phone_code_hash))

        if self.next_type is not None:
            data.write(self.next_type.write())

        if self.timeout is not None:
            data.write(Int(self.timeout))

        return data.getvalue()
