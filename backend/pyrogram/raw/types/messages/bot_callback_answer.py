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


class BotCallbackAnswer(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.BotCallbackAnswer`.

    Details:
        - Layer: ``123``
        - ID: ``0x36585ea4``

    Parameters:
        cache_time: ``int`` ``32-bit``
        alert (optional): ``bool``
        has_url (optional): ``bool``
        native_ui (optional): ``bool``
        message (optional): ``str``
        url (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetBotCallbackAnswer <pyrogram.raw.functions.messages.GetBotCallbackAnswer>`
    """

    __slots__: List[str] = ["cache_time", "alert", "has_url", "native_ui", "message", "url"]

    ID = 0x36585ea4
    QUALNAME = "types.messages.BotCallbackAnswer"

    def __init__(self, *, cache_time: int, alert: Union[None, bool] = None, has_url: Union[None, bool] = None,
                 native_ui: Union[None, bool] = None, message: Union[None, str] = None,
                 url: Union[None, str] = None) -> None:
        self.cache_time = cache_time  # int
        self.alert = alert  # flags.1?true
        self.has_url = has_url  # flags.3?true
        self.native_ui = native_ui  # flags.4?true
        self.message = message  # flags.0?string
        self.url = url  # flags.2?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "BotCallbackAnswer":
        flags = Int.read(data)

        alert = True if flags & (1 << 1) else False
        has_url = True if flags & (1 << 3) else False
        native_ui = True if flags & (1 << 4) else False
        message = String.read(data) if flags & (1 << 0) else None
        url = String.read(data) if flags & (1 << 2) else None
        cache_time = Int.read(data)

        return BotCallbackAnswer(cache_time=cache_time, alert=alert, has_url=has_url, native_ui=native_ui,
                                 message=message, url=url)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.alert else 0
        flags |= (1 << 3) if self.has_url else 0
        flags |= (1 << 4) if self.native_ui else 0
        flags |= (1 << 0) if self.message is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        data.write(Int(flags))

        if self.message is not None:
            data.write(String(self.message))

        if self.url is not None:
            data.write(String(self.url))

        data.write(Int(self.cache_time))

        return data.getvalue()
