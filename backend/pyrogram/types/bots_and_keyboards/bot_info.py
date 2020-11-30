from typing import List

from pyrogram import raw, types as tg_types
from pyrogram import types

from ..object import Object

import telegram.client as tg


class BotInfo(Object):
    def __init__(
            self,
            client: "tg.Client" = None,
            user_id: int = None,
            description: str = None,
            commands: List["tg_types.BotCommand"] = None,
    ):
        super().__init__(client)

        self.user_id = user_id
        self.description = description
        self.commands = commands

    @staticmethod
    def _parse(client, bot_info: "raw.types.BotInfo"):
        if bot_info is None:
            return None

        return BotInfo(
            client=client,
            user_id=getattr(bot_info, 'user_id'),
            description=getattr(bot_info, 'description'),
            commands=types.List([tg_types.BotCommand._parse(client, r) for r in bot_info.commands]) or None,
        )
