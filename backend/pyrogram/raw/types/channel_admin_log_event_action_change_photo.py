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


class ChannelAdminLogEventActionChangePhoto(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``120``
        - ID: ``0x434bd2af``

    Parameters:
        prev_photo: :obj:`Photo <pyrogram.raw.base.Photo>`
        new_photo: :obj:`Photo <pyrogram.raw.base.Photo>`
    """

    __slots__: List[str] = ["prev_photo", "new_photo"]

    ID = 0x434bd2af
    QUALNAME = "types.ChannelAdminLogEventActionChangePhoto"

    def __init__(self, *, prev_photo: "raw.base.Photo", new_photo: "raw.base.Photo") -> None:
        self.prev_photo = prev_photo  # Photo
        self.new_photo = new_photo  # Photo

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangePhoto":
        # No flags

        prev_photo = TLObject.read(data)

        new_photo = TLObject.read(data)

        return ChannelAdminLogEventActionChangePhoto(prev_photo=prev_photo, new_photo=new_photo)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.prev_photo.write())

        data.write(self.new_photo.write())

        return data.getvalue()
