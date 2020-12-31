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


class PromoData(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.help.PromoData`.

    Details:
        - Layer: ``122``
        - ID: ``0x8c39793f``

    Parameters:
        expires: ``int`` ``32-bit``
        peer: :obj:`Peer <pyrogram.raw.base.Peer>`
        chats: List of :obj:`Chat <pyrogram.raw.base.Chat>`
        users: List of :obj:`User <pyrogram.raw.base.User>`
        proxy (optional): ``bool``
        psa_type (optional): ``str``
        psa_message (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`help.GetPromoData <pyrogram.raw.functions.help.GetPromoData>`
    """

    __slots__: List[str] = ["expires", "peer", "chats", "users", "proxy", "psa_type", "psa_message"]

    ID = 0x8c39793f
    QUALNAME = "types.help.PromoData"

    def __init__(self, *, expires: int, peer: "raw.base.Peer", chats: List["raw.base.Chat"],
                 users: List["raw.base.User"], proxy: Union[None, bool] = None, psa_type: Union[None, str] = None,
                 psa_message: Union[None, str] = None) -> None:
        self.expires = expires  # int
        self.peer = peer  # Peer
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.proxy = proxy  # flags.0?true
        self.psa_type = psa_type  # flags.1?string
        self.psa_message = psa_message  # flags.2?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PromoData":
        flags = Int.read(data)

        proxy = True if flags & (1 << 0) else False
        expires = Int.read(data)

        peer = TLObject.read(data)

        chats = TLObject.read(data)

        users = TLObject.read(data)

        psa_type = String.read(data) if flags & (1 << 1) else None
        psa_message = String.read(data) if flags & (1 << 2) else None
        return PromoData(expires=expires, peer=peer, chats=chats, users=users, proxy=proxy, psa_type=psa_type,
                         psa_message=psa_message)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.proxy else 0
        flags |= (1 << 1) if self.psa_type is not None else 0
        flags |= (1 << 2) if self.psa_message is not None else 0
        data.write(Int(flags))

        data.write(Int(self.expires))

        data.write(self.peer.write())

        data.write(Vector(self.chats))

        data.write(Vector(self.users))

        if self.psa_type is not None:
            data.write(String(self.psa_type))

        if self.psa_message is not None:
            data.write(String(self.psa_message))

        return data.getvalue()
