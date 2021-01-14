from db.scaffold import Scaffold
from pyrogram import types
from typing import List, Optional
from telegram import models as tg_models


class GetUpdatedDialogs(Scaffold):

    def get_updated_dialogs(
            self,
            *,
            raw_dialogs: List['types.Dialog'],
            db_telegram_account: 'tg_models.TelegramAccount',
            update_chat: bool = True,
    ) -> Optional[List['tg_models.Dialog']]:
        if raw_dialogs is None or not len(raw_dialogs) or db_telegram_account is None:
            return None

        db_dialogs = []

        for raw_dialog in raw_dialogs:
            db_dialog = self.get_updated_dialog(
                raw_chat=raw_dialog.chat,
                db_account=db_telegram_account,
                is_member=True,
                update_chat=update_chat,
            )
            if db_dialog:
                db_dialogs.append(db_dialog)

        return db_dialogs
