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


class CreateStickerSet(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0xf1036780``

    Parameters:
        user_id: :obj:`InputUser <pyrogram.raw.base.InputUser>`
        title: ``str``
        short_name: ``str``
        stickers: List of :obj:`InputStickerSetItem <pyrogram.raw.base.InputStickerSetItem>`
        masks (optional): ``bool``
        animated (optional): ``bool``
        thumb (optional): :obj:`InputDocument <pyrogram.raw.base.InputDocument>`

    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: List[str] = ["user_id", "title", "short_name", "stickers", "masks", "animated", "thumb"]

    ID = 0xf1036780
    QUALNAME = "functions.stickers.CreateStickerSet"

    def __init__(self, *, user_id: "raw.base.InputUser", title: str, short_name: str,
                 stickers: List["raw.base.InputStickerSetItem"], masks: Union[None, bool] = None,
                 animated: Union[None, bool] = None, thumb: "raw.base.InputDocument" = None) -> None:
        self.user_id = user_id  # InputUser
        self.title = title  # string
        self.short_name = short_name  # string
        self.stickers = stickers  # Vector<InputStickerSetItem>
        self.masks = masks  # flags.0?true
        self.animated = animated  # flags.1?true
        self.thumb = thumb  # flags.2?InputDocument

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "CreateStickerSet":
        flags = Int.read(data)

        masks = True if flags & (1 << 0) else False
        animated = True if flags & (1 << 1) else False
        user_id = TLObject.read(data)

        title = String.read(data)

        short_name = String.read(data)

        thumb = TLObject.read(data) if flags & (1 << 2) else None

        stickers = TLObject.read(data)

        return CreateStickerSet(user_id=user_id, title=title, short_name=short_name, stickers=stickers, masks=masks,
                                animated=animated, thumb=thumb)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.masks else 0
        flags |= (1 << 1) if self.animated else 0
        flags |= (1 << 2) if self.thumb is not None else 0
        data.write(Int(flags))

        data.write(self.user_id.write())

        data.write(String(self.title))

        data.write(String(self.short_name))

        if self.thumb is not None:
            data.write(self.thumb.write())

        data.write(Vector(self.stickers))

        return data.getvalue()
