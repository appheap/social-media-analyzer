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


class ChannelFull(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChatFull`.

    Details:
        - Layer: ``120``
        - ID: ``0xf0e6672a``

    Parameters:
        id: ``int`` ``32-bit``
        about: ``str``
        read_inbox_max_id: ``int`` ``32-bit``
        read_outbox_max_id: ``int`` ``32-bit``
        unread_count: ``int`` ``32-bit``
        chat_photo: :obj:`Photo <pyrogram.raw.base.Photo>`
        notify_settings: :obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`
        exported_invite: :obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`
        bot_info: List of :obj:`BotInfo <pyrogram.raw.base.BotInfo>`
        pts: ``int`` ``32-bit``
        can_view_participants (optional): ``bool``
        can_set_username (optional): ``bool``
        can_set_stickers (optional): ``bool``
        hidden_prehistory (optional): ``bool``
        can_set_location (optional): ``bool``
        has_scheduled (optional): ``bool``
        can_view_stats (optional): ``bool``
        blocked (optional): ``bool``
        participants_count (optional): ``int`` ``32-bit``
        admins_count (optional): ``int`` ``32-bit``
        kicked_count (optional): ``int`` ``32-bit``
        banned_count (optional): ``int`` ``32-bit``
        online_count (optional): ``int`` ``32-bit``
        migrated_from_chat_id (optional): ``int`` ``32-bit``
        migrated_from_max_id (optional): ``int`` ``32-bit``
        pinned_msg_id (optional): ``int`` ``32-bit``
        stickerset (optional): :obj:`StickerSet <pyrogram.raw.base.StickerSet>`
        available_min_id (optional): ``int`` ``32-bit``
        folder_id (optional): ``int`` ``32-bit``
        linked_chat_id (optional): ``int`` ``32-bit``
        location (optional): :obj:`ChannelLocation <pyrogram.raw.base.ChannelLocation>`
        slowmode_seconds (optional): ``int`` ``32-bit``
        slowmode_next_send_date (optional): ``int`` ``32-bit``
        stats_dc (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["id", "about", "read_inbox_max_id", "read_outbox_max_id", "unread_count", "chat_photo",
                            "notify_settings", "exported_invite", "bot_info", "pts", "can_view_participants",
                            "can_set_username", "can_set_stickers", "hidden_prehistory", "can_set_location",
                            "has_scheduled", "can_view_stats", "blocked", "participants_count", "admins_count",
                            "kicked_count", "banned_count", "online_count", "migrated_from_chat_id",
                            "migrated_from_max_id", "pinned_msg_id", "stickerset", "available_min_id", "folder_id",
                            "linked_chat_id", "location", "slowmode_seconds", "slowmode_next_send_date", "stats_dc"]

    ID = 0xf0e6672a
    QUALNAME = "types.ChannelFull"

    def __init__(self, *, id: int, about: str, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int,
                 chat_photo: "raw.base.Photo", notify_settings: "raw.base.PeerNotifySettings",
                 exported_invite: "raw.base.ExportedChatInvite", bot_info: List["raw.base.BotInfo"], pts: int,
                 can_view_participants: Union[None, bool] = None, can_set_username: Union[None, bool] = None,
                 can_set_stickers: Union[None, bool] = None, hidden_prehistory: Union[None, bool] = None,
                 can_set_location: Union[None, bool] = None, has_scheduled: Union[None, bool] = None,
                 can_view_stats: Union[None, bool] = None, blocked: Union[None, bool] = None,
                 participants_count: Union[None, int] = None, admins_count: Union[None, int] = None,
                 kicked_count: Union[None, int] = None, banned_count: Union[None, int] = None,
                 online_count: Union[None, int] = None, migrated_from_chat_id: Union[None, int] = None,
                 migrated_from_max_id: Union[None, int] = None, pinned_msg_id: Union[None, int] = None,
                 stickerset: "raw.base.StickerSet" = None, available_min_id: Union[None, int] = None,
                 folder_id: Union[None, int] = None, linked_chat_id: Union[None, int] = None,
                 location: "raw.base.ChannelLocation" = None, slowmode_seconds: Union[None, int] = None,
                 slowmode_next_send_date: Union[None, int] = None, stats_dc: Union[None, int] = None) -> None:
        self.id = id  # int
        self.about = about  # string
        self.read_inbox_max_id = read_inbox_max_id  # int
        self.read_outbox_max_id = read_outbox_max_id  # int
        self.unread_count = unread_count  # int
        self.chat_photo = chat_photo  # Photo
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.exported_invite = exported_invite  # ExportedChatInvite
        self.bot_info = bot_info  # Vector<BotInfo>
        self.pts = pts  # int
        self.can_view_participants = can_view_participants  # flags.3?true
        self.can_set_username = can_set_username  # flags.6?true
        self.can_set_stickers = can_set_stickers  # flags.7?true
        self.hidden_prehistory = hidden_prehistory  # flags.10?true
        self.can_set_location = can_set_location  # flags.16?true
        self.has_scheduled = has_scheduled  # flags.19?true
        self.can_view_stats = can_view_stats  # flags.20?true
        self.blocked = blocked  # flags.22?true
        self.participants_count = participants_count  # flags.0?int
        self.admins_count = admins_count  # flags.1?int
        self.kicked_count = kicked_count  # flags.2?int
        self.banned_count = banned_count  # flags.2?int
        self.online_count = online_count  # flags.13?int
        self.migrated_from_chat_id = migrated_from_chat_id  # flags.4?int
        self.migrated_from_max_id = migrated_from_max_id  # flags.4?int
        self.pinned_msg_id = pinned_msg_id  # flags.5?int
        self.stickerset = stickerset  # flags.8?StickerSet
        self.available_min_id = available_min_id  # flags.9?int
        self.folder_id = folder_id  # flags.11?int
        self.linked_chat_id = linked_chat_id  # flags.14?int
        self.location = location  # flags.15?ChannelLocation
        self.slowmode_seconds = slowmode_seconds  # flags.17?int
        self.slowmode_next_send_date = slowmode_next_send_date  # flags.18?int
        self.stats_dc = stats_dc  # flags.12?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChannelFull":
        flags = Int.read(data)

        can_view_participants = True if flags & (1 << 3) else False
        can_set_username = True if flags & (1 << 6) else False
        can_set_stickers = True if flags & (1 << 7) else False
        hidden_prehistory = True if flags & (1 << 10) else False
        can_set_location = True if flags & (1 << 16) else False
        has_scheduled = True if flags & (1 << 19) else False
        can_view_stats = True if flags & (1 << 20) else False
        blocked = True if flags & (1 << 22) else False
        id = Int.read(data)

        about = String.read(data)

        participants_count = Int.read(data) if flags & (1 << 0) else None
        admins_count = Int.read(data) if flags & (1 << 1) else None
        kicked_count = Int.read(data) if flags & (1 << 2) else None
        banned_count = Int.read(data) if flags & (1 << 2) else None
        online_count = Int.read(data) if flags & (1 << 13) else None
        read_inbox_max_id = Int.read(data)

        read_outbox_max_id = Int.read(data)

        unread_count = Int.read(data)

        chat_photo = TLObject.read(data)

        notify_settings = TLObject.read(data)

        exported_invite = TLObject.read(data)

        bot_info = TLObject.read(data)

        migrated_from_chat_id = Int.read(data) if flags & (1 << 4) else None
        migrated_from_max_id = Int.read(data) if flags & (1 << 4) else None
        pinned_msg_id = Int.read(data) if flags & (1 << 5) else None
        stickerset = TLObject.read(data) if flags & (1 << 8) else None

        available_min_id = Int.read(data) if flags & (1 << 9) else None
        folder_id = Int.read(data) if flags & (1 << 11) else None
        linked_chat_id = Int.read(data) if flags & (1 << 14) else None
        location = TLObject.read(data) if flags & (1 << 15) else None

        slowmode_seconds = Int.read(data) if flags & (1 << 17) else None
        slowmode_next_send_date = Int.read(data) if flags & (1 << 18) else None
        stats_dc = Int.read(data) if flags & (1 << 12) else None
        pts = Int.read(data)

        return ChannelFull(id=id, about=about, read_inbox_max_id=read_inbox_max_id,
                           read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, chat_photo=chat_photo,
                           notify_settings=notify_settings, exported_invite=exported_invite, bot_info=bot_info, pts=pts,
                           can_view_participants=can_view_participants, can_set_username=can_set_username,
                           can_set_stickers=can_set_stickers, hidden_prehistory=hidden_prehistory,
                           can_set_location=can_set_location, has_scheduled=has_scheduled,
                           can_view_stats=can_view_stats, blocked=blocked, participants_count=participants_count,
                           admins_count=admins_count, kicked_count=kicked_count, banned_count=banned_count,
                           online_count=online_count, migrated_from_chat_id=migrated_from_chat_id,
                           migrated_from_max_id=migrated_from_max_id, pinned_msg_id=pinned_msg_id,
                           stickerset=stickerset, available_min_id=available_min_id, folder_id=folder_id,
                           linked_chat_id=linked_chat_id, location=location, slowmode_seconds=slowmode_seconds,
                           slowmode_next_send_date=slowmode_next_send_date, stats_dc=stats_dc)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.can_view_participants is not None else 0
        flags |= (1 << 6) if self.can_set_username is not None else 0
        flags |= (1 << 7) if self.can_set_stickers is not None else 0
        flags |= (1 << 10) if self.hidden_prehistory is not None else 0
        flags |= (1 << 16) if self.can_set_location is not None else 0
        flags |= (1 << 19) if self.has_scheduled is not None else 0
        flags |= (1 << 20) if self.can_view_stats is not None else 0
        flags |= (1 << 22) if self.blocked is not None else 0
        flags |= (1 << 0) if self.participants_count is not None else 0
        flags |= (1 << 1) if self.admins_count is not None else 0
        flags |= (1 << 2) if self.kicked_count is not None else 0
        flags |= (1 << 2) if self.banned_count is not None else 0
        flags |= (1 << 13) if self.online_count is not None else 0
        flags |= (1 << 4) if self.migrated_from_chat_id is not None else 0
        flags |= (1 << 4) if self.migrated_from_max_id is not None else 0
        flags |= (1 << 5) if self.pinned_msg_id is not None else 0
        flags |= (1 << 8) if self.stickerset is not None else 0
        flags |= (1 << 9) if self.available_min_id is not None else 0
        flags |= (1 << 11) if self.folder_id is not None else 0
        flags |= (1 << 14) if self.linked_chat_id is not None else 0
        flags |= (1 << 15) if self.location is not None else 0
        flags |= (1 << 17) if self.slowmode_seconds is not None else 0
        flags |= (1 << 18) if self.slowmode_next_send_date is not None else 0
        flags |= (1 << 12) if self.stats_dc is not None else 0
        data.write(Int(flags))

        data.write(Int(self.id))

        data.write(String(self.about))

        if self.participants_count is not None:
            data.write(Int(self.participants_count))

        if self.admins_count is not None:
            data.write(Int(self.admins_count))

        if self.kicked_count is not None:
            data.write(Int(self.kicked_count))

        if self.banned_count is not None:
            data.write(Int(self.banned_count))

        if self.online_count is not None:
            data.write(Int(self.online_count))

        data.write(Int(self.read_inbox_max_id))

        data.write(Int(self.read_outbox_max_id))

        data.write(Int(self.unread_count))

        data.write(self.chat_photo.write())

        data.write(self.notify_settings.write())

        data.write(self.exported_invite.write())

        data.write(Vector(self.bot_info))

        if self.migrated_from_chat_id is not None:
            data.write(Int(self.migrated_from_chat_id))

        if self.migrated_from_max_id is not None:
            data.write(Int(self.migrated_from_max_id))

        if self.pinned_msg_id is not None:
            data.write(Int(self.pinned_msg_id))

        if self.stickerset is not None:
            data.write(self.stickerset.write())

        if self.available_min_id is not None:
            data.write(Int(self.available_min_id))

        if self.folder_id is not None:
            data.write(Int(self.folder_id))

        if self.linked_chat_id is not None:
            data.write(Int(self.linked_chat_id))

        if self.location is not None:
            data.write(self.location.write())

        if self.slowmode_seconds is not None:
            data.write(Int(self.slowmode_seconds))

        if self.slowmode_next_send_date is not None:
            data.write(Int(self.slowmode_next_send_date))

        if self.stats_dc is not None:
            data.write(Int(self.stats_dc))

        data.write(Int(self.pts))

        return data.getvalue()
