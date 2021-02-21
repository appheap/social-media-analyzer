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


class SendMessageUploadRoundAction(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``123``
        - ID: ``0x243e1c66``

    Parameters:
        progress: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["progress"]

    ID = 0x243e1c66
    QUALNAME = "types.SendMessageUploadRoundAction"

    def __init__(self, *, progress: int) -> None:
        self.progress = progress  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SendMessageUploadRoundAction":
        # No flags

        progress = Int.read(data)

        return SendMessageUploadRoundAction(progress=progress)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.progress))

        return data.getvalue()
