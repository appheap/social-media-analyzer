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


class ChannelAdminLogEventsFilter(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChannelAdminLogEventsFilter`.

    Details:
        - Layer: ``122``
        - ID: ``0xea107ae4``

    Parameters:
        join (optional): ``bool``
        leave (optional): ``bool``
        invite (optional): ``bool``
        ban (optional): ``bool``
        unban (optional): ``bool``
        kick (optional): ``bool``
        unkick (optional): ``bool``
        promote (optional): ``bool``
        demote (optional): ``bool``
        info (optional): ``bool``
        settings (optional): ``bool``
        pinned (optional): ``bool``
        edit (optional): ``bool``
        delete (optional): ``bool``
        group_call (optional): ``bool``
    """

    __slots__: List[str] = ["join", "leave", "invite", "ban", "unban", "kick", "unkick", "promote", "demote", "info",
                            "settings", "pinned", "edit", "delete", "group_call"]

    ID = 0xea107ae4
    QUALNAME = "types.ChannelAdminLogEventsFilter"

    def __init__(self, *, join: Union[None, bool] = None, leave: Union[None, bool] = None,
                 invite: Union[None, bool] = None, ban: Union[None, bool] = None, unban: Union[None, bool] = None,
                 kick: Union[None, bool] = None, unkick: Union[None, bool] = None, promote: Union[None, bool] = None,
                 demote: Union[None, bool] = None, info: Union[None, bool] = None, settings: Union[None, bool] = None,
                 pinned: Union[None, bool] = None, edit: Union[None, bool] = None, delete: Union[None, bool] = None,
                 group_call: Union[None, bool] = None) -> None:
        self.join = join  # flags.0?true
        self.leave = leave  # flags.1?true
        self.invite = invite  # flags.2?true
        self.ban = ban  # flags.3?true
        self.unban = unban  # flags.4?true
        self.kick = kick  # flags.5?true
        self.unkick = unkick  # flags.6?true
        self.promote = promote  # flags.7?true
        self.demote = demote  # flags.8?true
        self.info = info  # flags.9?true
        self.settings = settings  # flags.10?true
        self.pinned = pinned  # flags.11?true
        self.edit = edit  # flags.12?true
        self.delete = delete  # flags.13?true
        self.group_call = group_call  # flags.14?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChannelAdminLogEventsFilter":
        flags = Int.read(data)

        join = True if flags & (1 << 0) else False
        leave = True if flags & (1 << 1) else False
        invite = True if flags & (1 << 2) else False
        ban = True if flags & (1 << 3) else False
        unban = True if flags & (1 << 4) else False
        kick = True if flags & (1 << 5) else False
        unkick = True if flags & (1 << 6) else False
        promote = True if flags & (1 << 7) else False
        demote = True if flags & (1 << 8) else False
        info = True if flags & (1 << 9) else False
        settings = True if flags & (1 << 10) else False
        pinned = True if flags & (1 << 11) else False
        edit = True if flags & (1 << 12) else False
        delete = True if flags & (1 << 13) else False
        group_call = True if flags & (1 << 14) else False
        return ChannelAdminLogEventsFilter(join=join, leave=leave, invite=invite, ban=ban, unban=unban, kick=kick,
                                           unkick=unkick, promote=promote, demote=demote, info=info, settings=settings,
                                           pinned=pinned, edit=edit, delete=delete, group_call=group_call)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.join else 0
        flags |= (1 << 1) if self.leave else 0
        flags |= (1 << 2) if self.invite else 0
        flags |= (1 << 3) if self.ban else 0
        flags |= (1 << 4) if self.unban else 0
        flags |= (1 << 5) if self.kick else 0
        flags |= (1 << 6) if self.unkick else 0
        flags |= (1 << 7) if self.promote else 0
        flags |= (1 << 8) if self.demote else 0
        flags |= (1 << 9) if self.info else 0
        flags |= (1 << 10) if self.settings else 0
        flags |= (1 << 11) if self.pinned else 0
        flags |= (1 << 12) if self.edit else 0
        flags |= (1 << 13) if self.delete else 0
        flags |= (1 << 14) if self.group_call else 0
        data.write(Int(flags))

        return data.getvalue()
