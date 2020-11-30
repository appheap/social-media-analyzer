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


class PhotosSlice(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.photos.Photos`.

    Details:
        - Layer: ``117``
        - ID: ``0x15051f54``

    Parameters:
        count: ``int`` ``32-bit``
        photos: List of :obj:`Photo <pyrogram.raw.base.Photo>`
        users: List of :obj:`User <pyrogram.raw.base.User>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`photos.GetUserPhotos <pyrogram.raw.functions.photos.GetUserPhotos>`
    """

    __slots__: List[str] = ["count", "photos", "users"]

    ID = 0x15051f54
    QUALNAME = "types.photos.PhotosSlice"

    def __init__(self, *, count: int, photos: List["raw.base.Photo"], users: List["raw.base.User"]) -> None:
        self.count = count  # int
        self.photos = photos  # Vector<Photo>
        self.users = users  # Vector<User>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PhotosSlice":
        # No flags

        count = Int.read(data)

        photos = TLObject.read(data)

        users = TLObject.read(data)

        return PhotosSlice(count=count, photos=photos, users=users)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.count))

        data.write(Vector(self.photos))

        data.write(Vector(self.users))

        return data.getvalue()
