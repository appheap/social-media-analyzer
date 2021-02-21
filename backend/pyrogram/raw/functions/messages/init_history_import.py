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


class InitHistoryImport(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x34090c3b``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        file: :obj:`InputFile <pyrogram.raw.base.InputFile>`
        media_count: ``int`` ``32-bit``

    Returns:
        :obj:`messages.HistoryImport <pyrogram.raw.base.messages.HistoryImport>`
    """

    __slots__: List[str] = ["peer", "file", "media_count"]

    ID = 0x34090c3b
    QUALNAME = "functions.messages.InitHistoryImport"

    def __init__(self, *, peer: "raw.base.InputPeer", file: "raw.base.InputFile", media_count: int) -> None:
        self.peer = peer  # InputPeer
        self.file = file  # InputFile
        self.media_count = media_count  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InitHistoryImport":
        # No flags

        peer = TLObject.read(data)

        file = TLObject.read(data)

        media_count = Int.read(data)

        return InitHistoryImport(peer=peer, file=file, media_count=media_count)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.peer.write())

        data.write(self.file.write())

        data.write(Int(self.media_count))

        return data.getvalue()
