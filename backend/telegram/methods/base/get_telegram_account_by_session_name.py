from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models


class GetTelegramAccountBySessionName(Scaffold):

    def get_telegram_account_by_session_name(
            self,
            session_name: 'str'
    ) -> Optional['tg_models.TelegramAccount']:
        return self.tg_models.TelegramAccount.accounts.get_telegram_account_by_session_name(session_name=session_name)
