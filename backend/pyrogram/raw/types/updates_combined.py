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


class UpdatesCombined(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Updates`.

    Details:
        - Layer: ``117``
        - ID: ``0x725b04c3``

    Parameters:
        updates: List of :obj:`Update <pyrogram.raw.base.Update>`
        users: List of :obj:`User <pyrogram.raw.base.User>`
        chats: List of :obj:`Chat <pyrogram.raw.base.Chat>`
        date: ``int`` ``32-bit``
        seq_start: ``int`` ``32-bit``
        seq: ``int`` ``32-bit``

    See Also:
        This object can be returned by 46 methods:

        .. hlist::
            :columns: 2

            - :obj:`account.GetNotifyExceptions <pyrogram.raw.functions.account.GetNotifyExceptions>`
            - :obj:`contacts.DeleteContacts <pyrogram.raw.functions.contacts.DeleteContacts>`
            - :obj:`contacts.AddContact <pyrogram.raw.functions.contacts.AddContact>`
            - :obj:`contacts.AcceptContact <pyrogram.raw.functions.contacts.AcceptContact>`
            - :obj:`contacts.GetLocated <pyrogram.raw.functions.contacts.GetLocated>`
            - :obj:`messages.SendMessage <pyrogram.raw.functions.messages.SendMessage>`
            - :obj:`messages.SendMedia <pyrogram.raw.functions.messages.SendMedia>`
            - :obj:`messages.ForwardMessages <pyrogram.raw.functions.messages.ForwardMessages>`
            - :obj:`messages.EditChatTitle <pyrogram.raw.functions.messages.EditChatTitle>`
            - :obj:`messages.EditChatPhoto <pyrogram.raw.functions.messages.EditChatPhoto>`
            - :obj:`messages.AddChatUser <pyrogram.raw.functions.messages.AddChatUser>`
            - :obj:`messages.DeleteChatUser <pyrogram.raw.functions.messages.DeleteChatUser>`
            - :obj:`messages.CreateChat <pyrogram.raw.functions.messages.CreateChat>`
            - :obj:`messages.ImportChatInvite <pyrogram.raw.functions.messages.ImportChatInvite>`
            - :obj:`messages.StartBot <pyrogram.raw.functions.messages.StartBot>`
            - :obj:`messages.MigrateChat <pyrogram.raw.functions.messages.MigrateChat>`
            - :obj:`messages.SendInlineBotResult <pyrogram.raw.functions.messages.SendInlineBotResult>`
            - :obj:`messages.EditMessage <pyrogram.raw.functions.messages.EditMessage>`
            - :obj:`messages.GetAllDrafts <pyrogram.raw.functions.messages.GetAllDrafts>`
            - :obj:`messages.SetGameScore <pyrogram.raw.functions.messages.SetGameScore>`
            - :obj:`messages.SendScreenshotNotification <pyrogram.raw.functions.messages.SendScreenshotNotification>`
            - :obj:`messages.SendMultiMedia <pyrogram.raw.functions.messages.SendMultiMedia>`
            - :obj:`messages.UpdatePinnedMessage <pyrogram.raw.functions.messages.UpdatePinnedMessage>`
            - :obj:`messages.SendVote <pyrogram.raw.functions.messages.SendVote>`
            - :obj:`messages.GetPollResults <pyrogram.raw.functions.messages.GetPollResults>`
            - :obj:`messages.EditChatDefaultBannedRights <pyrogram.raw.functions.messages.EditChatDefaultBannedRights>`
            - :obj:`messages.SendScheduledMessages <pyrogram.raw.functions.messages.SendScheduledMessages>`
            - :obj:`messages.DeleteScheduledMessages <pyrogram.raw.functions.messages.DeleteScheduledMessages>`
            - :obj:`help.GetAppChangelog <pyrogram.raw.functions.help.GetAppChangelog>`
            - :obj:`channels.CreateChannel <pyrogram.raw.functions.channels.CreateChannel>`
            - :obj:`channels.EditAdmin <pyrogram.raw.functions.channels.EditAdmin>`
            - :obj:`channels.EditTitle <pyrogram.raw.functions.channels.EditTitle>`
            - :obj:`channels.EditPhoto <pyrogram.raw.functions.channels.EditPhoto>`
            - :obj:`channels.JoinChannel <pyrogram.raw.functions.channels.JoinChannel>`
            - :obj:`channels.LeaveChannel <pyrogram.raw.functions.channels.LeaveChannel>`
            - :obj:`channels.InviteToChannel <pyrogram.raw.functions.channels.InviteToChannel>`
            - :obj:`channels.DeleteChannel <pyrogram.raw.functions.channels.DeleteChannel>`
            - :obj:`channels.ToggleSignatures <pyrogram.raw.functions.channels.ToggleSignatures>`
            - :obj:`channels.EditBanned <pyrogram.raw.functions.channels.EditBanned>`
            - :obj:`channels.TogglePreHistoryHidden <pyrogram.raw.functions.channels.TogglePreHistoryHidden>`
            - :obj:`channels.EditCreator <pyrogram.raw.functions.channels.EditCreator>`
            - :obj:`channels.ToggleSlowMode <pyrogram.raw.functions.channels.ToggleSlowMode>`
            - :obj:`phone.DiscardCall <pyrogram.raw.functions.phone.DiscardCall>`
            - :obj:`phone.SetCallRating <pyrogram.raw.functions.phone.SetCallRating>`
            - :obj:`folders.EditPeerFolders <pyrogram.raw.functions.folders.EditPeerFolders>`
            - :obj:`folders.DeleteFolder <pyrogram.raw.functions.folders.DeleteFolder>`
    """

    __slots__: List[str] = ["updates", "users", "chats", "date", "seq_start", "seq"]

    ID = 0x725b04c3
    QUALNAME = "types.UpdatesCombined"

    def __init__(self, *, updates: List["raw.base.Update"], users: List["raw.base.User"], chats: List["raw.base.Chat"],
                 date: int, seq_start: int, seq: int) -> None:
        self.updates = updates  # Vector<Update>
        self.users = users  # Vector<User>
        self.chats = chats  # Vector<Chat>
        self.date = date  # int
        self.seq_start = seq_start  # int
        self.seq = seq  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdatesCombined":
        # No flags

        updates = TLObject.read(data)

        users = TLObject.read(data)

        chats = TLObject.read(data)

        date = Int.read(data)

        seq_start = Int.read(data)

        seq = Int.read(data)

        return UpdatesCombined(updates=updates, users=users, chats=chats, date=date, seq_start=seq_start, seq=seq)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Vector(self.updates))

        data.write(Vector(self.users))

        data.write(Vector(self.chats))

        data.write(Int(self.date))

        data.write(Int(self.seq_start))

        data.write(Int(self.seq))

        return data.getvalue()
