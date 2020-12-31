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


class UserProfilePhoto(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.UserProfilePhoto`.

    Details:
        - Layer: ``122``
        - ID: ``0x69d3ab26``

    Parameters:
        photo_id: ``int`` ``64-bit``
        photo_small: :obj:`FileLocation <pyrogram.raw.base.FileLocation>`
        photo_big: :obj:`FileLocation <pyrogram.raw.base.FileLocation>`
        dc_id: ``int`` ``32-bit``
        has_video (optional): ``bool``
    """

    __slots__: List[str] = ["photo_id", "photo_small", "photo_big", "dc_id", "has_video"]

    ID = 0x69d3ab26
    QUALNAME = "types.UserProfilePhoto"

    def __init__(self, *, photo_id: int, photo_small: "raw.base.FileLocation", photo_big: "raw.base.FileLocation",
                 dc_id: int, has_video: Union[None, bool] = None) -> None:
        self.photo_id = photo_id  # long
        self.photo_small = photo_small  # FileLocation
        self.photo_big = photo_big  # FileLocation
        self.dc_id = dc_id  # int
        self.has_video = has_video  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UserProfilePhoto":
        flags = Int.read(data)

        has_video = True if flags & (1 << 0) else False
        photo_id = Long.read(data)

        photo_small = TLObject.read(data)

        photo_big = TLObject.read(data)

        dc_id = Int.read(data)

        return UserProfilePhoto(photo_id=photo_id, photo_small=photo_small, photo_big=photo_big, dc_id=dc_id,
                                has_video=has_video)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.has_video else 0
        data.write(Int(flags))

        data.write(Long(self.photo_id))

        data.write(self.photo_small.write())

        data.write(self.photo_big.write())

        data.write(Int(self.dc_id))

        return data.getvalue()
