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

from typing import Union

from pyrogram import raw
from pyrogram import types
from pyrogram.errors import UserNotParticipant
from pyrogram.scaffold import Scaffold


class GetChatMember(Scaffold):
    async def get_chat_member(
            self,
            chat_id: Union[int, str],
            user_id: Union[int, str]
    ) -> "types.ChatParticipant":
        """Get information about one member of a chat.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            user_id (``int`` | ``str``)::
                Unique identifier (int) or username (str) of the target user.
                For you yourself you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            :obj:`~pyrogram.types.ChatMember`: On success, a chat member is returned.

        Example:
            .. code-block:: python

                dan = app.get_chat_member("pyrogramchat", "haskell")
                print(dan)
        """
        chat = await self.resolve_peer(chat_id)
        user = await self.resolve_peer(user_id)

        if isinstance(chat, raw.types.InputPeerChat):
            r = await self.send(
                raw.functions.messages.GetFullChat(
                    chat_id=chat.chat_id
                )
            )

            members = getattr(r.full_chat.participants, "participants", [])
            users = {i.id: i for i in r.users}

            for member in members:
<<<<<<< HEAD
                member = types.ChatParticipant._parse(self, member, users)
=======
                member = types.ChatMember._parse(self, member, users)
>>>>>>> + Update telegram models

                if isinstance(user, raw.types.InputPeerSelf):
                    if member.user.is_self:
                        return member
                else:
                    if member.user.id == user.user_id:
                        return member
            else:
                raise UserNotParticipant
        elif isinstance(chat, raw.types.InputPeerChannel):
            r = await self.send(
                raw.functions.channels.GetParticipant(
                    channel=chat,
                    user_id=user
                )
            )

            users = {i.id: i for i in r.users}

<<<<<<< HEAD
            return types.ChatParticipant._parse(self, r.participant, users)
=======
            return types.ChatMember._parse(self, r.participant, users)
>>>>>>> + Update telegram models
        else:
            raise ValueError(f'The chat_id "{chat_id}" belongs to a user')
