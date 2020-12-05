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
from typing import Union, Iterable, List

from pyrogram import raw
from pyrogram import types
from pyrogram import utils
from pyrogram.scaffold import Scaffold

log = logging.getLogger(__name__)


class GetStickerSet(Scaffold):
    async def get_stickerset(
            self,
            input_stickerset: raw.base.InputStickerSet,

    ) -> "types.StickerSet":
        """Get info about a stickerset

        Parameters:
            input_stickerset (``bool``, *optional*):
                stickerset

        Returns:
            :obj:`~pyrogram.types.StickerSet`:

        Raises:
            ValueError: In case of invalid arguments.
        """
        if input_stickerset is None:
            raise ValueError('input_stickerset cannot be empty')

        r = await self.send(
            raw.functions.messages.GetStickerSet(
                stickerset=input_stickerset,
            )
        )
        if isinstance(r, raw.base.messages.StickerSet):
            return types.StickerSet._parse(self, r.set)
        else:
            return None
