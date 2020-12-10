from typing import List

from pyrogram import raw, types

from ..object import Object

import pyrogram


class BotInfo(Object):
    def __init__(
            self,
            client: "pyrogram.Client" = None,
            user_id: int = None,
            description: str = None,
            commands: List["types.BotCommand"] = None,
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
            commands=types.List([types.BotCommand._parse(client, r) for r in bot_info.commands]) or None,
        )
