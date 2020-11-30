from pyrogram import raw

from ..object import Object


class BotCommand(Object):
    def __init__(
            self,
            *,
            client: "Client" = None,
            command: str = None,
            description: str = None,
    ):
        super().__init__(client)

        self.command = command
        self.description = description

    @staticmethod
    def _parse(client, bot_command: "raw.types.BotCommand"):
        if bot_command is None:
            return None

        return BotCommand(
            client=client,
            command=getattr(bot_command, 'command'),
            description=getattr(bot_command, 'description'),
        )
