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


class AcceptAuthorization(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0xe7027c94``

    Parameters:
        bot_id: ``int`` ``32-bit``
        scope: ``str``
        public_key: ``str``
        value_hashes: List of :obj:`SecureValueHash <pyrogram.raw.base.SecureValueHash>`
        credentials: :obj:`SecureCredentialsEncrypted <pyrogram.raw.base.SecureCredentialsEncrypted>`

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["bot_id", "scope", "public_key", "value_hashes", "credentials"]

    ID = 0xe7027c94
    QUALNAME = "functions.account.AcceptAuthorization"

    def __init__(self, *, bot_id: int, scope: str, public_key: str, value_hashes: List["raw.base.SecureValueHash"],
                 credentials: "raw.base.SecureCredentialsEncrypted") -> None:
        self.bot_id = bot_id  # int
        self.scope = scope  # string
        self.public_key = public_key  # string
        self.value_hashes = value_hashes  # Vector<SecureValueHash>
        self.credentials = credentials  # SecureCredentialsEncrypted

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "AcceptAuthorization":
        # No flags

        bot_id = Int.read(data)

        scope = String.read(data)

        public_key = String.read(data)

        value_hashes = TLObject.read(data)

        credentials = TLObject.read(data)

        return AcceptAuthorization(bot_id=bot_id, scope=scope, public_key=public_key, value_hashes=value_hashes,
                                   credentials=credentials)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.bot_id))

        data.write(String(self.scope))

        data.write(String(self.public_key))

        data.write(Vector(self.value_hashes))

        data.write(self.credentials.write())

        return data.getvalue()
