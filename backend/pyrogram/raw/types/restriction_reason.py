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


class RestrictionReason(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.RestrictionReason`.

    Details:
        - Layer: ``123``
        - ID: ``0xd072acb4``

    Parameters:
        platform: ``str``
        reason: ``str``
        text: ``str``
    """

    __slots__: List[str] = ["platform", "reason", "text"]

    ID = 0xd072acb4
    QUALNAME = "types.RestrictionReason"

    def __init__(self, *, platform: str, reason: str, text: str) -> None:
        self.platform = platform  # string
        self.reason = reason  # string
        self.text = text  # string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "RestrictionReason":
        # No flags

        platform = String.read(data)

        reason = String.read(data)

        text = String.read(data)

        return RestrictionReason(platform=platform, reason=reason, text=text)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(String(self.platform))

        data.write(String(self.reason))

        data.write(String(self.text))

        return data.getvalue()
