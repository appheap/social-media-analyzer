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


class InitTakeoutSession(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0xf05b4804``

    Parameters:
        contacts (optional): ``bool``
        message_users (optional): ``bool``
        message_chats (optional): ``bool``
        message_megagroups (optional): ``bool``
        message_channels (optional): ``bool``
        files (optional): ``bool``
        file_max_size (optional): ``int`` ``32-bit``

    Returns:
        :obj:`account.Takeout <pyrogram.raw.base.account.Takeout>`
    """

    __slots__: List[str] = ["contacts", "message_users", "message_chats", "message_megagroups", "message_channels",
                            "files", "file_max_size"]

    ID = 0xf05b4804
    QUALNAME = "functions.account.InitTakeoutSession"

    def __init__(self, *, contacts: Union[None, bool] = None, message_users: Union[None, bool] = None,
                 message_chats: Union[None, bool] = None, message_megagroups: Union[None, bool] = None,
                 message_channels: Union[None, bool] = None, files: Union[None, bool] = None,
                 file_max_size: Union[None, int] = None) -> None:
        self.contacts = contacts  # flags.0?true
        self.message_users = message_users  # flags.1?true
        self.message_chats = message_chats  # flags.2?true
        self.message_megagroups = message_megagroups  # flags.3?true
        self.message_channels = message_channels  # flags.4?true
        self.files = files  # flags.5?true
        self.file_max_size = file_max_size  # flags.5?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InitTakeoutSession":
        flags = Int.read(data)

        contacts = True if flags & (1 << 0) else False
        message_users = True if flags & (1 << 1) else False
        message_chats = True if flags & (1 << 2) else False
        message_megagroups = True if flags & (1 << 3) else False
        message_channels = True if flags & (1 << 4) else False
        files = True if flags & (1 << 5) else False
        file_max_size = Int.read(data) if flags & (1 << 5) else None
        return InitTakeoutSession(contacts=contacts, message_users=message_users, message_chats=message_chats,
                                  message_megagroups=message_megagroups, message_channels=message_channels, files=files,
                                  file_max_size=file_max_size)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.contacts else 0
        flags |= (1 << 1) if self.message_users else 0
        flags |= (1 << 2) if self.message_chats else 0
        flags |= (1 << 3) if self.message_megagroups else 0
        flags |= (1 << 4) if self.message_channels else 0
        flags |= (1 << 5) if self.files else 0
        flags |= (1 << 5) if self.file_max_size is not None else 0
        data.write(Int(flags))

        if self.file_max_size is not None:
            data.write(Int(self.file_max_size))

        return data.getvalue()
