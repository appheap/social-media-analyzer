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


class EditPhoto(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0xf12e57c9``

    Parameters:
        channel: :obj:`InputChannel <pyrogram.raw.base.InputChannel>`
        photo: :obj:`InputChatPhoto <pyrogram.raw.base.InputChatPhoto>`

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "photo"]

    ID = 0xf12e57c9
    QUALNAME = "functions.channels.EditPhoto"

    def __init__(self, *, channel: "raw.base.InputChannel", photo: "raw.base.InputChatPhoto") -> None:
        self.channel = channel  # InputChannel
        self.photo = photo  # InputChatPhoto

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "EditPhoto":
        # No flags

        channel = TLObject.read(data)

        photo = TLObject.read(data)

        return EditPhoto(channel=channel, photo=photo)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.channel.write())

        data.write(self.photo.write())

        return data.getvalue()
