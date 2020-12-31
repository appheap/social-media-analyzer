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


class MegagroupStats(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.stats.MegagroupStats`.

    Details:
        - Layer: ``122``
        - ID: ``0xef7ff916``

    Parameters:
        period: :obj:`StatsDateRangeDays <pyrogram.raw.base.StatsDateRangeDays>`
        members: :obj:`StatsAbsValueAndPrev <pyrogram.raw.base.StatsAbsValueAndPrev>`
        messages: :obj:`StatsAbsValueAndPrev <pyrogram.raw.base.StatsAbsValueAndPrev>`
        viewers: :obj:`StatsAbsValueAndPrev <pyrogram.raw.base.StatsAbsValueAndPrev>`
        posters: :obj:`StatsAbsValueAndPrev <pyrogram.raw.base.StatsAbsValueAndPrev>`
        growth_graph: :obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`
        members_graph: :obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`
        new_members_by_source_graph: :obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`
        languages_graph: :obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`
        messages_graph: :obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`
        actions_graph: :obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`
        top_hours_graph: :obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`
        weekdays_graph: :obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`
        top_posters: List of :obj:`StatsGroupTopPoster <pyrogram.raw.base.StatsGroupTopPoster>`
        top_admins: List of :obj:`StatsGroupTopAdmin <pyrogram.raw.base.StatsGroupTopAdmin>`
        top_inviters: List of :obj:`StatsGroupTopInviter <pyrogram.raw.base.StatsGroupTopInviter>`
        users: List of :obj:`User <pyrogram.raw.base.User>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`stats.GetMegagroupStats <pyrogram.raw.functions.stats.GetMegagroupStats>`
    """

    __slots__: List[str] = ["period", "members", "messages", "viewers", "posters", "growth_graph", "members_graph",
                            "new_members_by_source_graph", "languages_graph", "messages_graph", "actions_graph",
                            "top_hours_graph", "weekdays_graph", "top_posters", "top_admins", "top_inviters", "users"]

    ID = 0xef7ff916
    QUALNAME = "types.stats.MegagroupStats"

    def __init__(self, *, period: "raw.base.StatsDateRangeDays", members: "raw.base.StatsAbsValueAndPrev",
                 messages: "raw.base.StatsAbsValueAndPrev", viewers: "raw.base.StatsAbsValueAndPrev",
                 posters: "raw.base.StatsAbsValueAndPrev", growth_graph: "raw.base.StatsGraph",
                 members_graph: "raw.base.StatsGraph", new_members_by_source_graph: "raw.base.StatsGraph",
                 languages_graph: "raw.base.StatsGraph", messages_graph: "raw.base.StatsGraph",
                 actions_graph: "raw.base.StatsGraph", top_hours_graph: "raw.base.StatsGraph",
                 weekdays_graph: "raw.base.StatsGraph", top_posters: List["raw.base.StatsGroupTopPoster"],
                 top_admins: List["raw.base.StatsGroupTopAdmin"], top_inviters: List["raw.base.StatsGroupTopInviter"],
                 users: List["raw.base.User"]) -> None:
        self.period = period  # StatsDateRangeDays
        self.members = members  # StatsAbsValueAndPrev
        self.messages = messages  # StatsAbsValueAndPrev
        self.viewers = viewers  # StatsAbsValueAndPrev
        self.posters = posters  # StatsAbsValueAndPrev
        self.growth_graph = growth_graph  # StatsGraph
        self.members_graph = members_graph  # StatsGraph
        self.new_members_by_source_graph = new_members_by_source_graph  # StatsGraph
        self.languages_graph = languages_graph  # StatsGraph
        self.messages_graph = messages_graph  # StatsGraph
        self.actions_graph = actions_graph  # StatsGraph
        self.top_hours_graph = top_hours_graph  # StatsGraph
        self.weekdays_graph = weekdays_graph  # StatsGraph
        self.top_posters = top_posters  # Vector<StatsGroupTopPoster>
        self.top_admins = top_admins  # Vector<StatsGroupTopAdmin>
        self.top_inviters = top_inviters  # Vector<StatsGroupTopInviter>
        self.users = users  # Vector<User>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MegagroupStats":
        # No flags

        period = TLObject.read(data)

        members = TLObject.read(data)

        messages = TLObject.read(data)

        viewers = TLObject.read(data)

        posters = TLObject.read(data)

        growth_graph = TLObject.read(data)

        members_graph = TLObject.read(data)

        new_members_by_source_graph = TLObject.read(data)

        languages_graph = TLObject.read(data)

        messages_graph = TLObject.read(data)

        actions_graph = TLObject.read(data)

        top_hours_graph = TLObject.read(data)

        weekdays_graph = TLObject.read(data)

        top_posters = TLObject.read(data)

        top_admins = TLObject.read(data)

        top_inviters = TLObject.read(data)

        users = TLObject.read(data)

        return MegagroupStats(period=period, members=members, messages=messages, viewers=viewers, posters=posters,
                              growth_graph=growth_graph, members_graph=members_graph,
                              new_members_by_source_graph=new_members_by_source_graph, languages_graph=languages_graph,
                              messages_graph=messages_graph, actions_graph=actions_graph,
                              top_hours_graph=top_hours_graph, weekdays_graph=weekdays_graph, top_posters=top_posters,
                              top_admins=top_admins, top_inviters=top_inviters, users=users)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.period.write())

        data.write(self.members.write())

        data.write(self.messages.write())

        data.write(self.viewers.write())

        data.write(self.posters.write())

        data.write(self.growth_graph.write())

        data.write(self.members_graph.write())

        data.write(self.new_members_by_source_graph.write())

        data.write(self.languages_graph.write())

        data.write(self.messages_graph.write())

        data.write(self.actions_graph.write())

        data.write(self.top_hours_graph.write())

        data.write(self.weekdays_graph.write())

        data.write(Vector(self.top_posters))

        data.write(Vector(self.top_admins))

        data.write(Vector(self.top_inviters))

        data.write(Vector(self.users))

        return data.getvalue()
