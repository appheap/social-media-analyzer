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


class MessageEditData(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.MessageEditData`.

    Details:
        - Layer: ``123``
        - ID: ``0x26b5dde6``

    Parameters:
        caption (optional): ``bool``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetMessageEditData <pyrogram.raw.functions.messages.GetMessageEditData>`
    """

    __slots__: List[str] = ["caption"]

    ID = 0x26b5dde6
    QUALNAME = "types.messages.MessageEditData"

    def __init__(self, *, caption: Union[None, bool] = None) -> None:
        self.caption = caption  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MessageEditData":
        flags = Int.read(data)

        caption = True if flags & (1 << 0) else False
        return MessageEditData(caption=caption)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.caption else 0
        data.write(Int(flags))

        return data.getvalue()
