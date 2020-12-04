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


class GetArchivedStickers(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0x57f17692``

    Parameters:
        offset_id: ``int`` ``64-bit``
        limit: ``int`` ``32-bit``
        masks (optional): ``bool``

    Returns:
        :obj:`messages.ArchivedStickers <pyrogram.raw.base.messages.ArchivedStickers>`
    """

    __slots__: List[str] = ["offset_id", "limit", "masks"]

    ID = 0x57f17692
    QUALNAME = "functions.messages.GetArchivedStickers"

    def __init__(self, *, offset_id: int, limit: int, masks: Union[None, bool] = None) -> None:
        self.offset_id = offset_id  # long
        self.limit = limit  # int
        self.masks = masks  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetArchivedStickers":
        flags = Int.read(data)

        masks = True if flags & (1 << 0) else False
        offset_id = Long.read(data)

        limit = Int.read(data)

        return GetArchivedStickers(offset_id=offset_id, limit=limit, masks=masks)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.masks is not None else 0
        data.write(Int(flags))

        data.write(Long(self.offset_id))

        data.write(Int(self.limit))

        return data.getvalue()
