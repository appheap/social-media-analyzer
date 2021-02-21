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


class UserFull(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.UserFull`.

    Details:
        - Layer: ``123``
        - ID: ``0xedf17c12``

    Parameters:
        user: :obj:`User <pyrogram.raw.base.User>`
        settings: :obj:`PeerSettings <pyrogram.raw.base.PeerSettings>`
        notify_settings: :obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`
        common_chats_count: ``int`` ``32-bit``
        blocked (optional): ``bool``
        phone_calls_available (optional): ``bool``
        phone_calls_private (optional): ``bool``
        can_pin_message (optional): ``bool``
        has_scheduled (optional): ``bool``
        video_calls_available (optional): ``bool``
        about (optional): ``str``
        profile_photo (optional): :obj:`Photo <pyrogram.raw.base.Photo>`
        bot_info (optional): :obj:`BotInfo <pyrogram.raw.base.BotInfo>`
        pinned_msg_id (optional): ``int`` ``32-bit``
        folder_id (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`users.GetFullUser <pyrogram.raw.functions.users.GetFullUser>`
    """

    __slots__: List[str] = ["user", "settings", "notify_settings", "common_chats_count", "blocked",
                            "phone_calls_available", "phone_calls_private", "can_pin_message", "has_scheduled",
                            "video_calls_available", "about", "profile_photo", "bot_info", "pinned_msg_id", "folder_id"]

    ID = 0xedf17c12
    QUALNAME = "types.UserFull"

    def __init__(self, *, user: "raw.base.User", settings: "raw.base.PeerSettings",
                 notify_settings: "raw.base.PeerNotifySettings", common_chats_count: int,
                 blocked: Union[None, bool] = None, phone_calls_available: Union[None, bool] = None,
                 phone_calls_private: Union[None, bool] = None, can_pin_message: Union[None, bool] = None,
                 has_scheduled: Union[None, bool] = None, video_calls_available: Union[None, bool] = None,
                 about: Union[None, str] = None, profile_photo: "raw.base.Photo" = None,
                 bot_info: "raw.base.BotInfo" = None, pinned_msg_id: Union[None, int] = None,
                 folder_id: Union[None, int] = None) -> None:
        self.user = user  # User
        self.settings = settings  # PeerSettings
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.common_chats_count = common_chats_count  # int
        self.blocked = blocked  # flags.0?true
        self.phone_calls_available = phone_calls_available  # flags.4?true
        self.phone_calls_private = phone_calls_private  # flags.5?true
        self.can_pin_message = can_pin_message  # flags.7?true
        self.has_scheduled = has_scheduled  # flags.12?true
        self.video_calls_available = video_calls_available  # flags.13?true
        self.about = about  # flags.1?string
        self.profile_photo = profile_photo  # flags.2?Photo
        self.bot_info = bot_info  # flags.3?BotInfo
        self.pinned_msg_id = pinned_msg_id  # flags.6?int
        self.folder_id = folder_id  # flags.11?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "UserFull":
        flags = Int.read(data)

        blocked = True if flags & (1 << 0) else False
        phone_calls_available = True if flags & (1 << 4) else False
        phone_calls_private = True if flags & (1 << 5) else False
        can_pin_message = True if flags & (1 << 7) else False
        has_scheduled = True if flags & (1 << 12) else False
        video_calls_available = True if flags & (1 << 13) else False
        user = TLObject.read(data)

        about = String.read(data) if flags & (1 << 1) else None
        settings = TLObject.read(data)

        profile_photo = TLObject.read(data) if flags & (1 << 2) else None

        notify_settings = TLObject.read(data)

        bot_info = TLObject.read(data) if flags & (1 << 3) else None

        pinned_msg_id = Int.read(data) if flags & (1 << 6) else None
        common_chats_count = Int.read(data)

        folder_id = Int.read(data) if flags & (1 << 11) else None
        return UserFull(user=user, settings=settings, notify_settings=notify_settings,
                        common_chats_count=common_chats_count, blocked=blocked,
                        phone_calls_available=phone_calls_available, phone_calls_private=phone_calls_private,
                        can_pin_message=can_pin_message, has_scheduled=has_scheduled,
                        video_calls_available=video_calls_available, about=about, profile_photo=profile_photo,
                        bot_info=bot_info, pinned_msg_id=pinned_msg_id, folder_id=folder_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.blocked else 0
        flags |= (1 << 4) if self.phone_calls_available else 0
        flags |= (1 << 5) if self.phone_calls_private else 0
        flags |= (1 << 7) if self.can_pin_message else 0
        flags |= (1 << 12) if self.has_scheduled else 0
        flags |= (1 << 13) if self.video_calls_available else 0
        flags |= (1 << 1) if self.about is not None else 0
        flags |= (1 << 2) if self.profile_photo is not None else 0
        flags |= (1 << 3) if self.bot_info is not None else 0
        flags |= (1 << 6) if self.pinned_msg_id is not None else 0
        flags |= (1 << 11) if self.folder_id is not None else 0
        data.write(Int(flags))

        data.write(self.user.write())

        if self.about is not None:
            data.write(String(self.about))

        data.write(self.settings.write())

        if self.profile_photo is not None:
            data.write(self.profile_photo.write())

        data.write(self.notify_settings.write())

        if self.bot_info is not None:
            data.write(self.bot_info.write())

        if self.pinned_msg_id is not None:
            data.write(Int(self.pinned_msg_id))

        data.write(Int(self.common_chats_count))

        if self.folder_id is not None:
            data.write(Int(self.folder_id))

        return data.getvalue()
