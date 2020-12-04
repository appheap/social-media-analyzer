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


class PasswordSettings(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.account.PasswordSettings`.

    Details:
        - Layer: ``120``
        - ID: ``0x9a5c33e5``

    Parameters:
        email (optional): ``str``
        secure_settings (optional): :obj:`SecureSecretSettings <pyrogram.raw.base.SecureSecretSettings>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`account.GetPasswordSettings <pyrogram.raw.functions.account.GetPasswordSettings>`
    """

    __slots__: List[str] = ["email", "secure_settings"]

    ID = 0x9a5c33e5
    QUALNAME = "types.account.PasswordSettings"

    def __init__(self, *, email: Union[None, str] = None,
                 secure_settings: "raw.base.SecureSecretSettings" = None) -> None:
        self.email = email  # flags.0?string
        self.secure_settings = secure_settings  # flags.1?SecureSecretSettings

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PasswordSettings":
        flags = Int.read(data)

        email = String.read(data) if flags & (1 << 0) else None
        secure_settings = TLObject.read(data) if flags & (1 << 1) else None

        return PasswordSettings(email=email, secure_settings=secure_settings)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.email is not None else 0
        flags |= (1 << 1) if self.secure_settings is not None else 0
        data.write(Int(flags))

        if self.email is not None:
            data.write(String(self.email))

        if self.secure_settings is not None:
            data.write(self.secure_settings.write())

        return data.getvalue()
