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


class BotCommand(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.BotCommand`.

    Details:
        - Layer: ``122``
        - ID: ``0xc27ac8c7``

    Parameters:
        command: ``str``
        description: ``str``
    """

    __slots__: List[str] = ["command", "description"]

    ID = 0xc27ac8c7
    QUALNAME = "types.BotCommand"

    def __init__(self, *, command: str, description: str) -> None:
        self.command = command  # string
        self.description = description  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "BotCommand":
        # No flags

        command = String.read(data)

        description = String.read(data)

        return BotCommand(command=command, description=description)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.command))

        data.write(String(self.description))

        return data.getvalue()
