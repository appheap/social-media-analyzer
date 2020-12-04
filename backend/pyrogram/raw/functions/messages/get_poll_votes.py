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


class GetPollVotes(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0xb86e380e``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        id: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``
        option (optional): ``bytes``
        offset (optional): ``str``

    Returns:
        :obj:`messages.VotesList <pyrogram.raw.base.messages.VotesList>`
    """

    __slots__: List[str] = ["peer", "id", "limit", "option", "offset"]

    ID = 0xb86e380e
    QUALNAME = "functions.messages.GetPollVotes"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, limit: int, option: Union[None, bytes] = None,
                 offset: Union[None, str] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.limit = limit  # int
        self.option = option  # flags.0?bytes
        self.offset = offset  # flags.1?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetPollVotes":
        flags = Int.read(data)

        peer = TLObject.read(data)

        id = Int.read(data)

        option = Bytes.read(data) if flags & (1 << 0) else None
        offset = String.read(data) if flags & (1 << 1) else None
        limit = Int.read(data)

        return GetPollVotes(peer=peer, id=id, limit=limit, option=option, offset=offset)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.option is not None else 0
        flags |= (1 << 1) if self.offset is not None else 0
        data.write(Int(flags))

        data.write(self.peer.write())

        data.write(Int(self.id))

        if self.option is not None:
            data.write(Bytes(self.option))

        if self.offset is not None:
            data.write(String(self.offset))

        data.write(Int(self.limit))

        return data.getvalue()
