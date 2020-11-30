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


class DocumentAttributeVideo(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``117``
        - ID: ``0xef02ce6``

    Parameters:
        duration: ``int`` ``32-bit``
        w: ``int`` ``32-bit``
        h: ``int`` ``32-bit``
        round_message (optional): ``bool``
        supports_streaming (optional): ``bool``
    """

    __slots__: List[str] = ["duration", "w", "h", "round_message", "supports_streaming"]

    ID = 0xef02ce6
    QUALNAME = "types.DocumentAttributeVideo"

    def __init__(self, *, duration: int, w: int, h: int, round_message: Union[None, bool] = None,
                 supports_streaming: Union[None, bool] = None) -> None:
        self.duration = duration  # int
        self.w = w  # int
        self.h = h  # int
        self.round_message = round_message  # flags.0?true
        self.supports_streaming = supports_streaming  # flags.1?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "DocumentAttributeVideo":
        flags = Int.read(data)

        round_message = True if flags & (1 << 0) else False
        supports_streaming = True if flags & (1 << 1) else False
        duration = Int.read(data)

        w = Int.read(data)

        h = Int.read(data)

        return DocumentAttributeVideo(duration=duration, w=w, h=h, round_message=round_message,
                                      supports_streaming=supports_streaming)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.round_message is not None else 0
        flags |= (1 << 1) if self.supports_streaming is not None else 0
        data.write(Int(flags))

        data.write(Int(self.duration))

        data.write(Int(self.w))

        data.write(Int(self.h))

        return data.getvalue()
