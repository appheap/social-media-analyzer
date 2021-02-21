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


class FileHash(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.FileHash`.

    Details:
        - Layer: ``123``
        - ID: ``0x6242c773``

    Parameters:
        offset: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``
        hash: ``bytes``

    See Also:
        This object can be returned by 3 methods:

        .. hlist::
            :columns: 2

            - :obj:`upload.ReuploadCdnFile <pyrogram.raw.functions.upload.ReuploadCdnFile>`
            - :obj:`upload.GetCdnFileHashes <pyrogram.raw.functions.upload.GetCdnFileHashes>`
            - :obj:`upload.GetFileHashes <pyrogram.raw.functions.upload.GetFileHashes>`
    """

    __slots__: List[str] = ["offset", "limit", "hash"]

    ID = 0x6242c773
    QUALNAME = "types.FileHash"

    def __init__(self, *, offset: int, limit: int, hash: bytes) -> None:
        self.offset = offset  # int
        self.limit = limit  # int
        self.hash = hash  # bytes

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "FileHash":
        # No flags

        offset = Int.read(data)

        limit = Int.read(data)

        hash = Bytes.read(data)

        return FileHash(offset=offset, limit=limit, hash=hash)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.offset))

        data.write(Int(self.limit))

        data.write(Bytes(self.hash))

        return data.getvalue()
