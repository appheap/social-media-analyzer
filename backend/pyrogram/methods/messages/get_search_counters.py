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
from typing import Union, List, Optional

from pyrogram import types
from pyrogram import raw
from pyrogram import utils
from pyrogram.scaffold import Scaffold
from pyrogram.raw.types import (
    InputMessagesFilterPhotos, InputMessagesFilterDocument, InputMessagesFilterUrl,
    InputMessagesFilterRoundVideo, InputMessagesFilterGeo, InputMessagesFilterContacts,
    InputMessagesFilterGif, InputMessagesFilterVoice, InputMessagesFilterMusic, InputMessagesFilterVideo,
)

log = logging.getLogger(__name__)

all_filters = [InputMessagesFilterPhotos(), InputMessagesFilterVideo(),
               InputMessagesFilterDocument(), InputMessagesFilterMusic(),
               InputMessagesFilterUrl(), InputMessagesFilterVoice(),
               InputMessagesFilterRoundVideo(), InputMessagesFilterGif(),
               InputMessagesFilterGeo(), InputMessagesFilterContacts(), ]

filters_dict = {
    'photo': InputMessagesFilterPhotos(),
    'video': InputMessagesFilterVideo(),
    'document': InputMessagesFilterDocument(),
    'music': InputMessagesFilterMusic(),
    'voice': InputMessagesFilterVoice(),
    'url': InputMessagesFilterUrl(),
    'video_note': InputMessagesFilterRoundVideo(),
    'animation': InputMessagesFilterGif(),
    'location': InputMessagesFilterGeo(),
    'contact': InputMessagesFilterContacts(),
}

_filter_names = {'InputMessagesFilterPhotos': 'photo', 'InputMessagesFilterVideo': 'video',
                 'InputMessagesFilterDocument': 'document', 'InputMessagesFilterMusic': 'music',
                 'InputMessagesFilterUrl': 'url', 'InputMessagesFilterVoice': 'voice',
                 'InputMessagesFilterRoundVideo': 'video_note', 'InputMessagesFilterGif': 'animation',
                 'InputMessagesFilterGeo': 'location', 'InputMessagesFilterContacts': 'contact'}


class GetSearchCounters(Scaffold):
    async def get_search_counters(
            self,
            chat_id: Union[int, str],
            filters: List["str"] = None
    ) -> Optional[List["types.SearchCounter"]]:
        """Indicates how many results would be found by a ``messages.search`` call with the same parameters

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            filters (List of ``str``):
                Provided message filter

        Returns:
            ``int``: On success, the search counter dict is returned.

        Example:
            .. code-block:: python

                app.get_search_counter("pyrogramchat")
        """

        if filters:
            raw_filters = []
            for _filter in filters:
                if _filter not in filters_dict:
                    raise ValueError(f"`{_filter}` is not a valid filter name")
                raw_filters.append(filters_dict.get(_filter))
        else:
            raw_filters = all_filters

        r = await self.send(
            raw.functions.messages.GetSearchCounters(
                peer=await self.resolve_peer(chat_id),
                filters=raw_filters
            )
        )

        if not r:
            return None

        return utils.parse_search_counters(r)
