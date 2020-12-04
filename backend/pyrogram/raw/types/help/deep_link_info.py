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


class DeepLinkInfo(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.help.DeepLinkInfo`.

    Details:
        - Layer: ``120``
        - ID: ``0x6a4ee832``

    Parameters:
        message: ``str``
        update_app (optional): ``bool``
        entities (optional): List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`help.GetDeepLinkInfo <pyrogram.raw.functions.help.GetDeepLinkInfo>`
    """

    __slots__: List[str] = ["message", "update_app", "entities"]

    ID = 0x6a4ee832
    QUALNAME = "types.help.DeepLinkInfo"

    def __init__(self, *, message: str, update_app: Union[None, bool] = None,
                 entities: Union[None, List["raw.base.MessageEntity"]] = None) -> None:
        self.message = message  # string
        self.update_app = update_app  # flags.0?true
        self.entities = entities  # flags.1?Vector<MessageEntity>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "DeepLinkInfo":
        flags = Int.read(data)

        update_app = True if flags & (1 << 0) else False
        message = String.read(data)

        entities = TLObject.read(data) if flags & (1 << 1) else []

        return DeepLinkInfo(message=message, update_app=update_app, entities=entities)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.update_app is not None else 0
        flags |= (1 << 1) if self.entities is not None else 0
        data.write(Int(flags))

        data.write(String(self.message))

        if self.entities is not None:
            data.write(Vector(self.entities))

        return data.getvalue()
