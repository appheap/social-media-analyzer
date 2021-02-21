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


class CodeSettings(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.CodeSettings`.

    Details:
        - Layer: ``123``
        - ID: ``0xdebebe83``

    Parameters:
        allow_flashcall (optional): ``bool``
        current_number (optional): ``bool``
        allow_app_hash (optional): ``bool``
    """

    __slots__: List[str] = ["allow_flashcall", "current_number", "allow_app_hash"]

    ID = 0xdebebe83
    QUALNAME = "types.CodeSettings"

    def __init__(self, *, allow_flashcall: Union[None, bool] = None, current_number: Union[None, bool] = None,
                 allow_app_hash: Union[None, bool] = None) -> None:
        self.allow_flashcall = allow_flashcall  # flags.0?true
        self.current_number = current_number  # flags.1?true
        self.allow_app_hash = allow_app_hash  # flags.4?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "CodeSettings":
        flags = Int.read(data)

        allow_flashcall = True if flags & (1 << 0) else False
        current_number = True if flags & (1 << 1) else False
        allow_app_hash = True if flags & (1 << 4) else False
        return CodeSettings(allow_flashcall=allow_flashcall, current_number=current_number,
                            allow_app_hash=allow_app_hash)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.allow_flashcall else 0
        flags |= (1 << 1) if self.current_number else 0
        flags |= (1 << 4) if self.allow_app_hash else 0
        data.write(Int(flags))

        return data.getvalue()
