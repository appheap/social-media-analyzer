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


class ExportMessageLink(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0xe63fadeb``

    Parameters:
        channel: :obj:`InputChannel <pyrogram.raw.base.InputChannel>`
        id: ``int`` ``32-bit``
        grouped (optional): ``bool``
        thread (optional): ``bool``

    Returns:
        :obj:`ExportedMessageLink <pyrogram.raw.base.ExportedMessageLink>`
    """

    __slots__: List[str] = ["channel", "id", "grouped", "thread"]

    ID = 0xe63fadeb
    QUALNAME = "functions.channels.ExportMessageLink"

    def __init__(self, *, channel: "raw.base.InputChannel", id: int, grouped: Union[None, bool] = None,
                 thread: Union[None, bool] = None) -> None:
        self.channel = channel  # InputChannel
        self.id = id  # int
        self.grouped = grouped  # flags.0?true
        self.thread = thread  # flags.1?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ExportMessageLink":
        flags = Int.read(data)

        grouped = True if flags & (1 << 0) else False
        thread = True if flags & (1 << 1) else False
        channel = TLObject.read(data)

        id = Int.read(data)

        return ExportMessageLink(channel=channel, id=id, grouped=grouped, thread=thread)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.grouped else 0
        flags |= (1 << 1) if self.thread else 0
        data.write(Int(flags))

        data.write(self.channel.write())

        data.write(Int(self.id))

        return data.getvalue()
