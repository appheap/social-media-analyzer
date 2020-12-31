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


class GetFile(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0xb15a9afc``

    Parameters:
        location: :obj:`InputFileLocation <pyrogram.raw.base.InputFileLocation>`
        offset: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``
        precise (optional): ``bool``
        cdn_supported (optional): ``bool``

    Returns:
        :obj:`upload.File <pyrogram.raw.base.upload.File>`
    """

    __slots__: List[str] = ["location", "offset", "limit", "precise", "cdn_supported"]

    ID = 0xb15a9afc
    QUALNAME = "functions.upload.GetFile"

    def __init__(self, *, location: "raw.base.InputFileLocation", offset: int, limit: int,
                 precise: Union[None, bool] = None, cdn_supported: Union[None, bool] = None) -> None:
        self.location = location  # InputFileLocation
        self.offset = offset  # int
        self.limit = limit  # int
        self.precise = precise  # flags.0?true
        self.cdn_supported = cdn_supported  # flags.1?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetFile":
        flags = Int.read(data)

        precise = True if flags & (1 << 0) else False
        cdn_supported = True if flags & (1 << 1) else False
        location = TLObject.read(data)

        offset = Int.read(data)

        limit = Int.read(data)

        return GetFile(location=location, offset=offset, limit=limit, precise=precise, cdn_supported=cdn_supported)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.precise else 0
        flags |= (1 << 1) if self.cdn_supported else 0
        data.write(Int(flags))

        data.write(self.location.write())

        data.write(Int(self.offset))

        data.write(Int(self.limit))

        return data.getvalue()
