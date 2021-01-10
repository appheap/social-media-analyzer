from typing import Optional

from db.scaffold import Scaffold
import pyrogram
from pyrogram import types
from telegram import models as tg_models
from users import models as site_models


class GetUpdatedTelegramAccount(Scaffold):

    def get_updated_telegram_account(
            self,
            db_site_user: 'site_models.SiteUser',
            raw_user: 'types.User',
            client: 'pyrogram.Client',
    ) -> Optional['tg_models.TelegramAccount']:
        if db_site_user is None or raw_user is None or client is None:
            return None

        db_user = self.get_updated_user(
            raw_user=raw_user
        )

        return self.tg_models.TelegramAccount.accounts.update_or_create_from_raw(
            db_site_user=db_site_user,
            db_user=db_user,
            client=client
        )
