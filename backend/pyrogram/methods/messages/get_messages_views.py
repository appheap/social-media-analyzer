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
from typing import Union, Iterable, List

from pyrogram import raw
from pyrogram import types
from pyrogram import utils
from pyrogram.scaffold import Scaffold

log = logging.getLogger(__name__)


class GetMessagesViews(Scaffold):
    async def get_messages_views(
            self,
            chat_id: Union[int, str],
            message_ids: Union[int, Iterable[int]] = None,
            increment: bool = True,
    ) -> Union["types.MessageViews", List["types.MessageViews"]]:
        """Get one or more messages views from a chat by using message identifiers.

        You can retrieve up to 100 message views at once.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_ids (``iterable``, *optional*):
                Pass a single message identifier or a list of message ids (as integers) to get the message views of the
                messages. Iterators and Generators are also accepted.

            increment (``bool``, *optional*):
                Whether to mark the message as viewed and increment the view counter

        Returns:
            :obj:`~pyrogram.types.MessageViews` | List of :obj:`~pyrogram.types.MessageViews`: In case *message_ids* was an
            integer, the single requested message is returned, otherwise, in case *message_ids* was an iterable, the
            returned value will be a list of message views, even if such iterable contained just a single element.

        Example:
            .. code-block:: python

                # Get one message views
                app.get_messages_views("pyrogramchat", 51110)

                # Get more than one message views (list of message views)
                app.get_messages_views("pyrogramchat", [44625, 51110])


        Raises:
            ValueError: In case of invalid arguments.
        """
        ids = message_ids

        if ids is None:
            raise ValueError("No argument supplied. pass message_ids")

        peer = await self.resolve_peer(chat_id)

        is_iterable = not isinstance(ids, int)
        ids = list(ids) if is_iterable else [ids]

        rpc = raw.functions.messages.GetMessagesViews(peer=peer, id=ids, increment=increment)

        r = await self.send(rpc, sleep_threshold=-1)

        message_views = await utils.parse_message_views(self, r, ids)

        if len(message_views) == 1:
            return message_views[0]
        else:
            return message_views
