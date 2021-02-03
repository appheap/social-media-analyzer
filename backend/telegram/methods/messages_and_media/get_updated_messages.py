from typing import Optional, List, Generator

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models


class GetUpdatedMessages(Scaffold):

    def get_updated_messages(
            self,
            *,
            db_chat: 'tg_models.Chat',
            raw_messages: List['types.Message'],
            logger_account: "tg_models.TelegramAccount",

            create_entities: bool = True,
    ) -> Generator['tg_models.Message', None, None]:
        if db_chat is None or raw_messages is None or logger_account is None:
            return None

        for raw_message in raw_messages:
            yield self.get_updated_message(
                db_chat=db_chat,
                raw_message=raw_message,
                logger_account=logger_account,
                create_entities=create_entities
            )
