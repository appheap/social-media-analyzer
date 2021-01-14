from django.db import transaction

from db.scaffold import Scaffold
from telegram import models as tg_models


class CreateAdminBasedChatAnalyzers(Scaffold):
    def create_admin_based_chat_analyzers(
            self,
            db_chat: 'tg_models.Chat',
            db_telegram_channel: 'tg_models.TelegramChannel',
            enabled: bool = False,
    ):
        if db_chat is None or db_telegram_channel is None:
            return

        with transaction.atomic():
            with transaction.atomic():
                db_chat.update_or_create_admin_log_analyzer(
                    model=db_chat,
                    field_name='admin_log_analyzer',
                    chat_id=db_chat.chat_id,
                    enabled=enabled,
                )

                db_chat.update_or_create_chat_members_analyzer(
                    model=db_chat,
                    field_name='members_analyzer',
                    chat_id=db_chat.chat_id,
                    enabled=enabled,
                )
