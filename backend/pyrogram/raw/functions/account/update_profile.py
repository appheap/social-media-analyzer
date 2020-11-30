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


class UpdateProfile(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0x78515775``

    Parameters:
        first_name (optional): ``str``
        last_name (optional): ``str``
        about (optional): ``str``

    Returns:
        :obj:`User <pyrogram.raw.base.User>`
    """

    __slots__: List[str] = ["first_name", "last_name", "about"]

    ID = 0x78515775
    QUALNAME = "functions.account.UpdateProfile"

    def __init__(self, *, first_name: Union[None, str] = None, last_name: Union[None, str] = None,
                 about: Union[None, str] = None) -> None:
        self.first_name = first_name  # flags.0?string
        self.last_name = last_name  # flags.1?string
        self.about = about  # flags.2?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateProfile":
        flags = Int.read(data)

        first_name = String.read(data) if flags & (1 << 0) else None
        last_name = String.read(data) if flags & (1 << 1) else None
        about = String.read(data) if flags & (1 << 2) else None
        return UpdateProfile(first_name=first_name, last_name=last_name, about=about)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.first_name is not None else 0
        flags |= (1 << 1) if self.last_name is not None else 0
        flags |= (1 << 2) if self.about is not None else 0
        data.write(Int(flags))

        if self.first_name is not None:
            data.write(String(self.first_name))

        if self.last_name is not None:
            data.write(String(self.last_name))

        if self.about is not None:
            data.write(String(self.about))

        return data.getvalue()
