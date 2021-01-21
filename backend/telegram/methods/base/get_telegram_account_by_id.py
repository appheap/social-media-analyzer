from db.scaffold import Scaffold
from typing import List, Optional
from telegram import models as tg_models


class GetTelegramAccountById(Scaffold):

    def get_telegram_account_by_id(
            self,
            id: int
    ) -> Optional['tg_models.TelegramAccount']:
        return self.tg_models.TelegramAccount.accounts.get_telegram_account_by_id(
            id=id
        )
