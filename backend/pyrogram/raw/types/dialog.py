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


class Dialog(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Dialog`.

    Details:
        - Layer: ``120``
        - ID: ``0x2c171f72``

    Parameters:
        peer: :obj:`Peer <pyrogram.raw.base.Peer>`
        top_message: ``int`` ``32-bit``
        read_inbox_max_id: ``int`` ``32-bit``
        read_outbox_max_id: ``int`` ``32-bit``
        unread_count: ``int`` ``32-bit``
        unread_mentions_count: ``int`` ``32-bit``
        notify_settings: :obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`
        pinned (optional): ``bool``
        unread_mark (optional): ``bool``
        pts (optional): ``int`` ``32-bit``
        draft (optional): :obj:`DraftMessage <pyrogram.raw.base.DraftMessage>`
        folder_id (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["peer", "top_message", "read_inbox_max_id", "read_outbox_max_id", "unread_count",
                            "unread_mentions_count", "notify_settings", "pinned", "unread_mark", "pts", "draft",
                            "folder_id"]

    ID = 0x2c171f72
    QUALNAME = "types.Dialog"

    def __init__(self, *, peer: "raw.base.Peer", top_message: int, read_inbox_max_id: int, read_outbox_max_id: int,
                 unread_count: int, unread_mentions_count: int, notify_settings: "raw.base.PeerNotifySettings",
                 pinned: Union[None, bool] = None, unread_mark: Union[None, bool] = None, pts: Union[None, int] = None,
                 draft: "raw.base.DraftMessage" = None, folder_id: Union[None, int] = None) -> None:
        self.peer = peer  # Peer
        self.top_message = top_message  # int
        self.read_inbox_max_id = read_inbox_max_id  # int
        self.read_outbox_max_id = read_outbox_max_id  # int
        self.unread_count = unread_count  # int
        self.unread_mentions_count = unread_mentions_count  # int
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.pinned = pinned  # flags.2?true
        self.unread_mark = unread_mark  # flags.3?true
        self.pts = pts  # flags.0?int
        self.draft = draft  # flags.1?DraftMessage
        self.folder_id = folder_id  # flags.4?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Dialog":
        flags = Int.read(data)

        pinned = True if flags & (1 << 2) else False
        unread_mark = True if flags & (1 << 3) else False
        peer = TLObject.read(data)

        top_message = Int.read(data)

        read_inbox_max_id = Int.read(data)

        read_outbox_max_id = Int.read(data)

        unread_count = Int.read(data)

        unread_mentions_count = Int.read(data)

        notify_settings = TLObject.read(data)

        pts = Int.read(data) if flags & (1 << 0) else None
        draft = TLObject.read(data) if flags & (1 << 1) else None

        folder_id = Int.read(data) if flags & (1 << 4) else None
        return Dialog(peer=peer, top_message=top_message, read_inbox_max_id=read_inbox_max_id,
                      read_outbox_max_id=read_outbox_max_id, unread_count=unread_count,
                      unread_mentions_count=unread_mentions_count, notify_settings=notify_settings, pinned=pinned,
                      unread_mark=unread_mark, pts=pts, draft=draft, folder_id=folder_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.pinned is not None else 0
        flags |= (1 << 3) if self.unread_mark is not None else 0
        flags |= (1 << 0) if self.pts is not None else 0
        flags |= (1 << 1) if self.draft is not None else 0
        flags |= (1 << 4) if self.folder_id is not None else 0
        data.write(Int(flags))

        data.write(self.peer.write())

        data.write(Int(self.top_message))

        data.write(Int(self.read_inbox_max_id))

        data.write(Int(self.read_outbox_max_id))

        data.write(Int(self.unread_count))

        data.write(Int(self.unread_mentions_count))

        data.write(self.notify_settings.write())

        if self.pts is not None:
            data.write(Int(self.pts))

        if self.draft is not None:
            data.write(self.draft.write())

        if self.folder_id is not None:
            data.write(Int(self.folder_id))

        return data.getvalue()
