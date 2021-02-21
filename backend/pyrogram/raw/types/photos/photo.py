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


class Photo(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.photos.Photo`.

    Details:
        - Layer: ``123``
        - ID: ``0x20212ca8``

    Parameters:
        photo: :obj:`Photo <pyrogram.raw.base.Photo>`
        users: List of :obj:`User <pyrogram.raw.base.User>`

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`photos.UpdateProfilePhoto <pyrogram.raw.functions.photos.UpdateProfilePhoto>`
            - :obj:`photos.UploadProfilePhoto <pyrogram.raw.functions.photos.UploadProfilePhoto>`
    """

    __slots__: List[str] = ["photo", "users"]

    ID = 0x20212ca8
    QUALNAME = "types.photos.Photo"

    def __init__(self, *, photo: "raw.base.Photo", users: List["raw.base.User"]) -> None:
        self.photo = photo  # Photo
        self.users = users  # Vector<User>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Photo":
        # No flags

        photo = TLObject.read(data)

        users = TLObject.read(data)

        return Photo(photo=photo, users=users)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.photo.write())

        data.write(Vector(self.users))

        return data.getvalue()
