from typing import Optional

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models


class GetUpdatedAdminShip(Scaffold):
    def get_updated_adminship(
            self,
            *,
            db_account: 'tg_models.TelegramAccount',
            db_chat: 'tg_models.Chat',

            raw_chat: types.Chat,
    ) -> Optional['tg_models.AdminShip']:
        if db_account is None or db_chat is None or raw_chat is None:
            return None

        return self.tg_models.AdminShip.objects.update_or_create_from_raw(
            db_account=db_account,
            db_chat=db_chat,
            raw_chat=raw_chat,
        )
