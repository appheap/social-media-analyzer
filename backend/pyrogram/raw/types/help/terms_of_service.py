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


class TermsOfService(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.help.TermsOfService`.

    Details:
        - Layer: ``123``
        - ID: ``0x780a0310``

    Parameters:
        id: :obj:`DataJSON <pyrogram.raw.base.DataJSON>`
        text: ``str``
        entities: List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`
        popup (optional): ``bool``
        min_age_confirm (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["id", "text", "entities", "popup", "min_age_confirm"]

    ID = 0x780a0310
    QUALNAME = "types.help.TermsOfService"

    def __init__(self, *, id: "raw.base.DataJSON", text: str, entities: List["raw.base.MessageEntity"],
                 popup: Union[None, bool] = None, min_age_confirm: Union[None, int] = None) -> None:
        self.id = id  # DataJSON
        self.text = text  # string
        self.entities = entities  # Vector<MessageEntity>
        self.popup = popup  # flags.0?true
        self.min_age_confirm = min_age_confirm  # flags.1?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "TermsOfService":
        flags = Int.read(data)

        popup = True if flags & (1 << 0) else False
        id = TLObject.read(data)

        text = String.read(data)

        entities = TLObject.read(data)

        min_age_confirm = Int.read(data) if flags & (1 << 1) else None
        return TermsOfService(id=id, text=text, entities=entities, popup=popup, min_age_confirm=min_age_confirm)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.popup else 0
        flags |= (1 << 1) if self.min_age_confirm is not None else 0
        data.write(Int(flags))

        data.write(self.id.write())

        data.write(String(self.text))

        data.write(Vector(self.entities))

        if self.min_age_confirm is not None:
            data.write(Int(self.min_age_confirm))

        return data.getvalue()
