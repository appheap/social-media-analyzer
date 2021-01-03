from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models


class GetUpdatedDialog(Scaffold):

    def get_updated_dialog(
            self,
            *,
            db_chat: "tg_models.Chat",
            db_account: "tg_models.TelegramAccount",
            is_member: bool,
            left_date_ts: int = None
    ) -> Optional["tg_models.Dialog"]:
        return self.tg_models.Dialog.objects.update_or_create_dialog(
            db_chat=db_chat,
            db_account=db_account,
            is_member=is_member,
            left_date_ts=left_date_ts,
        )
