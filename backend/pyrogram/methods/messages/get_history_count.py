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

import logging
from typing import Union

from pyrogram import raw
from pyrogram.scaffold import Scaffold

log = logging.getLogger(__name__)


class GetHistoryCount(Scaffold):
    async def get_history_count(
            self,
            chat_id: Union[int, str]
    ) -> int:
        """Get the total count of messages in a chat.

        .. note::

            Due to Telegram latest internal changes, the server can't reliably find anymore the total count of messages
            a **private** or a **basic group** chat has with a single method call. To overcome this limitation, Pyrogram
            has to iterate over all the messages. Channels and supergroups are not affected by this limitation.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            ``int``: On success, the chat history count is returned.

        Example:
            .. code-block:: python

                app.get_history_count("pyrogramchat")
        """

        r = await self.send(
            raw.functions.messages.GetHistory(
                peer=await self.resolve_peer(chat_id),
                offset_id=0,
                offset_date=0,
                add_offset=0,
                limit=1,
                max_id=0,
                min_id=0,
                hash=0
            )
        )

        if isinstance(r, raw.types.messages.Messages):
            return len(r.messages)
        else:
            return r.count
