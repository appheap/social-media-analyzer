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


class ChannelParticipantAdmin(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChannelParticipant`.

    Details:
        - Layer: ``122``
        - ID: ``0xccbebbaf``

    Parameters:
        user_id: ``int`` ``32-bit``
        promoted_by: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        admin_rights: :obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`
        can_edit (optional): ``bool``
        is_self (optional): ``bool``
        inviter_id (optional): ``int`` ``32-bit``
        rank (optional): ``str``
    """

    __slots__: List[str] = ["user_id", "promoted_by", "date", "admin_rights", "can_edit", "is_self", "inviter_id",
                            "rank"]

    ID = 0xccbebbaf
    QUALNAME = "types.ChannelParticipantAdmin"

    def __init__(self, *, user_id: int, promoted_by: int, date: int, admin_rights: "raw.base.ChatAdminRights",
                 can_edit: Union[None, bool] = None, is_self: Union[None, bool] = None,
                 inviter_id: Union[None, int] = None, rank: Union[None, str] = None) -> None:
        self.user_id = user_id  # int
        self.promoted_by = promoted_by  # int
        self.date = date  # int
        self.admin_rights = admin_rights  # ChatAdminRights
        self.can_edit = can_edit  # flags.0?true
        self.is_self = is_self  # flags.1?true
        self.inviter_id = inviter_id  # flags.1?int
        self.rank = rank  # flags.2?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChannelParticipantAdmin":
        flags = Int.read(data)

        can_edit = True if flags & (1 << 0) else False
        is_self = True if flags & (1 << 1) else False
        user_id = Int.read(data)

        inviter_id = Int.read(data) if flags & (1 << 1) else None
        promoted_by = Int.read(data)

        date = Int.read(data)

        admin_rights = TLObject.read(data)

        rank = String.read(data) if flags & (1 << 2) else None
        return ChannelParticipantAdmin(user_id=user_id, promoted_by=promoted_by, date=date, admin_rights=admin_rights,
                                       can_edit=can_edit, is_self=is_self, inviter_id=inviter_id, rank=rank)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.can_edit else 0
        flags |= (1 << 1) if self.is_self else 0
        flags |= (1 << 1) if self.inviter_id is not None else 0
        flags |= (1 << 2) if self.rank is not None else 0
        data.write(Int(flags))

        data.write(Int(self.user_id))

        if self.inviter_id is not None:
            data.write(Int(self.inviter_id))

        data.write(Int(self.promoted_by))

        data.write(Int(self.date))

        data.write(self.admin_rights.write())

        if self.rank is not None:
            data.write(String(self.rank))

        return data.getvalue()
