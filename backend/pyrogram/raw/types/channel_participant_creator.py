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


class ChannelParticipantCreator(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChannelParticipant`.

    Details:
        - Layer: ``120``
        - ID: ``0x447dca4b``

    Parameters:
        user_id: ``int`` ``32-bit``
        admin_rights: :obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`
        rank (optional): ``str``
    """

    __slots__: List[str] = ["user_id", "admin_rights", "rank"]

    ID = 0x447dca4b
    QUALNAME = "types.ChannelParticipantCreator"

    def __init__(self, *, user_id: int, admin_rights: "raw.base.ChatAdminRights",
                 rank: Union[None, str] = None) -> None:
        self.user_id = user_id  # int
        self.admin_rights = admin_rights  # ChatAdminRights
        self.rank = rank  # flags.0?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChannelParticipantCreator":
        flags = Int.read(data)

        user_id = Int.read(data)

        admin_rights = TLObject.read(data)

        rank = String.read(data) if flags & (1 << 0) else None
        return ChannelParticipantCreator(user_id=user_id, admin_rights=admin_rights, rank=rank)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rank is not None else 0
        data.write(Int(flags))

        data.write(Int(self.user_id))

        data.write(self.admin_rights.write())

        if self.rank is not None:
            data.write(String(self.rank))

        return data.getvalue()
