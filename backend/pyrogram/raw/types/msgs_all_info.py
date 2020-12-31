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


class MsgsAllInfo(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.MsgsAllInfo`.

    Details:
        - Layer: ``122``
        - ID: ``0x8cc0d131``

    Parameters:
        msg_ids: List of ``int`` ``64-bit``
        info: ``str``
    """

    __slots__: List[str] = ["msg_ids", "info"]

    ID = 0x8cc0d131
    QUALNAME = "types.MsgsAllInfo"

    def __init__(self, *, msg_ids: List[int], info: str) -> None:
        self.msg_ids = msg_ids  # Vector<long>
        self.info = info  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MsgsAllInfo":
        # No flags

        msg_ids = TLObject.read(data, Long)

        info = String.read(data)

        return MsgsAllInfo(msg_ids=msg_ids, info=info)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Vector(self.msg_ids, Long))

        data.write(String(self.info))

        return data.getvalue()
