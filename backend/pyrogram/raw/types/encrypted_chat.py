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


class EncryptedChat(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.EncryptedChat`.

    Details:
        - Layer: ``117``
        - ID: ``0xfa56ce36``

    Parameters:
        id: ``int`` ``32-bit``
        access_hash: ``int`` ``64-bit``
        date: ``int`` ``32-bit``
        admin_id: ``int`` ``32-bit``
        participant_id: ``int`` ``32-bit``
        g_a_or_b: ``bytes``
        key_fingerprint: ``int`` ``64-bit``

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.RequestEncryption <pyrogram.raw.functions.messages.RequestEncryption>`
            - :obj:`messages.AcceptEncryption <pyrogram.raw.functions.messages.AcceptEncryption>`
    """

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id", "g_a_or_b", "key_fingerprint"]

    ID = 0xfa56ce36
    QUALNAME = "types.EncryptedChat"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_a_or_b: bytes,
                 key_fingerprint: int) -> None:
        self.id = id  # int
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # int
        self.participant_id = participant_id  # int
        self.g_a_or_b = g_a_or_b  # bytes
        self.key_fingerprint = key_fingerprint  # long

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "EncryptedChat":
        # No flags

        id = Int.read(data)

        access_hash = Long.read(data)

        date = Int.read(data)

        admin_id = Int.read(data)

        participant_id = Int.read(data)

        g_a_or_b = Bytes.read(data)

        key_fingerprint = Long.read(data)

        return EncryptedChat(id=id, access_hash=access_hash, date=date, admin_id=admin_id,
                             participant_id=participant_id, g_a_or_b=g_a_or_b, key_fingerprint=key_fingerprint)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Int(self.id))

        data.write(Long(self.access_hash))

        data.write(Int(self.date))

        data.write(Int(self.admin_id))

        data.write(Int(self.participant_id))

        data.write(Bytes(self.g_a_or_b))

        data.write(Long(self.key_fingerprint))

        return data.getvalue()
