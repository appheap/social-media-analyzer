from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models


class UpdateMessageAndView(Scaffold):

    def update_message_and_view(
            self,
            *,
            db_chat: 'tg_models.Chat',
            raw_message: types.Message,
            logger_account: "tg_models.TelegramAccount",
            now: int,
    ) -> None:
        if db_chat is None or raw_message is None or logger_account is None or now is None:
            return None

        db_message = self.get_updated_message(
            db_chat=db_chat,
            raw_message=raw_message,
            logger_account=logger_account,
        )

        if raw_message.views and db_message:
            self.get_updated_message_view(
                raw_message_view=raw_message.views,
                db_chat=db_chat,
                db_message=db_message,
                logger_account=logger_account,
                date_ts=now,
            )
