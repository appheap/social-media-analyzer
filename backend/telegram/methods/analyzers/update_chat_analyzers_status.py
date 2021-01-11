from django.db import transaction

from db.scaffold import Scaffold
from telegram import models as tg_models


class UpdateChatAnalyzersStatus(Scaffold):

    def update_chat_analyzers_status(
            self,
            *,
            db_telegram_channel: 'tg_models.TelegramChannel',
            enabled: bool = False,
            only_admin_based_analyzers: bool = False,
    ):
        db_chat = db_telegram_channel.chat

        with transaction.atomic():
            db_chat.update_or_create_admin_log_analyzer(
                model=db_chat,
                field_name='admin_log_analyzer',
                db_telegram_channel=db_telegram_channel,
                chat_id=db_chat.chat_id,
                enabled=enabled,
                create=False,
            )

            db_chat.update_or_create_chat_members_analyzer(
                model=db_chat,
                field_name='members_analyzer',
                db_telegram_channel=db_telegram_channel,
                chat_id=db_chat.chat_id,
                enabled=enabled,
                create=False,
            )

            if not only_admin_based_analyzers:
                db_chat.update_or_create_chat_member_count_analyzer(
                    model=db_chat,
                    field_name='member_count_analyzer',
                    chat_id=db_chat.chat_id,
                    enabled=enabled,
                    create=False,
                )

                db_chat.update_or_create_message_views_analyzer(
                    model=db_chat,
                    field_name='message_view_analyzer',
                    chat_id=db_chat.chat_id,
                    enabled=enabled,
                    create=False,
                )

                db_chat.update_or_create_chat_shared_media_analyzer(
                    model=db_chat,
                    field_name='shared_media_analyzer',
                    chat_id=db_chat.chat_id,
                    enabled=enabled,
                    create=False,
                )
