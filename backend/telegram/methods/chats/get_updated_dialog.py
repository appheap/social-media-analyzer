from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models
from pyrogram import types


class GetUpdatedDialog(Scaffold):

    def get_updated_dialog(
            self,
            *,
            raw_chat: "types.Chat",
            db_account: "tg_models.TelegramAccount",
            is_member: bool,
            left_date_ts: int = None,
            update_chat: bool = True,
    ) -> Optional["tg_models.Dialog"]:
        if raw_chat is None:
            return None

        def get_updated_chat():
            return self.get_updated_chat(
                raw_chat=raw_chat,
                db_telegram_account=db_account,
            )

        if update_chat:
            db_chat = get_updated_chat()
        else:
            db_chat = self.get_chat_by_id(chat_id=raw_chat.id)
            if db_chat is None:
                db_chat = get_updated_chat()

        return self.tg_models.Dialog.objects.update_or_create_dialog(
            db_chat=db_chat,
            db_account=db_account,
            is_member=is_member,
            left_date_ts=left_date_ts,
        )
