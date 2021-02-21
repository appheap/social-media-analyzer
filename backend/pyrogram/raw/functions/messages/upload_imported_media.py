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


class UploadImportedMedia(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0x2a862092``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        import_id: ``int`` ``64-bit``
        file_name: ``str``
        media: :obj:`InputMedia <pyrogram.raw.base.InputMedia>`

    Returns:
        :obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`
    """

    __slots__: List[str] = ["peer", "import_id", "file_name", "media"]

    ID = 0x2a862092
    QUALNAME = "functions.messages.UploadImportedMedia"

    def __init__(self, *, peer: "raw.base.InputPeer", import_id: int, file_name: str,
                 media: "raw.base.InputMedia") -> None:
        self.peer = peer  # InputPeer
        self.import_id = import_id  # long
        self.file_name = file_name  # string
        self.media = media  # InputMedia

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UploadImportedMedia":
        # No flags

        peer = TLObject.read(data)

        import_id = Long.read(data)

        file_name = String.read(data)

        media = TLObject.read(data)

        return UploadImportedMedia(peer=peer, import_id=import_id, file_name=file_name, media=media)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.peer.write())

        data.write(Long(self.import_id))

        data.write(String(self.file_name))

        data.write(self.media.write())

        return data.getvalue()
