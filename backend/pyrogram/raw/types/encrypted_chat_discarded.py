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


class EncryptedChatDiscarded(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.EncryptedChat`.

    Details:
        - Layer: ``123``
        - ID: ``0x1e1c7c45``

    Parameters:
        id: ``int`` ``32-bit``
        history_deleted (optional): ``bool``

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.RequestEncryption <pyrogram.raw.functions.messages.RequestEncryption>`
            - :obj:`messages.AcceptEncryption <pyrogram.raw.functions.messages.AcceptEncryption>`
    """

    __slots__: List[str] = ["id", "history_deleted"]

    ID = 0x1e1c7c45
    QUALNAME = "types.EncryptedChatDiscarded"

    def __init__(self, *, id: int, history_deleted: Union[None, bool] = None) -> None:
        self.id = id  # int
        self.history_deleted = history_deleted  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "EncryptedChatDiscarded":
        flags = Int.read(data)

        history_deleted = True if flags & (1 << 0) else False
        id = Int.read(data)

        return EncryptedChatDiscarded(id=id, history_deleted=history_deleted)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.history_deleted else 0
        data.write(Int(flags))

        data.write(Int(self.id))

        return data.getvalue()
