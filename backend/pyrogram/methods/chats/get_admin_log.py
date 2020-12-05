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

import logging
from typing import List, Union

from pyrogram import raw
from pyrogram import types
from pyrogram import utils
from pyrogram.scaffold import Scaffold

log = logging.getLogger(__name__)


class Filters:
    JOIN = "join"
    LEAVE = "leave"
    INVITE = "invite"
    BAN = "ban"
    UNBAN = "unban"
    KICK = "kick"
    UNKICK = "unkick"
    PROMOTE = "promote"
    DEMOTE = "demote"
    INFO = "info"
    SETTINGS = "settings"
    PINNED = "pinned"
    EDIT = "edit"
    DELETE = "delete"


All_Filters = [
    Filters.JOIN,
    Filters.LEAVE,
    Filters.INVITE,
    Filters.BAN,
    Filters.UNBAN,
    Filters.KICK,
    Filters.UNKICK,
    Filters.PROMOTE,
    Filters.DEMOTE,
    Filters.INFO,
    Filters.SETTINGS,
    Filters.PINNED,
    Filters.EDIT,
    Filters.DELETE,
]


class GetAdminLog(Scaffold):
    async def get_admin_log(
            self,
            chat_id: Union[str, int] = None,
            query: str = "",
            filters: "" = None,
            admins: "" = None,
            max_id: int = 0,
            min_id: int = 0,
            limit: int = 0,

    ) -> List["types.ChannelAdminLogEvent"]:
        """Get a chat's admin log events.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            query (``str``, *optional*):
                Search query, can be empty

            filters (List of ``str``, *optional*):
                Event filter, can be empty

            admins (``int``, *optional*):
                Only show events from these admins, can be empty

            max_id (``int``, *optional*):
                Maximum ID of message to return, can be empty

            min_id (``int``, *optional*):
                Minimum ID of message to return , can be empty

            limit (``int``, *optional*):
                Limits the number of admin log events to be retrieved.
                Defaults to 0.


        Returns:
            List of :obj:`~pyrogram.types.ChannelAdminLogEvent`: On success, a list of admin log events is returned.

        Example:
            .. code-block:: python

                # Get All admin log events of a chat
                app.get_admin_logs('pyrogram')

        """

        peer = await self.resolve_peer(chat_id)

        if filters:
            if not isinstance(filters, list):
                raise ValueError('filters type must be a list')
            for _filter in filters:
                if _filter not in All_Filters:
                    raise ValueError('wrong filter value used')

            raw_filters = raw.types.ChannelAdminLogEventsFilter(
                join=True if 'join' in filters else None,
                leave=True if 'leave' in filters else None,
                invite=True if 'invite' in filters else None,
                ban=True if 'ban' in filters else None,
                unban=True if 'unban' in filters else None,
                kick=True if 'unban' in filters else None,
                unkick=True if 'unkick' in filters else None,
                promote=True if 'promote' in filters else None,
                demote=True if 'demote' in filters else None,
                info=True if 'info' in filters else None,
                settings=True if 'settings' in filters else None,
                pinned=True if 'pinned' in filters else None,
                edit=True if 'edit' in filters else None,
                delete=True if 'delete' in filters else None,
            )
        else:
            raw_filters = None

        r = await self.send(
            raw.functions.channels.GetAdminLog(
                channel=peer,
                q=query,
                max_id=max_id,
                min_id=min_id,
                limit=limit,
                events_filter=raw_filters,
                admins=admins,
            )
        )

        return await utils.parse_admin_log_events(self, r)
