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


class Photo(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Photo`.

    Details:
        - Layer: ``122``
        - ID: ``0xfb197a65``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        file_reference: ``bytes``
        date: ``int`` ``32-bit``
        sizes: List of :obj:`PhotoSize <pyrogram.raw.base.PhotoSize>`
        dc_id: ``int`` ``32-bit``
        has_stickers (optional): ``bool``
        video_sizes (optional): List of :obj:`VideoSize <pyrogram.raw.base.VideoSize>`
    """

    __slots__: List[str] = ["id", "access_hash", "file_reference", "date", "sizes", "dc_id", "has_stickers",
                            "video_sizes"]

    ID = 0xfb197a65
    QUALNAME = "types.Photo"

    def __init__(self, *, id: int, access_hash: int, file_reference: bytes, date: int,
                 sizes: List["raw.base.PhotoSize"], dc_id: int, has_stickers: Union[None, bool] = None,
                 video_sizes: Union[None, List["raw.base.VideoSize"]] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.file_reference = file_reference  # bytes
        self.date = date  # int
        self.sizes = sizes  # Vector<PhotoSize>
        self.dc_id = dc_id  # int
        self.has_stickers = has_stickers  # flags.0?true
        self.video_sizes = video_sizes  # flags.1?Vector<VideoSize>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Photo":
        flags = Int.read(data)

        has_stickers = True if flags & (1 << 0) else False
        id = Long.read(data)

        access_hash = Long.read(data)

        file_reference = Bytes.read(data)

        date = Int.read(data)

        sizes = TLObject.read(data)

        video_sizes = TLObject.read(data) if flags & (1 << 1) else []

        dc_id = Int.read(data)

        return Photo(id=id, access_hash=access_hash, file_reference=file_reference, date=date, sizes=sizes, dc_id=dc_id,
                     has_stickers=has_stickers, video_sizes=video_sizes)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.has_stickers else 0
        flags |= (1 << 1) if self.video_sizes is not None else 0
        data.write(Int(flags))

        data.write(Long(self.id))

        data.write(Long(self.access_hash))

        data.write(Bytes(self.file_reference))

        data.write(Int(self.date))

        data.write(Vector(self.sizes))

        if self.video_sizes is not None:
            data.write(Vector(self.video_sizes))

        data.write(Int(self.dc_id))

        return data.getvalue()
