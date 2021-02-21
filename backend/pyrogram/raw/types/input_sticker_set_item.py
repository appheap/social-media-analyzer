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


class InputStickerSetItem(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputStickerSetItem`.

    Details:
        - Layer: ``123``
        - ID: ``0xffa0a496``

    Parameters:
        document: :obj:`InputDocument <pyrogram.raw.base.InputDocument>`
        emoji: ``str``
        mask_coords (optional): :obj:`MaskCoords <pyrogram.raw.base.MaskCoords>`
    """

    __slots__: List[str] = ["document", "emoji", "mask_coords"]

    ID = 0xffa0a496
    QUALNAME = "types.InputStickerSetItem"

    def __init__(self, *, document: "raw.base.InputDocument", emoji: str,
                 mask_coords: "raw.base.MaskCoords" = None) -> None:
        self.document = document  # InputDocument
        self.emoji = emoji  # string
        self.mask_coords = mask_coords  # flags.0?MaskCoords

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputStickerSetItem":
        flags = Int.read(data)

        document = TLObject.read(data)

        emoji = String.read(data)

        mask_coords = TLObject.read(data) if flags & (1 << 0) else None

        return InputStickerSetItem(document=document, emoji=emoji, mask_coords=mask_coords)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.mask_coords is not None else 0
        data.write(Int(flags))

        data.write(self.document.write())

        data.write(String(self.emoji))

        if self.mask_coords is not None:
            data.write(self.mask_coords.write())

        return data.getvalue()
