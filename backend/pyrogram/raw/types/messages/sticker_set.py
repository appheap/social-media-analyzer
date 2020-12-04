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


class StickerSet(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.StickerSet`.

    Details:
        - Layer: ``120``
        - ID: ``0xb60a24a6``

    Parameters:
        set: :obj:`StickerSet <pyrogram.raw.base.StickerSet>`
        packs: List of :obj:`StickerPack <pyrogram.raw.base.StickerPack>`
        documents: List of :obj:`Document <pyrogram.raw.base.Document>`

    See Also:
        This object can be returned by 6 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetStickerSet <pyrogram.raw.functions.messages.GetStickerSet>`
            - :obj:`stickers.CreateStickerSet <pyrogram.raw.functions.stickers.CreateStickerSet>`
            - :obj:`stickers.RemoveStickerFromSet <pyrogram.raw.functions.stickers.RemoveStickerFromSet>`
            - :obj:`stickers.ChangeStickerPosition <pyrogram.raw.functions.stickers.ChangeStickerPosition>`
            - :obj:`stickers.AddStickerToSet <pyrogram.raw.functions.stickers.AddStickerToSet>`
            - :obj:`stickers.SetStickerSetThumb <pyrogram.raw.functions.stickers.SetStickerSetThumb>`
    """

    __slots__: List[str] = ["set", "packs", "documents"]

    ID = 0xb60a24a6
    QUALNAME = "types.messages.StickerSet"

    def __init__(self, *, set: "raw.base.StickerSet", packs: List["raw.base.StickerPack"],
                 documents: List["raw.base.Document"]) -> None:
        self.set = set  # StickerSet
        self.packs = packs  # Vector<StickerPack>
        self.documents = documents  # Vector<Document>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StickerSet":
        # No flags

        set = TLObject.read(data)

        packs = TLObject.read(data)

        documents = TLObject.read(data)

        return StickerSet(set=set, packs=packs, documents=documents)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.set.write())

        data.write(Vector(self.packs))

        data.write(Vector(self.documents))

        return data.getvalue()
