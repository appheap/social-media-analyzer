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


class Message(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Message`.

    Details:
        - Layer: ``121``
        - ID: ``0x58ae39c9``

    Parameters:
        id: ``int`` ``32-bit``
        from_id (optional): :obj:`Peer <pyrogram.raw.base.Peer>`
        to_id: :obj:`Peer <pyrogram.raw.base.Peer>`
        date: ``int`` ``32-bit``
        message: ``str``
        out (optional): ``bool``
        mentioned (optional): ``bool``
        media_unread (optional): ``bool``
        silent (optional): ``bool``
        post (optional): ``bool``
        from_scheduled (optional): ``bool``
        legacy (optional): ``bool``
        edit_hide (optional): ``bool``
        pinned (optional): ``bool``
        fwd_from (optional): :obj:`MessageFwdHeader <pyrogram.raw.base.MessageFwdHeader>`
        via_bot_id (optional): ``int`` ``32-bit``
        reply_to (optional): :obj:`MessageReplyHeader <pyrogram.raw.base.MessageReplyHeader>`
        media (optional): :obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`
        reply_markup (optional): :obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`
        entities (optional): List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`
        views (optional): ``int`` ``32-bit``
        forwards (optional): ``int`` ``32-bit``
        replies (optional): :obj:`MessageReplies <pyrogram.raw.base.MessageReplies>`
        edit_date (optional): ``int`` ``32-bit``
        post_author (optional): ``str``
        grouped_id (optional): ``int`` ``64-bit``
        restriction_reason (optional): List of :obj:`RestrictionReason <pyrogram.raw.base.RestrictionReason>`
    """

    __slots__: List[str] = ["out", "mentioned", "media_unread", "silent", "post", "from_scheduled", "legacy",
                            "edit_hide", "pinned", "id", "from_id", "to_id", "fwd_from", "via_bot_id", "reply_to",
                            "date", "message", "media", "reply_markup", "entities", "views", "forwards", "replies",
                            "edit_date", "post_author", "grouped_id", "restriction_reason",
                            ]
    ID = 0x58ae39c9
    QUALNAME = "types.Message"

    def __init__(
            self, *,
            id: int,
            from_id: Union[None, "raw.base.Peer"] = None,
            to_id: "raw.base.Peer" = None,
            date: int = None,
            message: str = None,

            out: Union[None, bool] = None,
            mentioned: Union[None, bool] = None,
            media_unread: Union[None, bool] = None,
            silent: Union[None, bool] = None,
            post: Union[None, bool] = None,
            from_scheduled: Union[None, bool] = None,
            legacy: Union[None, bool] = None,
            edit_hide: Union[None, bool] = None,
            pinned: Union[None, bool] = None,
            fwd_from: Union[None, "raw.base.MessageFwdHeader"] = None,
            via_bot_id: Union[None, int] = None,
            reply_to: Union[None, "raw.base.MessageReplyHeader"] = None,
            media: Union[None, "raw.base.MessageMedia"] = None,
            reply_markup: Union[None, "raw.base.ReplyMarkup"] = None,
            entities: Union[None, List["raw.base.MessageEntity"]] = None,
            views: Union[None, int] = None,
            forwards: Union[None, int] = None,
            replies: Union[None, "raw.base.MessageReplies"] = None,
            edit_date: Union[None, int] = None,
            post_author: Union[None, str] = None,
            grouped_id: Union[None, int] = None,
            restriction_reason: Union[None, List["raw.base.RestrictionReason"]] = None,

    ) -> None:

        self.id = id  # int
        self.from_id = from_id  # flags.8?Peer
        self.to_id = to_id  # Peer
        self.date = date  # int
        self.message = message  # string

        self.out = out  # flags.1?true
        self.mentioned = mentioned  # flags.4?true
        self.media_unread = media_unread  # flags.5?true
        self.silent = silent  # flags.13?true
        self.post = post  # flags.14?true
        self.from_scheduled = from_scheduled  # flags.18?true
        self.legacy = legacy  # flags.19?true
        self.edit_hide = edit_hide  # flags.21?true
        self.pinned = pinned  # flags.24?true
        self.fwd_from = fwd_from  # flags.2?MessageFwdHeader
        self.via_bot_id = via_bot_id  # flags.11?int
        self.reply_to = reply_to  # flags.3?MessageReplyHeader
        self.media = media  # flags.9?MessageMedia
        self.reply_markup = reply_markup  # flags.6?ReplyMarkup
        self.entities = entities  # flags.7?Vector<MessageEntity>
        self.views = views  # flags.10?int
        self.forwards = forwards  # flags.10?int
        self.replies = replies  # flags.23?MessageReplies
        self.edit_date = edit_date  # flags.15?int
        self.post_author = post_author  # flags.16?string
        self.grouped_id = grouped_id  # flags.17?long
        self.restriction_reason = restriction_reason  # flags.22?Vector<RestrictionReason>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Message":
        flags = Int.read(data)

        out = True if flags & (1 << 1) else False
        mentioned = True if flags & (1 << 4) else False
        media_unread = True if flags & (1 << 5) else False
        silent = True if flags & (1 << 13) else False
        post = True if flags & (1 << 14) else False
        from_scheduled = True if flags & (1 << 18) else False
        legacy = True if flags & (1 << 19) else False
        edit_hide = True if flags & (1 << 21) else False
        pinned = True if flags & (1 << 24) else False

        id = Int.read(data)
        from_id = TLObject.read(data) if flags & (1 << 8) else None
        to_id = TLObject.read(data)

        fwd_from = TLObject.read(data) if flags & (1 << 2) else None

        via_bot_id = Int.read(data) if flags & (1 << 11) else None
        reply_to = TLObject.read(data) if flags & (1 << 3) else None
        date = Int.read(data)

        message = String.read(data)

        media = TLObject.read(data) if flags & (1 << 9) else None

        reply_markup = TLObject.read(data) if flags & (1 << 6) else None

        entities = TLObject.read(data) if flags & (1 << 7) else []

        views = Int.read(data) if flags & (1 << 10) else None
        forwards = Int.read(data) if flags & (1 << 10) else None
        replies = TLObject.read(data) if flags & (1 << 23) else []
        edit_date = Int.read(data) if flags & (1 << 15) else None
        post_author = String.read(data) if flags & (1 << 16) else None
        grouped_id = Long.read(data) if flags & (1 << 17) else None
        restriction_reason = TLObject.read(data) if flags & (1 << 22) else []

        return Message(
            id=id,
            from_id=from_id,
            to_id=to_id,
            date=date,
            message=message,
            out=out,
            mentioned=mentioned,
            media_unread=media_unread,
            silent=silent,
            post=post,
            from_scheduled=from_scheduled,
            legacy=legacy,
            edit_hide=edit_hide,
            pinned=pinned,
            fwd_from=fwd_from,
            via_bot_id=via_bot_id,
            reply_to=reply_to,
            media=media,
            reply_markup=reply_markup,
            entities=entities,
            views=views,
            forwards=forwards,
            replies=replies,
            edit_date=edit_date,
            post_author=post_author,
            grouped_id=grouped_id,
            restriction_reason=restriction_reason,
        )

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.out is not None else 0
        flags |= (1 << 4) if self.mentioned is not None else 0
        flags |= (1 << 5) if self.media_unread is not None else 0
        flags |= (1 << 13) if self.silent is not None else 0
        flags |= (1 << 14) if self.post is not None else 0
        flags |= (1 << 18) if self.from_scheduled is not None else 0
        flags |= (1 << 19) if self.legacy is not None else 0
        flags |= (1 << 21) if self.edit_hide is not None else 0
        flags |= (1 << 24) if self.pinned is not None else 0
        flags |= (1 << 8) if self.from_id is not None else 0
        flags |= (1 << 2) if self.fwd_from is not None else 0
        flags |= (1 << 11) if self.via_bot_id is not None else 0
        flags |= (1 << 3) if self.reply_to is not None else 0
        flags |= (1 << 9) if self.media is not None else 0
        flags |= (1 << 6) if self.reply_markup is not None else 0
        flags |= (1 << 7) if self.entities is not None else 0
        flags |= (1 << 10) if self.views is not None and self.forwards is not None else 0
        flags |= (1 << 15) if self.edit_date is not None else 0
        flags |= (1 << 16) if self.post_author is not None else 0
        flags |= (1 << 17) if self.grouped_id is not None else 0
        flags |= (1 << 22) if self.restriction_reason is not None else 0
        data.write(Int(flags))

        data.write(Int(self.id))

        if self.from_id is not None:
            data.write(Int(self.from_id))

        data.write(self.to_id.write())

        if self.fwd_from is not None:
            data.write(self.fwd_from.write())

        if self.via_bot_id is not None:
            data.write(Int(self.via_bot_id))

        if self.reply_to is not None:
            data.write(self.reply_to.write())

        data.write(Int(self.date))

        data.write(String(self.message))

        if self.media is not None:
            data.write(self.media.write())

        if self.reply_markup is not None:
            data.write(self.reply_markup.write())

        if self.entities is not None:
            data.write(Vector(self.entities))

        if self.views is not None:
            data.write(Int(self.views))

        if self.forwards is not None:
            data.write(Int(self.forwards))

        if self.replies is not None:
            data.write(self.replies.write())

        if self.edit_date is not None:
            data.write(Int(self.edit_date))

        if self.post_author is not None:
            data.write(String(self.post_author))

        if self.grouped_id is not None:
            data.write(Long(self.grouped_id))

        if self.restriction_reason is not None:
            data.write(Vector(self.restriction_reason))

        return data.getvalue()
