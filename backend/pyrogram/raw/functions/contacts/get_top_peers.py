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


class GetTopPeers(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``120``
        - ID: ``0xd4982db5``

    Parameters:
        offset: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``
        hash: ``int`` ``32-bit``
        correspondents (optional): ``bool``
        bots_pm (optional): ``bool``
        bots_inline (optional): ``bool``
        phone_calls (optional): ``bool``
        forward_users (optional): ``bool``
        forward_chats (optional): ``bool``
        groups (optional): ``bool``
        channels (optional): ``bool``

    Returns:
        :obj:`contacts.TopPeers <pyrogram.raw.base.contacts.TopPeers>`
    """

    __slots__: List[str] = ["offset", "limit", "hash", "correspondents", "bots_pm", "bots_inline", "phone_calls",
                            "forward_users", "forward_chats", "groups", "channels"]

    ID = 0xd4982db5
    QUALNAME = "functions.contacts.GetTopPeers"

    def __init__(self, *, offset: int, limit: int, hash: int, correspondents: Union[None, bool] = None,
                 bots_pm: Union[None, bool] = None, bots_inline: Union[None, bool] = None,
                 phone_calls: Union[None, bool] = None, forward_users: Union[None, bool] = None,
                 forward_chats: Union[None, bool] = None, groups: Union[None, bool] = None,
                 channels: Union[None, bool] = None) -> None:
        self.offset = offset  # int
        self.limit = limit  # int
        self.hash = hash  # int
        self.correspondents = correspondents  # flags.0?true
        self.bots_pm = bots_pm  # flags.1?true
        self.bots_inline = bots_inline  # flags.2?true
        self.phone_calls = phone_calls  # flags.3?true
        self.forward_users = forward_users  # flags.4?true
        self.forward_chats = forward_chats  # flags.5?true
        self.groups = groups  # flags.10?true
        self.channels = channels  # flags.15?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetTopPeers":
        flags = Int.read(data)

        correspondents = True if flags & (1 << 0) else False
        bots_pm = True if flags & (1 << 1) else False
        bots_inline = True if flags & (1 << 2) else False
        phone_calls = True if flags & (1 << 3) else False
        forward_users = True if flags & (1 << 4) else False
        forward_chats = True if flags & (1 << 5) else False
        groups = True if flags & (1 << 10) else False
        channels = True if flags & (1 << 15) else False
        offset = Int.read(data)

        limit = Int.read(data)

        hash = Int.read(data)

        return GetTopPeers(offset=offset, limit=limit, hash=hash, correspondents=correspondents, bots_pm=bots_pm,
                           bots_inline=bots_inline, phone_calls=phone_calls, forward_users=forward_users,
                           forward_chats=forward_chats, groups=groups, channels=channels)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.correspondents is not None else 0
        flags |= (1 << 1) if self.bots_pm is not None else 0
        flags |= (1 << 2) if self.bots_inline is not None else 0
        flags |= (1 << 3) if self.phone_calls is not None else 0
        flags |= (1 << 4) if self.forward_users is not None else 0
        flags |= (1 << 5) if self.forward_chats is not None else 0
        flags |= (1 << 10) if self.groups is not None else 0
        flags |= (1 << 15) if self.channels is not None else 0
        data.write(Int(flags))

        data.write(Int(self.offset))

        data.write(Int(self.limit))

        data.write(Int(self.hash))

        return data.getvalue()
