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


class InputKeyboardButtonUrlAuth(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``122``
        - ID: ``0xd02e7fd4``

    Parameters:
        text: ``str``
        url: ``str``
        bot: :obj:`InputUser <pyrogram.raw.base.InputUser>`
        request_write_access (optional): ``bool``
        fwd_text (optional): ``str``
    """

    __slots__: List[str] = ["text", "url", "bot", "request_write_access", "fwd_text"]

    ID = 0xd02e7fd4
    QUALNAME = "types.InputKeyboardButtonUrlAuth"

    def __init__(self, *, text: str, url: str, bot: "raw.base.InputUser",
                 request_write_access: Union[None, bool] = None, fwd_text: Union[None, str] = None) -> None:
        self.text = text  # string
        self.url = url  # string
        self.bot = bot  # InputUser
        self.request_write_access = request_write_access  # flags.0?true
        self.fwd_text = fwd_text  # flags.1?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputKeyboardButtonUrlAuth":
        flags = Int.read(data)

        request_write_access = True if flags & (1 << 0) else False
        text = String.read(data)

        fwd_text = String.read(data) if flags & (1 << 1) else None
        url = String.read(data)

        bot = TLObject.read(data)

        return InputKeyboardButtonUrlAuth(text=text, url=url, bot=bot, request_write_access=request_write_access,
                                          fwd_text=fwd_text)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.request_write_access else 0
        flags |= (1 << 1) if self.fwd_text is not None else 0
        data.write(Int(flags))

        data.write(String(self.text))

        if self.fwd_text is not None:
            data.write(String(self.fwd_text))

        data.write(String(self.url))

        data.write(self.bot.write())

        return data.getvalue()
