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


class InputMediaPhoto(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``123``
        - ID: ``0xb3ba0635``

    Parameters:
        id: :obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`
        ttl_seconds (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["id", "ttl_seconds"]

    ID = 0xb3ba0635
    QUALNAME = "types.InputMediaPhoto"

    def __init__(self, *, id: "raw.base.InputPhoto", ttl_seconds: Union[None, int] = None) -> None:
        self.id = id  # InputPhoto
        self.ttl_seconds = ttl_seconds  # flags.0?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputMediaPhoto":
        flags = Int.read(data)

        id = TLObject.read(data)

        ttl_seconds = Int.read(data) if flags & (1 << 0) else None
        return InputMediaPhoto(id=id, ttl_seconds=ttl_seconds)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ttl_seconds is not None else 0
        data.write(Int(flags))

        data.write(self.id.write())

        if self.ttl_seconds is not None:
            data.write(Int(self.ttl_seconds))

        return data.getvalue()
