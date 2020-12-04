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


class KeyboardButtonRequestPoll(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``120``
        - ID: ``0xbbc7515d``

    Parameters:
        text: ``str``
        quiz (optional): ``bool``
    """

    __slots__: List[str] = ["text", "quiz"]

    ID = 0xbbc7515d
    QUALNAME = "types.KeyboardButtonRequestPoll"

    def __init__(self, *, text: str, quiz: Union[None, bool] = None) -> None:
        self.text = text  # string
        self.quiz = quiz  # flags.0?Bool

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "KeyboardButtonRequestPoll":
        flags = Int.read(data)

        quiz = Bool.read(data) if flags & (1 << 0) else None
        text = String.read(data)

        return KeyboardButtonRequestPoll(text=text, quiz=quiz)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.quiz is not None else 0
        data.write(Int(flags))

        if self.quiz is not None:
            data.write(Bool(self.quiz))

        data.write(String(self.text))

        return data.getvalue()
