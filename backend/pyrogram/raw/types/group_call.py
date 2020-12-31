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


class GroupCall(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.GroupCall`.

    Details:
        - Layer: ``122``
        - ID: ``0x55903081``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        participants_count: ``int`` ``32-bit``
        version: ``int`` ``32-bit``
        join_muted (optional): ``bool``
        can_change_join_muted (optional): ``bool``
        params (optional): :obj:`DataJSON <pyrogram.raw.base.DataJSON>`
    """

    __slots__: List[str] = ["id", "access_hash", "participants_count", "version", "join_muted", "can_change_join_muted",
                            "params"]

    ID = 0x55903081
    QUALNAME = "types.GroupCall"

    def __init__(self, *, id: int, access_hash: int, participants_count: int, version: int,
                 join_muted: Union[None, bool] = None, can_change_join_muted: Union[None, bool] = None,
                 params: "raw.base.DataJSON" = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.participants_count = participants_count  # int
        self.version = version  # int
        self.join_muted = join_muted  # flags.1?true
        self.can_change_join_muted = can_change_join_muted  # flags.2?true
        self.params = params  # flags.0?DataJSON

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GroupCall":
        flags = Int.read(data)

        join_muted = True if flags & (1 << 1) else False
        can_change_join_muted = True if flags & (1 << 2) else False
        id = Long.read(data)

        access_hash = Long.read(data)

        participants_count = Int.read(data)

        params = TLObject.read(data) if flags & (1 << 0) else None

        version = Int.read(data)

        return GroupCall(id=id, access_hash=access_hash, participants_count=participants_count, version=version,
                         join_muted=join_muted, can_change_join_muted=can_change_join_muted, params=params)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.join_muted else 0
        flags |= (1 << 2) if self.can_change_join_muted else 0
        flags |= (1 << 0) if self.params is not None else 0
        data.write(Int(flags))

        data.write(Long(self.id))

        data.write(Long(self.access_hash))

        data.write(Int(self.participants_count))

        if self.params is not None:
            data.write(self.params.write())

        data.write(Int(self.version))

        return data.getvalue()
