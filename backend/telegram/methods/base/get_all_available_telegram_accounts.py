from db.scaffold import Scaffold
from typing import List, Optional
from telegram import models as tg_models


class GetAllAvailableTelegramAccounts(Scaffold):

    def get_all_available_telegram_accounts(
            self,
    ) -> Optional[List['tg_models.TelegramAccount']]:
        return self.tg_models.TelegramAccount.objects.all()
