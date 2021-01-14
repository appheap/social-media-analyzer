from db.scaffold import Scaffold
from typing import List, Optional
from telegram import models as tg_models


class GetTelegramAccountsBySessionNames(Scaffold):

    def get_telegram_accounts_by_session_names(
            self,
            *,
            db_chat: 'tg_models.Chat',
            session_names: List['str'],
            with_admin_permissions: bool = False,
    ) -> Optional[List['tg_models.TelegramAccount']]:
        return self.tg_models.AdminShip.objects.get_telegram_accounts_by_account_session_names(
            db_chat=db_chat,
            session_names=session_names,
            with_admin_permissions=with_admin_permissions
        )
