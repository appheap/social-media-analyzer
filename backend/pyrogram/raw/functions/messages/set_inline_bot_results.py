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


class SetInlineBotResults(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0xeb5ea206``

    Parameters:
        query_id: ``int`` ``64-bit``
        results: List of :obj:`InputBotInlineResult <pyrogram.raw.base.InputBotInlineResult>`
        cache_time: ``int`` ``32-bit``
        gallery (optional): ``bool``
        private (optional): ``bool``
        next_offset (optional): ``str``
        switch_pm (optional): :obj:`InlineBotSwitchPM <pyrogram.raw.base.InlineBotSwitchPM>`

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id", "results", "cache_time", "gallery", "private", "next_offset", "switch_pm"]

    ID = 0xeb5ea206
    QUALNAME = "functions.messages.SetInlineBotResults"

    def __init__(self, *, query_id: int, results: List["raw.base.InputBotInlineResult"], cache_time: int,
                 gallery: Union[None, bool] = None, private: Union[None, bool] = None,
                 next_offset: Union[None, str] = None, switch_pm: "raw.base.InlineBotSwitchPM" = None) -> None:
        self.query_id = query_id  # long
        self.results = results  # Vector<InputBotInlineResult>
        self.cache_time = cache_time  # int
        self.gallery = gallery  # flags.0?true
        self.private = private  # flags.1?true
        self.next_offset = next_offset  # flags.2?string
        self.switch_pm = switch_pm  # flags.3?InlineBotSwitchPM

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SetInlineBotResults":
        flags = Int.read(data)

        gallery = True if flags & (1 << 0) else False
        private = True if flags & (1 << 1) else False
        query_id = Long.read(data)

        results = TLObject.read(data)

        cache_time = Int.read(data)

        next_offset = String.read(data) if flags & (1 << 2) else None
        switch_pm = TLObject.read(data) if flags & (1 << 3) else None

        return SetInlineBotResults(query_id=query_id, results=results, cache_time=cache_time, gallery=gallery,
                                   private=private, next_offset=next_offset, switch_pm=switch_pm)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.gallery is not None else 0
        flags |= (1 << 1) if self.private is not None else 0
        flags |= (1 << 2) if self.next_offset is not None else 0
        flags |= (1 << 3) if self.switch_pm is not None else 0
        data.write(Int(flags))

        data.write(Long(self.query_id))

        data.write(Vector(self.results))

        data.write(Int(self.cache_time))

        if self.next_offset is not None:
            data.write(String(self.next_offset))

        if self.switch_pm is not None:
            data.write(self.switch_pm.write())

        return data.getvalue()
