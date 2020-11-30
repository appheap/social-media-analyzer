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


class RegisterDevice(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0x68976c6f``

    Parameters:
        token_type: ``int`` ``32-bit``
        token: ``str``
        app_sandbox: ``bool``
        secret: ``bytes``
        other_uids: List of ``int`` ``32-bit``
        no_muted (optional): ``bool``

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["token_type", "token", "app_sandbox", "secret", "other_uids", "no_muted"]

    ID = 0x68976c6f
    QUALNAME = "functions.account.RegisterDevice"

    def __init__(self, *, token_type: int, token: str, app_sandbox: bool, secret: bytes, other_uids: List[int],
                 no_muted: Union[None, bool] = None) -> None:
        self.token_type = token_type  # int
        self.token = token  # string
        self.app_sandbox = app_sandbox  # Bool
        self.secret = secret  # bytes
        self.other_uids = other_uids  # Vector<int>
        self.no_muted = no_muted  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "RegisterDevice":
        flags = Int.read(data)

        no_muted = True if flags & (1 << 0) else False
        token_type = Int.read(data)

        token = String.read(data)

        app_sandbox = Bool.read(data)

        secret = Bytes.read(data)

        other_uids = TLObject.read(data, Int)

        return RegisterDevice(token_type=token_type, token=token, app_sandbox=app_sandbox, secret=secret,
                              other_uids=other_uids, no_muted=no_muted)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.no_muted is not None else 0
        data.write(Int(flags))

        data.write(Int(self.token_type))

        data.write(String(self.token))

        data.write(Bool(self.app_sandbox))

        data.write(Bytes(self.secret))

        data.write(Vector(self.other_uids, Int))

        return data.getvalue()
