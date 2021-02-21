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


class Folder(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Folder`.

    Details:
        - Layer: ``123``
        - ID: ``0xff544e65``

    Parameters:
        id: ``int`` ``32-bit``
        title: ``str``
        autofill_new_broadcasts (optional): ``bool``
        autofill_public_groups (optional): ``bool``
        autofill_new_correspondents (optional): ``bool``
        photo (optional): :obj:`ChatPhoto <pyrogram.raw.base.ChatPhoto>`
    """

    __slots__: List[str] = ["id", "title", "autofill_new_broadcasts", "autofill_public_groups",
                            "autofill_new_correspondents", "photo"]

    ID = 0xff544e65
    QUALNAME = "types.Folder"

    def __init__(self, *, id: int, title: str, autofill_new_broadcasts: Union[None, bool] = None,
                 autofill_public_groups: Union[None, bool] = None,
                 autofill_new_correspondents: Union[None, bool] = None, photo: "raw.base.ChatPhoto" = None) -> None:
        self.id = id  # int
        self.title = title  # string
        self.autofill_new_broadcasts = autofill_new_broadcasts  # flags.0?true
        self.autofill_public_groups = autofill_public_groups  # flags.1?true
        self.autofill_new_correspondents = autofill_new_correspondents  # flags.2?true
        self.photo = photo  # flags.3?ChatPhoto

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Folder":
        flags = Int.read(data)

        autofill_new_broadcasts = True if flags & (1 << 0) else False
        autofill_public_groups = True if flags & (1 << 1) else False
        autofill_new_correspondents = True if flags & (1 << 2) else False
        id = Int.read(data)

        title = String.read(data)

        photo = TLObject.read(data) if flags & (1 << 3) else None

        return Folder(id=id, title=title, autofill_new_broadcasts=autofill_new_broadcasts,
                      autofill_public_groups=autofill_public_groups,
                      autofill_new_correspondents=autofill_new_correspondents, photo=photo)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.autofill_new_broadcasts else 0
        flags |= (1 << 1) if self.autofill_public_groups else 0
        flags |= (1 << 2) if self.autofill_new_correspondents else 0
        flags |= (1 << 3) if self.photo is not None else 0
        data.write(Int(flags))

        data.write(Int(self.id))

        data.write(String(self.title))

        if self.photo is not None:
            data.write(self.photo.write())

        return data.getvalue()
