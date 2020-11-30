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


class DifferenceSlice(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.updates.Difference`.

    Details:
        - Layer: ``117``
        - ID: ``0xa8fb1981``

    Parameters:
        new_messages: List of :obj:`Message <pyrogram.raw.base.Message>`
        new_encrypted_messages: List of :obj:`EncryptedMessage <pyrogram.raw.base.EncryptedMessage>`
        other_updates: List of :obj:`Update <pyrogram.raw.base.Update>`
        chats: List of :obj:`Chat <pyrogram.raw.base.Chat>`
        users: List of :obj:`User <pyrogram.raw.base.User>`
        intermediate_state: :obj:`updates.State <pyrogram.raw.base.updates.State>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`updates.GetDifference <pyrogram.raw.functions.updates.GetDifference>`
    """

    __slots__: List[str] = ["new_messages", "new_encrypted_messages", "other_updates", "chats", "users",
                            "intermediate_state"]

    ID = 0xa8fb1981
    QUALNAME = "types.updates.DifferenceSlice"

    def __init__(self, *, new_messages: List["raw.base.Message"],
                 new_encrypted_messages: List["raw.base.EncryptedMessage"], other_updates: List["raw.base.Update"],
                 chats: List["raw.base.Chat"], users: List["raw.base.User"],
                 intermediate_state: "raw.base.updates.State") -> None:
        self.new_messages = new_messages  # Vector<Message>
        self.new_encrypted_messages = new_encrypted_messages  # Vector<EncryptedMessage>
        self.other_updates = other_updates  # Vector<Update>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.intermediate_state = intermediate_state  # updates.State

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "DifferenceSlice":
        # No flags

        new_messages = TLObject.read(data)

        new_encrypted_messages = TLObject.read(data)

        other_updates = TLObject.read(data)

        chats = TLObject.read(data)

        users = TLObject.read(data)

        intermediate_state = TLObject.read(data)

        return DifferenceSlice(new_messages=new_messages, new_encrypted_messages=new_encrypted_messages,
                               other_updates=other_updates, chats=chats, users=users,
                               intermediate_state=intermediate_state)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Vector(self.new_messages))

        data.write(Vector(self.new_encrypted_messages))

        data.write(Vector(self.other_updates))

        data.write(Vector(self.chats))

        data.write(Vector(self.users))

        data.write(self.intermediate_state.write())

        return data.getvalue()
