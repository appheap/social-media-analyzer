from typing import List, Generator

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models


class GetUpdatedMessageViews(Scaffold):
    def get_updated_message_views(
            self,
            *,
            raw_messages: List['types.Message'],
            db_chat: "tg_models.Chat",
            logger_account: "tg_models.TelegramAccount",
            date_ts: int,

            create_recent_repliers: bool = True,
    ) -> Generator['tg_models.MessageView', None, None]:
        if raw_messages is None or db_chat is None or logger_account is None or date_ts is None:
            return

        for raw_message in raw_messages:
            db_message = self.get_message_from_raw(
                chat_id=db_chat.chat_id,
                raw_message=raw_message,
            )
            if db_message is None:
                db_message = self.get_updated_message(
                    db_chat=db_chat,
                    raw_message=raw_message,
                    logger_account=logger_account
                )
                if not db_message:
                    continue

                db_message_view = self.get_updated_message_view(
                    raw_message_view=raw_message.views,
                    db_chat=db_chat,
                    db_message=db_message,
                    logger_account=logger_account,
                    date_ts=date_ts,
                    create_recent_repliers=create_recent_repliers,
                )
                if db_message_view:
                    yield db_message_view
