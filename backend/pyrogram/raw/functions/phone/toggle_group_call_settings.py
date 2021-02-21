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


class ToggleGroupCallSettings(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x74bbb43d``

    Parameters:
        call: :obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`
        join_muted (optional): ``bool``

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "join_muted"]

    ID = 0x74bbb43d
    QUALNAME = "functions.phone.ToggleGroupCallSettings"

    def __init__(self, *, call: "raw.base.InputGroupCall", join_muted: Union[None, bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.join_muted = join_muted  # flags.0?Bool

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ToggleGroupCallSettings":
        flags = Int.read(data)

        call = TLObject.read(data)

        join_muted = Bool.read(data) if flags & (1 << 0) else None
        return ToggleGroupCallSettings(call=call, join_muted=join_muted)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.join_muted is not None else 0
        data.write(Int(flags))

        data.write(self.call.write())

        if self.join_muted is not None:
            data.write(Bool(self.join_muted))

        return data.getvalue()
