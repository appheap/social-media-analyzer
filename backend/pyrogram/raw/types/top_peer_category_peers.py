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


class TopPeerCategoryPeers(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.TopPeerCategoryPeers`.

    Details:
        - Layer: ``120``
        - ID: ``0xfb834291``

    Parameters:
        category: :obj:`TopPeerCategory <pyrogram.raw.base.TopPeerCategory>`
        count: ``int`` ``32-bit``
        peers: List of :obj:`TopPeer <pyrogram.raw.base.TopPeer>`
    """

    __slots__: List[str] = ["category", "count", "peers"]

    ID = 0xfb834291
    QUALNAME = "types.TopPeerCategoryPeers"

    def __init__(self, *, category: "raw.base.TopPeerCategory", count: int, peers: List["raw.base.TopPeer"]) -> None:
        self.category = category  # TopPeerCategory
        self.count = count  # int
        self.peers = peers  # Vector<TopPeer>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "TopPeerCategoryPeers":
        # No flags

        category = TLObject.read(data)

        count = Int.read(data)

        peers = TLObject.read(data)

        return TopPeerCategoryPeers(category=category, count=count, peers=peers)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.category.write())

        data.write(Int(self.count))

        data.write(Vector(self.peers))

        return data.getvalue()
