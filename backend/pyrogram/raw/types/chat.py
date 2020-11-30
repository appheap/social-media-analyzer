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


class Chat(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Chat`.

    Details:
        - Layer: ``117``
        - ID: ``0x3bda1bde``

    Parameters:
        id: ``int`` ``32-bit``
        title: ``str``
        photo: :obj:`ChatPhoto <pyrogram.raw.base.ChatPhoto>`
        participants_count: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        version: ``int`` ``32-bit``
        creator (optional): ``bool``
        kicked (optional): ``bool``
        left (optional): ``bool``
        deactivated (optional): ``bool``
        migrated_to (optional): :obj:`InputChannel <pyrogram.raw.base.InputChannel>`
        admin_rights (optional): :obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`
        default_banned_rights (optional): :obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`
    """

    __slots__: List[str] = ["id", "title", "photo", "participants_count", "date", "version", "creator", "kicked",
                            "left", "deactivated", "migrated_to", "admin_rights", "default_banned_rights"]

    ID = 0x3bda1bde
    QUALNAME = "types.Chat"

    def __init__(self, *, id: int, title: str, photo: "raw.base.ChatPhoto", participants_count: int, date: int,
                 version: int, creator: Union[None, bool] = None, kicked: Union[None, bool] = None,
                 left: Union[None, bool] = None, deactivated: Union[None, bool] = None,
                 migrated_to: "raw.base.InputChannel" = None, admin_rights: "raw.base.ChatAdminRights" = None,
                 default_banned_rights: "raw.base.ChatBannedRights" = None) -> None:
        self.id = id  # int
        self.title = title  # string
        self.photo = photo  # ChatPhoto
        self.participants_count = participants_count  # int
        self.date = date  # int
        self.version = version  # int
        self.creator = creator  # flags.0?true
        self.kicked = kicked  # flags.1?true
        self.left = left  # flags.2?true
        self.deactivated = deactivated  # flags.5?true
        self.migrated_to = migrated_to  # flags.6?InputChannel
        self.admin_rights = admin_rights  # flags.14?ChatAdminRights
        self.default_banned_rights = default_banned_rights  # flags.18?ChatBannedRights

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Chat":
        flags = Int.read(data)

        creator = True if flags & (1 << 0) else False
        kicked = True if flags & (1 << 1) else False
        left = True if flags & (1 << 2) else False
        deactivated = True if flags & (1 << 5) else False
        id = Int.read(data)

        title = String.read(data)

        photo = TLObject.read(data)

        participants_count = Int.read(data)

        date = Int.read(data)

        version = Int.read(data)

        migrated_to = TLObject.read(data) if flags & (1 << 6) else None

        admin_rights = TLObject.read(data) if flags & (1 << 14) else None

        default_banned_rights = TLObject.read(data) if flags & (1 << 18) else None

        return Chat(id=id, title=title, photo=photo, participants_count=participants_count, date=date, version=version,
                    creator=creator, kicked=kicked, left=left, deactivated=deactivated, migrated_to=migrated_to,
                    admin_rights=admin_rights, default_banned_rights=default_banned_rights)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator is not None else 0
        flags |= (1 << 1) if self.kicked is not None else 0
        flags |= (1 << 2) if self.left is not None else 0
        flags |= (1 << 5) if self.deactivated is not None else 0
        flags |= (1 << 6) if self.migrated_to is not None else 0
        flags |= (1 << 14) if self.admin_rights is not None else 0
        flags |= (1 << 18) if self.default_banned_rights is not None else 0
        data.write(Int(flags))

        data.write(Int(self.id))

        data.write(String(self.title))

        data.write(self.photo.write())

        data.write(Int(self.participants_count))

        data.write(Int(self.date))

        data.write(Int(self.version))

        if self.migrated_to is not None:
            data.write(self.migrated_to.write())

        if self.admin_rights is not None:
            data.write(self.admin_rights.write())

        if self.default_banned_rights is not None:
            data.write(self.default_banned_rights.write())

        return data.getvalue()
