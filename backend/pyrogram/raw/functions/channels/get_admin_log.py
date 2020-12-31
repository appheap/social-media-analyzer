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


class GetAdminLog(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``122``
        - ID: ``0x33ddf480``

    Parameters:
        channel: :obj:`InputChannel <pyrogram.raw.base.InputChannel>`
        q: ``str``
        max_id: ``int`` ``64-bit``
        min_id: ``int`` ``64-bit``
        limit: ``int`` ``32-bit``
        events_filter (optional): :obj:`ChannelAdminLogEventsFilter <pyrogram.raw.base.ChannelAdminLogEventsFilter>`
        admins (optional): List of :obj:`InputUser <pyrogram.raw.base.InputUser>`

    Returns:
        :obj:`channels.AdminLogResults <pyrogram.raw.base.channels.AdminLogResults>`
    """

    __slots__: List[str] = ["channel", "q", "max_id", "min_id", "limit", "events_filter", "admins"]

    ID = 0x33ddf480
    QUALNAME = "functions.channels.GetAdminLog"

    def __init__(self, *, channel: "raw.base.InputChannel", q: str, max_id: int, min_id: int, limit: int,
                 events_filter: "raw.base.ChannelAdminLogEventsFilter" = None,
                 admins: Union[None, List["raw.base.InputUser"]] = None) -> None:
        self.channel = channel  # InputChannel
        self.q = q  # string
        self.max_id = max_id  # long
        self.min_id = min_id  # long
        self.limit = limit  # int
        self.events_filter = events_filter  # flags.0?ChannelAdminLogEventsFilter
        self.admins = admins  # flags.1?Vector<InputUser>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetAdminLog":
        flags = Int.read(data)

        channel = TLObject.read(data)

        q = String.read(data)

        events_filter = TLObject.read(data) if flags & (1 << 0) else None

        admins = TLObject.read(data) if flags & (1 << 1) else []

        max_id = Long.read(data)

        min_id = Long.read(data)

        limit = Int.read(data)

        return GetAdminLog(channel=channel, q=q, max_id=max_id, min_id=min_id, limit=limit, events_filter=events_filter,
                           admins=admins)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.events_filter is not None else 0
        flags |= (1 << 1) if self.admins is not None else 0
        data.write(Int(flags))

        data.write(self.channel.write())

        data.write(String(self.q))

        if self.events_filter is not None:
            data.write(self.events_filter.write())

        if self.admins is not None:
            data.write(Vector(self.admins))

        data.write(Long(self.max_id))

        data.write(Long(self.min_id))

        data.write(Int(self.limit))

        return data.getvalue()
