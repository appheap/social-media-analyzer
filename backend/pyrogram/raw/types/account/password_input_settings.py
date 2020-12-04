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


class PasswordInputSettings(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.account.PasswordInputSettings`.

    Details:
        - Layer: ``120``
        - ID: ``0xc23727c9``

    Parameters:
        new_algo (optional): :obj:`PasswordKdfAlgo <pyrogram.raw.base.PasswordKdfAlgo>`
        new_password_hash (optional): ``bytes``
        hint (optional): ``str``
        email (optional): ``str``
        new_secure_settings (optional): :obj:`SecureSecretSettings <pyrogram.raw.base.SecureSecretSettings>`
    """

    __slots__: List[str] = ["new_algo", "new_password_hash", "hint", "email", "new_secure_settings"]

    ID = 0xc23727c9
    QUALNAME = "types.account.PasswordInputSettings"

    def __init__(self, *, new_algo: "raw.base.PasswordKdfAlgo" = None, new_password_hash: Union[None, bytes] = None,
                 hint: Union[None, str] = None, email: Union[None, str] = None,
                 new_secure_settings: "raw.base.SecureSecretSettings" = None) -> None:
        self.new_algo = new_algo  # flags.0?PasswordKdfAlgo
        self.new_password_hash = new_password_hash  # flags.0?bytes
        self.hint = hint  # flags.0?string
        self.email = email  # flags.1?string
        self.new_secure_settings = new_secure_settings  # flags.2?SecureSecretSettings

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PasswordInputSettings":
        flags = Int.read(data)

        new_algo = TLObject.read(data) if flags & (1 << 0) else None

        new_password_hash = Bytes.read(data) if flags & (1 << 0) else None
        hint = String.read(data) if flags & (1 << 0) else None
        email = String.read(data) if flags & (1 << 1) else None
        new_secure_settings = TLObject.read(data) if flags & (1 << 2) else None

        return PasswordInputSettings(new_algo=new_algo, new_password_hash=new_password_hash, hint=hint, email=email,
                                     new_secure_settings=new_secure_settings)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.new_algo is not None else 0
        flags |= (1 << 0) if self.new_password_hash is not None else 0
        flags |= (1 << 0) if self.hint is not None else 0
        flags |= (1 << 1) if self.email is not None else 0
        flags |= (1 << 2) if self.new_secure_settings is not None else 0
        data.write(Int(flags))

        if self.new_algo is not None:
            data.write(self.new_algo.write())

        if self.new_password_hash is not None:
            data.write(Bytes(self.new_password_hash))

        if self.hint is not None:
            data.write(String(self.hint))

        if self.email is not None:
            data.write(String(self.email))

        if self.new_secure_settings is not None:
            data.write(self.new_secure_settings.write())

        return data.getvalue()
