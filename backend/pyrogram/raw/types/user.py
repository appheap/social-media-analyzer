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


class User(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.User`.

    Details:
        - Layer: ``117``
        - ID: ``0x938458c1``

    Parameters:
        id: ``int`` ``32-bit``
        is_self (optional): ``bool``
        contact (optional): ``bool``
        mutual_contact (optional): ``bool``
        deleted (optional): ``bool``
        bot (optional): ``bool``
        bot_chat_history (optional): ``bool``
        bot_nochats (optional): ``bool``
        verified (optional): ``bool``
        restricted (optional): ``bool``
        min (optional): ``bool``
        bot_inline_geo (optional): ``bool``
        support (optional): ``bool``
        scam (optional): ``bool``
        apply_min_photo (optional): ``bool``
        access_hash (optional): ``int`` ``64-bit``
        first_name (optional): ``str``
        last_name (optional): ``str``
        username (optional): ``str``
        phone (optional): ``str``
        photo (optional): :obj:`UserProfilePhoto <pyrogram.raw.base.UserProfilePhoto>`
        status (optional): :obj:`UserStatus <pyrogram.raw.base.UserStatus>`
        bot_info_version (optional): ``int`` ``32-bit``
        restriction_reason (optional): List of :obj:`RestrictionReason <pyrogram.raw.base.RestrictionReason>`
        bot_inline_placeholder (optional): ``str``
        lang_code (optional): ``str``

    See Also:
        This object can be returned by 4 methods:

        .. hlist::
            :columns: 2

            - :obj:`account.UpdateProfile <pyrogram.raw.functions.account.UpdateProfile>`
            - :obj:`account.UpdateUsername <pyrogram.raw.functions.account.UpdateUsername>`
            - :obj:`account.ChangePhone <pyrogram.raw.functions.account.ChangePhone>`
            - :obj:`users.GetUsers <pyrogram.raw.functions.users.GetUsers>`
    """

    __slots__: List[str] = ["id", "is_self", "contact", "mutual_contact", "deleted", "bot", "bot_chat_history",
                            "bot_nochats", "verified", "restricted", "min", "bot_inline_geo", "support", "scam",
                            "apply_min_photo", "access_hash", "first_name", "last_name", "username", "phone", "photo",
                            "status", "bot_info_version", "restriction_reason", "bot_inline_placeholder", "lang_code"]

    ID = 0x938458c1
    QUALNAME = "types.User"

    def __init__(self, *, id: int, is_self: Union[None, bool] = None, contact: Union[None, bool] = None,
                 mutual_contact: Union[None, bool] = None, deleted: Union[None, bool] = None,
                 bot: Union[None, bool] = None, bot_chat_history: Union[None, bool] = None,
                 bot_nochats: Union[None, bool] = None, verified: Union[None, bool] = None,
                 restricted: Union[None, bool] = None, min: Union[None, bool] = None,
                 bot_inline_geo: Union[None, bool] = None, support: Union[None, bool] = None,
                 scam: Union[None, bool] = None, apply_min_photo: Union[None, bool] = None,
                 access_hash: Union[None, int] = None, first_name: Union[None, str] = None,
                 last_name: Union[None, str] = None, username: Union[None, str] = None, phone: Union[None, str] = None,
                 photo: "raw.base.UserProfilePhoto" = None, status: "raw.base.UserStatus" = None,
                 bot_info_version: Union[None, int] = None,
                 restriction_reason: Union[None, List["raw.base.RestrictionReason"]] = None,
                 bot_inline_placeholder: Union[None, str] = None, lang_code: Union[None, str] = None) -> None:
        self.id = id  # int
        self.is_self = is_self  # flags.10?true
        self.contact = contact  # flags.11?true
        self.mutual_contact = mutual_contact  # flags.12?true
        self.deleted = deleted  # flags.13?true
        self.bot = bot  # flags.14?true
        self.bot_chat_history = bot_chat_history  # flags.15?true
        self.bot_nochats = bot_nochats  # flags.16?true
        self.verified = verified  # flags.17?true
        self.restricted = restricted  # flags.18?true
        self.min = min  # flags.20?true
        self.bot_inline_geo = bot_inline_geo  # flags.21?true
        self.support = support  # flags.23?true
        self.scam = scam  # flags.24?true
        self.apply_min_photo = apply_min_photo  # flags.25?true
        self.access_hash = access_hash  # flags.0?long
        self.first_name = first_name  # flags.1?string
        self.last_name = last_name  # flags.2?string
        self.username = username  # flags.3?string
        self.phone = phone  # flags.4?string
        self.photo = photo  # flags.5?UserProfilePhoto
        self.status = status  # flags.6?UserStatus
        self.bot_info_version = bot_info_version  # flags.14?int
        self.restriction_reason = restriction_reason  # flags.18?Vector<RestrictionReason>
        self.bot_inline_placeholder = bot_inline_placeholder  # flags.19?string
        self.lang_code = lang_code  # flags.22?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "User":
        flags = Int.read(data)

        is_self = True if flags & (1 << 10) else False
        contact = True if flags & (1 << 11) else False
        mutual_contact = True if flags & (1 << 12) else False
        deleted = True if flags & (1 << 13) else False
        bot = True if flags & (1 << 14) else False
        bot_chat_history = True if flags & (1 << 15) else False
        bot_nochats = True if flags & (1 << 16) else False
        verified = True if flags & (1 << 17) else False
        restricted = True if flags & (1 << 18) else False
        min = True if flags & (1 << 20) else False
        bot_inline_geo = True if flags & (1 << 21) else False
        support = True if flags & (1 << 23) else False
        scam = True if flags & (1 << 24) else False
        apply_min_photo = True if flags & (1 << 25) else False
        id = Int.read(data)

        access_hash = Long.read(data) if flags & (1 << 0) else None
        first_name = String.read(data) if flags & (1 << 1) else None
        last_name = String.read(data) if flags & (1 << 2) else None
        username = String.read(data) if flags & (1 << 3) else None
        phone = String.read(data) if flags & (1 << 4) else None
        photo = TLObject.read(data) if flags & (1 << 5) else None

        status = TLObject.read(data) if flags & (1 << 6) else None

        bot_info_version = Int.read(data) if flags & (1 << 14) else None
        restriction_reason = TLObject.read(data) if flags & (1 << 18) else []

        bot_inline_placeholder = String.read(data) if flags & (1 << 19) else None
        lang_code = String.read(data) if flags & (1 << 22) else None
        return User(id=id, is_self=is_self, contact=contact, mutual_contact=mutual_contact, deleted=deleted, bot=bot,
                    bot_chat_history=bot_chat_history, bot_nochats=bot_nochats, verified=verified,
                    restricted=restricted, min=min, bot_inline_geo=bot_inline_geo, support=support, scam=scam,
                    apply_min_photo=apply_min_photo, access_hash=access_hash, first_name=first_name,
                    last_name=last_name, username=username, phone=phone, photo=photo, status=status,
                    bot_info_version=bot_info_version, restriction_reason=restriction_reason,
                    bot_inline_placeholder=bot_inline_placeholder, lang_code=lang_code)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.is_self is not None else 0
        flags |= (1 << 11) if self.contact is not None else 0
        flags |= (1 << 12) if self.mutual_contact is not None else 0
        flags |= (1 << 13) if self.deleted is not None else 0
        flags |= (1 << 14) if self.bot is not None else 0
        flags |= (1 << 15) if self.bot_chat_history is not None else 0
        flags |= (1 << 16) if self.bot_nochats is not None else 0
        flags |= (1 << 17) if self.verified is not None else 0
        flags |= (1 << 18) if self.restricted is not None else 0
        flags |= (1 << 20) if self.min is not None else 0
        flags |= (1 << 21) if self.bot_inline_geo is not None else 0
        flags |= (1 << 23) if self.support is not None else 0
        flags |= (1 << 24) if self.scam is not None else 0
        flags |= (1 << 25) if self.apply_min_photo is not None else 0
        flags |= (1 << 0) if self.access_hash is not None else 0
        flags |= (1 << 1) if self.first_name is not None else 0
        flags |= (1 << 2) if self.last_name is not None else 0
        flags |= (1 << 3) if self.username is not None else 0
        flags |= (1 << 4) if self.phone is not None else 0
        flags |= (1 << 5) if self.photo is not None else 0
        flags |= (1 << 6) if self.status is not None else 0
        flags |= (1 << 14) if self.bot_info_version is not None else 0
        flags |= (1 << 18) if self.restriction_reason is not None else 0
        flags |= (1 << 19) if self.bot_inline_placeholder is not None else 0
        flags |= (1 << 22) if self.lang_code is not None else 0
        data.write(Int(flags))

        data.write(Int(self.id))

        if self.access_hash is not None:
            data.write(Long(self.access_hash))

        if self.first_name is not None:
            data.write(String(self.first_name))

        if self.last_name is not None:
            data.write(String(self.last_name))

        if self.username is not None:
            data.write(String(self.username))

        if self.phone is not None:
            data.write(String(self.phone))

        if self.photo is not None:
            data.write(self.photo.write())

        if self.status is not None:
            data.write(self.status.write())

        if self.bot_info_version is not None:
            data.write(Int(self.bot_info_version))

        if self.restriction_reason is not None:
            data.write(Vector(self.restriction_reason))

        if self.bot_inline_placeholder is not None:
            data.write(String(self.bot_inline_placeholder))

        if self.lang_code is not None:
            data.write(String(self.lang_code))

        return data.getvalue()
