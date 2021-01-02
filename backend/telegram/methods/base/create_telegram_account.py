from typing import Optional

from db.scaffold import Scaffold
import pyrogram
from telegram import models as tg_models
from users import models as site_models


class CreateTelegramAccount(Scaffold):

    def create_telegram_account(
            self,
            db_site_user: 'site_models.SiteUser',
            db_user: 'tg_models.User',
            client: pyrogram.Client,
    ) -> Optional['tg_models.TelegramAccount']:
        return self.tg_models.TelegramAccount.accounts.update_or_create_from_raw(
            db_site_user=db_site_user,
            db_user=db_user,
            client=client
        )
