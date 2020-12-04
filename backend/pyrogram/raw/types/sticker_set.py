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


class StickerSet(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.StickerSet`.

    Details:
        - Layer: ``120``
        - ID: ``0xeeb46f27``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        title: ``str``
        short_name: ``str``
        count: ``int`` ``32-bit``
        hash: ``int`` ``32-bit``
        archived (optional): ``bool``
        official (optional): ``bool``
        masks (optional): ``bool``
        animated (optional): ``bool``
        installed_date (optional): ``int`` ``32-bit``
        thumb (optional): :obj:`PhotoSize <pyrogram.raw.base.PhotoSize>`
        thumb_dc_id (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["id", "access_hash", "title", "short_name", "count", "hash", "archived", "official",
                            "masks", "animated", "installed_date", "thumb", "thumb_dc_id"]

    ID = 0xeeb46f27
    QUALNAME = "types.StickerSet"

    def __init__(self, *, id: int, access_hash: int, title: str, short_name: str, count: int, hash: int,
                 archived: Union[None, bool] = None, official: Union[None, bool] = None,
                 masks: Union[None, bool] = None, animated: Union[None, bool] = None,
                 installed_date: Union[None, int] = None, thumb: "raw.base.PhotoSize" = None,
                 thumb_dc_id: Union[None, int] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.title = title  # string
        self.short_name = short_name  # string
        self.count = count  # int
        self.hash = hash  # int
        self.archived = archived  # flags.1?true
        self.official = official  # flags.2?true
        self.masks = masks  # flags.3?true
        self.animated = animated  # flags.5?true
        self.installed_date = installed_date  # flags.0?int
        self.thumb = thumb  # flags.4?PhotoSize
        self.thumb_dc_id = thumb_dc_id  # flags.4?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StickerSet":
        flags = Int.read(data)

        archived = True if flags & (1 << 1) else False
        official = True if flags & (1 << 2) else False
        masks = True if flags & (1 << 3) else False
        animated = True if flags & (1 << 5) else False
        installed_date = Int.read(data) if flags & (1 << 0) else None
        id = Long.read(data)

        access_hash = Long.read(data)

        title = String.read(data)

        short_name = String.read(data)

        thumb = TLObject.read(data) if flags & (1 << 4) else None

        thumb_dc_id = Int.read(data) if flags & (1 << 4) else None
        count = Int.read(data)

        hash = Int.read(data)

        return StickerSet(id=id, access_hash=access_hash, title=title, short_name=short_name, count=count, hash=hash,
                          archived=archived, official=official, masks=masks, animated=animated,
                          installed_date=installed_date, thumb=thumb, thumb_dc_id=thumb_dc_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.archived is not None else 0
        flags |= (1 << 2) if self.official is not None else 0
        flags |= (1 << 3) if self.masks is not None else 0
        flags |= (1 << 5) if self.animated is not None else 0
        flags |= (1 << 0) if self.installed_date is not None else 0
        flags |= (1 << 4) if self.thumb is not None else 0
        flags |= (1 << 4) if self.thumb_dc_id is not None else 0
        data.write(Int(flags))

        if self.installed_date is not None:
            data.write(Int(self.installed_date))

        data.write(Long(self.id))

        data.write(Long(self.access_hash))

        data.write(String(self.title))

        data.write(String(self.short_name))

        if self.thumb is not None:
            data.write(self.thumb.write())

        if self.thumb_dc_id is not None:
            data.write(Int(self.thumb_dc_id))

        data.write(Int(self.count))

        data.write(Int(self.hash))

        return data.getvalue()
