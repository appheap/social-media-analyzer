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


class UpdateShortMessage(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Updates`.

    Details:
        - Layer: ``120``
        - ID: ``0x2296d2c8``

    Parameters:
        id: ``int`` ``32-bit``
        user_id: ``int`` ``32-bit``
        message: ``str``
        pts: ``int`` ``32-bit``
        pts_count: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        out (optional): ``bool``
        mentioned (optional): ``bool``
        media_unread (optional): ``bool``
        silent (optional): ``bool``
        fwd_from (optional): :obj:`MessageFwdHeader <pyrogram.raw.base.MessageFwdHeader>`
        via_bot_id (optional): ``int`` ``32-bit``
        reply_to (optional): :obj:`MessageReplyHeader <pyrogram.raw.base.MessageReplyHeader>`
        entities (optional): List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`

    See Also:
        This object can be returned by 47 methods:

        .. hlist::
            :columns: 2

            - :obj:`account.GetNotifyExceptions <pyrogram.raw.functions.account.GetNotifyExceptions>`
            - :obj:`contacts.DeleteContacts <pyrogram.raw.functions.contacts.DeleteContacts>`
            - :obj:`contacts.AddContact <pyrogram.raw.functions.contacts.AddContact>`
            - :obj:`contacts.AcceptContact <pyrogram.raw.functions.contacts.AcceptContact>`
            - :obj:`contacts.GetLocated <pyrogram.raw.functions.contacts.GetLocated>`
            - :obj:`contacts.BlockFromReplies <pyrogram.raw.functions.contacts.BlockFromReplies>`
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

    __slots__: List[str] = ["id", "user_id", "message", "pts", "pts_count", "date", "out", "mentioned", "media_unread",
                            "silent", "fwd_from", "via_bot_id", "reply_to", "entities"]

    ID = 0x2296d2c8
    QUALNAME = "types.UpdateShortMessage"

    def __init__(self, *, id: int, user_id: int, message: str, pts: int, pts_count: int, date: int,
                 out: Union[None, bool] = None, mentioned: Union[None, bool] = None,
                 media_unread: Union[None, bool] = None, silent: Union[None, bool] = None,
                 fwd_from: "raw.base.MessageFwdHeader" = None, via_bot_id: Union[None, int] = None,
                 reply_to: "raw.base.MessageReplyHeader" = None,
                 entities: Union[None, List["raw.base.MessageEntity"]] = None) -> None:
        self.id = id  # int
        self.user_id = user_id  # int
        self.message = message  # string
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.date = date  # int
        self.out = out  # flags.1?true
        self.mentioned = mentioned  # flags.4?true
        self.media_unread = media_unread  # flags.5?true
        self.silent = silent  # flags.13?true
        self.fwd_from = fwd_from  # flags.2?MessageFwdHeader
        self.via_bot_id = via_bot_id  # flags.11?int
        self.reply_to = reply_to  # flags.3?MessageReplyHeader
        self.entities = entities  # flags.7?Vector<MessageEntity>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UpdateShortMessage":
        flags = Int.read(data)

        out = True if flags & (1 << 1) else False
        mentioned = True if flags & (1 << 4) else False
        media_unread = True if flags & (1 << 5) else False
        silent = True if flags & (1 << 13) else False
        id = Int.read(data)

        user_id = Int.read(data)

        message = String.read(data)

        pts = Int.read(data)

        pts_count = Int.read(data)

        date = Int.read(data)

        fwd_from = TLObject.read(data) if flags & (1 << 2) else None

        via_bot_id = Int.read(data) if flags & (1 << 11) else None
        reply_to = TLObject.read(data) if flags & (1 << 3) else None

        entities = TLObject.read(data) if flags & (1 << 7) else []

        return UpdateShortMessage(id=id, user_id=user_id, message=message, pts=pts, pts_count=pts_count, date=date,
                                  out=out, mentioned=mentioned, media_unread=media_unread, silent=silent,
                                  fwd_from=fwd_from, via_bot_id=via_bot_id, reply_to=reply_to, entities=entities)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.out is not None else 0
        flags |= (1 << 4) if self.mentioned is not None else 0
        flags |= (1 << 5) if self.media_unread is not None else 0
        flags |= (1 << 13) if self.silent is not None else 0
        flags |= (1 << 2) if self.fwd_from is not None else 0
        flags |= (1 << 11) if self.via_bot_id is not None else 0
        flags |= (1 << 3) if self.reply_to is not None else 0
        flags |= (1 << 7) if self.entities is not None else 0
        data.write(Int(flags))

        data.write(Int(self.id))

        data.write(Int(self.user_id))

        data.write(String(self.message))

        data.write(Int(self.pts))

        data.write(Int(self.pts_count))

        data.write(Int(self.date))

        if self.fwd_from is not None:
            data.write(self.fwd_from.write())

        if self.via_bot_id is not None:
            data.write(Int(self.via_bot_id))

        if self.reply_to is not None:
            data.write(self.reply_to.write())

        if self.entities is not None:
            data.write(Vector(self.entities))

        return data.getvalue()
