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


class Password(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.account.Password`.

    Details:
        - Layer: ``117``
        - ID: ``0xad2641f8``

    Parameters:
        new_algo: :obj:`PasswordKdfAlgo <pyrogram.raw.base.PasswordKdfAlgo>`
        new_secure_algo: :obj:`SecurePasswordKdfAlgo <pyrogram.raw.base.SecurePasswordKdfAlgo>`
        secure_random: ``bytes``
        has_recovery (optional): ``bool``
        has_secure_values (optional): ``bool``
        has_password (optional): ``bool``
        current_algo (optional): :obj:`PasswordKdfAlgo <pyrogram.raw.base.PasswordKdfAlgo>`
        srp_B (optional): ``bytes``
        srp_id (optional): ``int`` ``64-bit``
        hint (optional): ``str``
        email_unconfirmed_pattern (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`account.GetPassword <pyrogram.raw.functions.account.GetPassword>`
    """

    __slots__: List[str] = ["new_algo", "new_secure_algo", "secure_random", "has_recovery", "has_secure_values",
                            "has_password", "current_algo", "srp_B", "srp_id", "hint", "email_unconfirmed_pattern"]

    ID = 0xad2641f8
    QUALNAME = "types.account.Password"

    def __init__(self, *, new_algo: "raw.base.PasswordKdfAlgo", new_secure_algo: "raw.base.SecurePasswordKdfAlgo",
                 secure_random: bytes, has_recovery: Union[None, bool] = None,
                 has_secure_values: Union[None, bool] = None, has_password: Union[None, bool] = None,
                 current_algo: "raw.base.PasswordKdfAlgo" = None, srp_B: Union[None, bytes] = None,
                 srp_id: Union[None, int] = None, hint: Union[None, str] = None,
                 email_unconfirmed_pattern: Union[None, str] = None) -> None:
        self.new_algo = new_algo  # PasswordKdfAlgo
        self.new_secure_algo = new_secure_algo  # SecurePasswordKdfAlgo
        self.secure_random = secure_random  # bytes
        self.has_recovery = has_recovery  # flags.0?true
        self.has_secure_values = has_secure_values  # flags.1?true
        self.has_password = has_password  # flags.2?true
        self.current_algo = current_algo  # flags.2?PasswordKdfAlgo
        self.srp_B = srp_B  # flags.2?bytes
        self.srp_id = srp_id  # flags.2?long
        self.hint = hint  # flags.3?string
        self.email_unconfirmed_pattern = email_unconfirmed_pattern  # flags.4?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Password":
        flags = Int.read(data)

        has_recovery = True if flags & (1 << 0) else False
        has_secure_values = True if flags & (1 << 1) else False
        has_password = True if flags & (1 << 2) else False
        current_algo = TLObject.read(data) if flags & (1 << 2) else None

        srp_B = Bytes.read(data) if flags & (1 << 2) else None
        srp_id = Long.read(data) if flags & (1 << 2) else None
        hint = String.read(data) if flags & (1 << 3) else None
        email_unconfirmed_pattern = String.read(data) if flags & (1 << 4) else None
        new_algo = TLObject.read(data)

        new_secure_algo = TLObject.read(data)

        secure_random = Bytes.read(data)

        return Password(new_algo=new_algo, new_secure_algo=new_secure_algo, secure_random=secure_random,
                        has_recovery=has_recovery, has_secure_values=has_secure_values, has_password=has_password,
                        current_algo=current_algo, srp_B=srp_B, srp_id=srp_id, hint=hint,
                        email_unconfirmed_pattern=email_unconfirmed_pattern)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.has_recovery is not None else 0
        flags |= (1 << 1) if self.has_secure_values is not None else 0
        flags |= (1 << 2) if self.has_password is not None else 0
        flags |= (1 << 2) if self.current_algo is not None else 0
        flags |= (1 << 2) if self.srp_B is not None else 0
        flags |= (1 << 2) if self.srp_id is not None else 0
        flags |= (1 << 3) if self.hint is not None else 0
        flags |= (1 << 4) if self.email_unconfirmed_pattern is not None else 0
        data.write(Int(flags))

        if self.current_algo is not None:
            data.write(self.current_algo.write())

        if self.srp_B is not None:
            data.write(Bytes(self.srp_B))

        if self.srp_id is not None:
            data.write(Long(self.srp_id))

        if self.hint is not None:
            data.write(String(self.hint))

        if self.email_unconfirmed_pattern is not None:
            data.write(String(self.email_unconfirmed_pattern))

        data.write(self.new_algo.write())

        data.write(self.new_secure_algo.write())

        data.write(Bytes(self.secure_random))

        return data.getvalue()
