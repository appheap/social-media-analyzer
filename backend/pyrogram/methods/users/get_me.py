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

from pyrogram import raw
from pyrogram import types
from pyrogram.scaffold import Scaffold


class GetMe(Scaffold):
    async def get_me(self) -> "types.User":
        """Get your own user identity.

        Returns:
            :obj:`~pyrogram.types.User`: Information about the own logged in user/bot.

        Example:
            .. code-block:: python

                me = app.get_me()
                print(me)
        """
        return types.User._parse(
            self,
            (await self.send(
                raw.functions.users.GetFullUser(
                    id=raw.types.InputUserSelf()
                )
            )).user
        )
