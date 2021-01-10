from db.scaffold import Scaffold
from typing import List, Optional
from telegram import models as tg_models


class GetTelegramAccountsByIds(Scaffold):

    def get_telegram_accounts_by_ids(
            self,
            ids: List['int']
    ) -> Optional[List['tg_models.TelegramAccount']]:
        return self.tg_models.TelegramAccount.accounts.get_telegram_accounts_by_ids(
            ids=ids
        )
