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


class EncryptedChatRequested(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.EncryptedChat`.

    Details:
        - Layer: ``122``
        - ID: ``0x62718a82``

    Parameters:
        id: ``int`` ``32-bit``
        access_hash: ``int`` ``64-bit``
        date: ``int`` ``32-bit``
        admin_id: ``int`` ``32-bit``
        participant_id: ``int`` ``32-bit``
        g_a: ``bytes``
        folder_id (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.RequestEncryption <pyrogram.raw.functions.messages.RequestEncryption>`
            - :obj:`messages.AcceptEncryption <pyrogram.raw.functions.messages.AcceptEncryption>`
    """

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id", "g_a", "folder_id"]

    ID = 0x62718a82
    QUALNAME = "types.EncryptedChatRequested"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_a: bytes,
                 folder_id: Union[None, int] = None) -> None:
        self.id = id  # int
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # int
        self.participant_id = participant_id  # int
        self.g_a = g_a  # bytes
        self.folder_id = folder_id  # flags.0?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "EncryptedChatRequested":
        flags = Int.read(data)

        folder_id = Int.read(data) if flags & (1 << 0) else None
        id = Int.read(data)

        access_hash = Long.read(data)

        date = Int.read(data)

        admin_id = Int.read(data)

        participant_id = Int.read(data)

        g_a = Bytes.read(data)

        return EncryptedChatRequested(id=id, access_hash=access_hash, date=date, admin_id=admin_id,
                                      participant_id=participant_id, g_a=g_a, folder_id=folder_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.folder_id is not None else 0
        data.write(Int(flags))

        if self.folder_id is not None:
            data.write(Int(self.folder_id))

        data.write(Int(self.id))

        data.write(Long(self.access_hash))

        data.write(Int(self.date))

        data.write(Int(self.admin_id))

        data.write(Int(self.participant_id))

        data.write(Bytes(self.g_a))

        return data.getvalue()
