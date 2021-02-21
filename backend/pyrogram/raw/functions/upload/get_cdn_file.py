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


class GetCdnFile(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x2000bcc3``

    Parameters:
        file_token: ``bytes``
        offset: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``

    Returns:
        :obj:`upload.CdnFile <pyrogram.raw.base.upload.CdnFile>`
    """

    __slots__: List[str] = ["file_token", "offset", "limit"]

    ID = 0x2000bcc3
    QUALNAME = "functions.upload.GetCdnFile"

    def __init__(self, *, file_token: bytes, offset: int, limit: int) -> None:
        self.file_token = file_token  # bytes
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetCdnFile":
        # No flags

        file_token = Bytes.read(data)

        offset = Int.read(data)

        limit = Int.read(data)

        return GetCdnFile(file_token=file_token, offset=offset, limit=limit)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Bytes(self.file_token))

        data.write(Int(self.offset))

        data.write(Int(self.limit))

        return data.getvalue()
