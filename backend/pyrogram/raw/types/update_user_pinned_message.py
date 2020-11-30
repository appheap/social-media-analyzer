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


class UpdateUserPinnedMessage(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``117``
        - ID: ``0x4c43da18``

    Parameters:
        user_id: ``int`` ``32-bit``
        id: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["user_id", "id"]

    ID = 0x4c43da18
    QUALNAME = "types.UpdateUserPinnedMessage"

    def __init__(self, *, user_id: int, id: int) -> None:
        self.user_id = user_id  # int
        self.id = id  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateUserPinnedMessage":
        # No flags

        user_id = Int.read(data)

        id = Int.read(data)

        return UpdateUserPinnedMessage(user_id=user_id, id=id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.user_id))

        data.write(Int(self.id))

        return data.getvalue()
