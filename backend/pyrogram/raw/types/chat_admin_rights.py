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


class ChatAdminRights(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChatAdminRights`.

    Details:
        - Layer: ``122``
        - ID: ``0x5fb224d5``

    Parameters:
        change_info (optional): ``bool``
        post_messages (optional): ``bool``
        edit_messages (optional): ``bool``
        delete_messages (optional): ``bool``
        ban_users (optional): ``bool``
        invite_users (optional): ``bool``
        pin_messages (optional): ``bool``
        add_admins (optional): ``bool``
        anonymous (optional): ``bool``
        manage_call (optional): ``bool``
    """

    __slots__: List[str] = ["change_info", "post_messages", "edit_messages", "delete_messages", "ban_users",
                            "invite_users", "pin_messages", "add_admins", "anonymous", "manage_call"]

    ID = 0x5fb224d5
    QUALNAME = "types.ChatAdminRights"

    def __init__(self, *, change_info: Union[None, bool] = None, post_messages: Union[None, bool] = None,
                 edit_messages: Union[None, bool] = None, delete_messages: Union[None, bool] = None,
                 ban_users: Union[None, bool] = None, invite_users: Union[None, bool] = None,
                 pin_messages: Union[None, bool] = None, add_admins: Union[None, bool] = None,
                 anonymous: Union[None, bool] = None, manage_call: Union[None, bool] = None) -> None:
        self.change_info = change_info  # flags.0?true
        self.post_messages = post_messages  # flags.1?true
        self.edit_messages = edit_messages  # flags.2?true
        self.delete_messages = delete_messages  # flags.3?true
        self.ban_users = ban_users  # flags.4?true
        self.invite_users = invite_users  # flags.5?true
        self.pin_messages = pin_messages  # flags.7?true
        self.add_admins = add_admins  # flags.9?true
        self.anonymous = anonymous  # flags.10?true
        self.manage_call = manage_call  # flags.11?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChatAdminRights":
        flags = Int.read(data)

        change_info = True if flags & (1 << 0) else False
        post_messages = True if flags & (1 << 1) else False
        edit_messages = True if flags & (1 << 2) else False
        delete_messages = True if flags & (1 << 3) else False
        ban_users = True if flags & (1 << 4) else False
        invite_users = True if flags & (1 << 5) else False
        pin_messages = True if flags & (1 << 7) else False
        add_admins = True if flags & (1 << 9) else False
        anonymous = True if flags & (1 << 10) else False
        manage_call = True if flags & (1 << 11) else False
        return ChatAdminRights(change_info=change_info, post_messages=post_messages, edit_messages=edit_messages,
                               delete_messages=delete_messages, ban_users=ban_users, invite_users=invite_users,
                               pin_messages=pin_messages, add_admins=add_admins, anonymous=anonymous,
                               manage_call=manage_call)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.change_info else 0
        flags |= (1 << 1) if self.post_messages else 0
        flags |= (1 << 2) if self.edit_messages else 0
        flags |= (1 << 3) if self.delete_messages else 0
        flags |= (1 << 4) if self.ban_users else 0
        flags |= (1 << 5) if self.invite_users else 0
        flags |= (1 << 7) if self.pin_messages else 0
        flags |= (1 << 9) if self.add_admins else 0
        flags |= (1 << 10) if self.anonymous else 0
        flags |= (1 << 11) if self.manage_call else 0
        data.write(Int(flags))

        return data.getvalue()
