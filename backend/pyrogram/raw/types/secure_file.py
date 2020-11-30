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


class SecureFile(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.SecureFile`.

    Details:
        - Layer: ``117``
        - ID: ``0xe0277a62``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        size: ``int`` ``32-bit``
        dc_id: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        file_hash: ``bytes``
        secret: ``bytes``
    """

    __slots__: List[str] = ["id", "access_hash", "size", "dc_id", "date", "file_hash", "secret"]

    ID = 0xe0277a62
    QUALNAME = "types.SecureFile"

    def __init__(self, *, id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: bytes,
                 secret: bytes) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.size = size  # int
        self.dc_id = dc_id  # int
        self.date = date  # int
        self.file_hash = file_hash  # bytes
        self.secret = secret  # bytes

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SecureFile":
        # No flags

        id = Long.read(data)

        access_hash = Long.read(data)

        size = Int.read(data)

        dc_id = Int.read(data)

        date = Int.read(data)

        file_hash = Bytes.read(data)

        secret = Bytes.read(data)

        return SecureFile(id=id, access_hash=access_hash, size=size, dc_id=dc_id, date=date, file_hash=file_hash,
                          secret=secret)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Long(self.id))

        data.write(Long(self.access_hash))

        data.write(Int(self.size))

        data.write(Int(self.dc_id))

        data.write(Int(self.date))

        data.write(Bytes(self.file_hash))

        data.write(Bytes(self.secret))

        return data.getvalue()
