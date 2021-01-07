from typing import Optional
from telegram import models as tg_models

from db.scaffold import Scaffold


class GetUpdatedChatMemberCount(Scaffold):

    def get_updated_chat_member_count(
            self,
            *,
            db_chat: 'tg_models.Chat',
            count: int,
            date_ts: int,
            logger_account: 'tg_models.TelegramAccount'
    ) -> Optional['tg_models.ChatMemberCount']:
        if db_chat is None or count is None or date_ts is None or logger_account is None:
            return None

        return self.tg_models.ChatMemberCount.objects.update_or_create_from_raw(
            db_chat=db_chat,
            count=count,
            date_ts=date_ts,
            logger_account=logger_account,
        )
