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


class SecureSecretSettings(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.SecureSecretSettings`.

    Details:
        - Layer: ``120``
        - ID: ``0x1527bcac``

    Parameters:
        secure_algo: :obj:`SecurePasswordKdfAlgo <pyrogram.raw.base.SecurePasswordKdfAlgo>`
        secure_secret: ``bytes``
        secure_secret_id: ``int`` ``64-bit``
    """

    __slots__: List[str] = ["secure_algo", "secure_secret", "secure_secret_id"]

    ID = 0x1527bcac
    QUALNAME = "types.SecureSecretSettings"

    def __init__(self, *, secure_algo: "raw.base.SecurePasswordKdfAlgo", secure_secret: bytes,
                 secure_secret_id: int) -> None:
        self.secure_algo = secure_algo  # SecurePasswordKdfAlgo
        self.secure_secret = secure_secret  # bytes
        self.secure_secret_id = secure_secret_id  # long

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SecureSecretSettings":
        # No flags

        secure_algo = TLObject.read(data)

        secure_secret = Bytes.read(data)

        secure_secret_id = Long.read(data)

        return SecureSecretSettings(secure_algo=secure_algo, secure_secret=secure_secret,
                                    secure_secret_id=secure_secret_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.secure_algo.write())

        data.write(Bytes(self.secure_secret))

        data.write(Long(self.secure_secret_id))

        return data.getvalue()
