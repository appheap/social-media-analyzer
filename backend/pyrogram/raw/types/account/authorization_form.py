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


class AuthorizationForm(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.account.AuthorizationForm`.

    Details:
        - Layer: ``123``
        - ID: ``0xad2e1cd8``

    Parameters:
        required_types: List of :obj:`SecureRequiredType <pyrogram.raw.base.SecureRequiredType>`
        values: List of :obj:`SecureValue <pyrogram.raw.base.SecureValue>`
        errors: List of :obj:`SecureValueError <pyrogram.raw.base.SecureValueError>`
        users: List of :obj:`User <pyrogram.raw.base.User>`
        privacy_policy_url (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`account.GetAuthorizationForm <pyrogram.raw.functions.account.GetAuthorizationForm>`
    """

    __slots__: List[str] = ["required_types", "values", "errors", "users", "privacy_policy_url"]

    ID = 0xad2e1cd8
    QUALNAME = "types.account.AuthorizationForm"

    def __init__(self, *, required_types: List["raw.base.SecureRequiredType"], values: List["raw.base.SecureValue"],
                 errors: List["raw.base.SecureValueError"], users: List["raw.base.User"],
                 privacy_policy_url: Union[None, str] = None) -> None:
        self.required_types = required_types  # Vector<SecureRequiredType>
        self.values = values  # Vector<SecureValue>
        self.errors = errors  # Vector<SecureValueError>
        self.users = users  # Vector<User>
        self.privacy_policy_url = privacy_policy_url  # flags.0?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "AuthorizationForm":
        flags = Int.read(data)

        required_types = TLObject.read(data)

        values = TLObject.read(data)

        errors = TLObject.read(data)

        users = TLObject.read(data)

        privacy_policy_url = String.read(data) if flags & (1 << 0) else None
        return AuthorizationForm(required_types=required_types, values=values, errors=errors, users=users,
                                 privacy_policy_url=privacy_policy_url)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.privacy_policy_url is not None else 0
        data.write(Int(flags))

        data.write(Vector(self.required_types))

        data.write(Vector(self.values))

        data.write(Vector(self.errors))

        data.write(Vector(self.users))

        if self.privacy_policy_url is not None:
            data.write(String(self.privacy_policy_url))

        return data.getvalue()
