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


class DialogFilter(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.DialogFilter`.

    Details:
        - Layer: ``122``
        - ID: ``0x7438f7e8``

    Parameters:
        id: ``int`` ``32-bit``
        title: ``str``
        pinned_peers: List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        include_peers: List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        exclude_peers: List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        contacts (optional): ``bool``
        non_contacts (optional): ``bool``
        groups (optional): ``bool``
        broadcasts (optional): ``bool``
        bots (optional): ``bool``
        exclude_muted (optional): ``bool``
        exclude_read (optional): ``bool``
        exclude_archived (optional): ``bool``
        emoticon (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetDialogFilters <pyrogram.raw.functions.messages.GetDialogFilters>`
    """

    __slots__: List[str] = ["id", "title", "pinned_peers", "include_peers", "exclude_peers", "contacts", "non_contacts",
                            "groups", "broadcasts", "bots", "exclude_muted", "exclude_read", "exclude_archived",
                            "emoticon"]

    ID = 0x7438f7e8
    QUALNAME = "types.DialogFilter"

    def __init__(self, *, id: int, title: str, pinned_peers: List["raw.base.InputPeer"],
                 include_peers: List["raw.base.InputPeer"], exclude_peers: List["raw.base.InputPeer"],
                 contacts: Union[None, bool] = None, non_contacts: Union[None, bool] = None,
                 groups: Union[None, bool] = None, broadcasts: Union[None, bool] = None, bots: Union[None, bool] = None,
                 exclude_muted: Union[None, bool] = None, exclude_read: Union[None, bool] = None,
                 exclude_archived: Union[None, bool] = None, emoticon: Union[None, str] = None) -> None:
        self.id = id  # int
        self.title = title  # string
        self.pinned_peers = pinned_peers  # Vector<InputPeer>
        self.include_peers = include_peers  # Vector<InputPeer>
        self.exclude_peers = exclude_peers  # Vector<InputPeer>
        self.contacts = contacts  # flags.0?true
        self.non_contacts = non_contacts  # flags.1?true
        self.groups = groups  # flags.2?true
        self.broadcasts = broadcasts  # flags.3?true
        self.bots = bots  # flags.4?true
        self.exclude_muted = exclude_muted  # flags.11?true
        self.exclude_read = exclude_read  # flags.12?true
        self.exclude_archived = exclude_archived  # flags.13?true
        self.emoticon = emoticon  # flags.25?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "DialogFilter":
        flags = Int.read(data)

        contacts = True if flags & (1 << 0) else False
        non_contacts = True if flags & (1 << 1) else False
        groups = True if flags & (1 << 2) else False
        broadcasts = True if flags & (1 << 3) else False
        bots = True if flags & (1 << 4) else False
        exclude_muted = True if flags & (1 << 11) else False
        exclude_read = True if flags & (1 << 12) else False
        exclude_archived = True if flags & (1 << 13) else False
        id = Int.read(data)

        title = String.read(data)

        emoticon = String.read(data) if flags & (1 << 25) else None
        pinned_peers = TLObject.read(data)

        include_peers = TLObject.read(data)

        exclude_peers = TLObject.read(data)

        return DialogFilter(id=id, title=title, pinned_peers=pinned_peers, include_peers=include_peers,
                            exclude_peers=exclude_peers, contacts=contacts, non_contacts=non_contacts, groups=groups,
                            broadcasts=broadcasts, bots=bots, exclude_muted=exclude_muted, exclude_read=exclude_read,
                            exclude_archived=exclude_archived, emoticon=emoticon)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.contacts else 0
        flags |= (1 << 1) if self.non_contacts else 0
        flags |= (1 << 2) if self.groups else 0
        flags |= (1 << 3) if self.broadcasts else 0
        flags |= (1 << 4) if self.bots else 0
        flags |= (1 << 11) if self.exclude_muted else 0
        flags |= (1 << 12) if self.exclude_read else 0
        flags |= (1 << 13) if self.exclude_archived else 0
        flags |= (1 << 25) if self.emoticon is not None else 0
        data.write(Int(flags))

        data.write(Int(self.id))

        data.write(String(self.title))

        if self.emoticon is not None:
            data.write(String(self.emoticon))

        data.write(Vector(self.pinned_peers))

        data.write(Vector(self.include_peers))

        data.write(Vector(self.exclude_peers))

        return data.getvalue()
