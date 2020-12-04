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


class FileCdnRedirect(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.upload.File`.

    Details:
        - Layer: ``120``
        - ID: ``0xf18cda44``

    Parameters:
        dc_id: ``int`` ``32-bit``
        file_token: ``bytes``
        encryption_key: ``bytes``
        encryption_iv: ``bytes``
        file_hashes: List of :obj:`FileHash <pyrogram.raw.base.FileHash>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`upload.GetFile <pyrogram.raw.functions.upload.GetFile>`
    """

    __slots__: List[str] = ["dc_id", "file_token", "encryption_key", "encryption_iv", "file_hashes"]

    ID = 0xf18cda44
    QUALNAME = "types.upload.FileCdnRedirect"

    def __init__(self, *, dc_id: int, file_token: bytes, encryption_key: bytes, encryption_iv: bytes,
                 file_hashes: List["raw.base.FileHash"]) -> None:
        self.dc_id = dc_id  # int
        self.file_token = file_token  # bytes
        self.encryption_key = encryption_key  # bytes
        self.encryption_iv = encryption_iv  # bytes
        self.file_hashes = file_hashes  # Vector<FileHash>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "FileCdnRedirect":
        # No flags

        dc_id = Int.read(data)

        file_token = Bytes.read(data)

        encryption_key = Bytes.read(data)

        encryption_iv = Bytes.read(data)

        file_hashes = TLObject.read(data)

        return FileCdnRedirect(dc_id=dc_id, file_token=file_token, encryption_key=encryption_key,
                               encryption_iv=encryption_iv, file_hashes=file_hashes)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.dc_id))

        data.write(Bytes(self.file_token))

        data.write(Bytes(self.encryption_key))

        data.write(Bytes(self.encryption_iv))

        data.write(Vector(self.file_hashes))

        return data.getvalue()
