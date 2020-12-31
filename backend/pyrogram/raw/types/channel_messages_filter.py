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


class ChannelMessagesFilter(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChannelMessagesFilter`.

    Details:
        - Layer: ``122``
        - ID: ``0xcd77d957``

    Parameters:
        ranges: List of :obj:`MessageRange <pyrogram.raw.base.MessageRange>`
        exclude_new_messages (optional): ``bool``
    """

    __slots__: List[str] = ["ranges", "exclude_new_messages"]

    ID = 0xcd77d957
    QUALNAME = "types.ChannelMessagesFilter"

    def __init__(self, *, ranges: List["raw.base.MessageRange"],
                 exclude_new_messages: Union[None, bool] = None) -> None:
        self.ranges = ranges  # Vector<MessageRange>
        self.exclude_new_messages = exclude_new_messages  # flags.1?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChannelMessagesFilter":
        flags = Int.read(data)

        exclude_new_messages = True if flags & (1 << 1) else False
        ranges = TLObject.read(data)

        return ChannelMessagesFilter(ranges=ranges, exclude_new_messages=exclude_new_messages)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.exclude_new_messages else 0
        data.write(Int(flags))

        data.write(Vector(self.ranges))

        return data.getvalue()
