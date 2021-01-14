from typing import Optional

from django.db import models, DatabaseError
import arrow

from ..base import BaseModel
from core.globals import logger
from telegram import models as tg_models


class ChatMemberCountQuerySet(models.QuerySet):
    def update_or_create_chat_member_count(self, *, defaults: dict, **kwargs) -> Optional['ChatMemberCount']:
        try:
            return self.update_or_create(
                defaults=defaults,
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class ChatMemberCountManager(models.Manager):
    def get_queryset(self) -> ChatMemberCountQuerySet:
        return ChatMemberCountQuerySet(self.model, using=self._db)

    def update_or_create_from_raw(
            self,
            *,
            db_chat: 'tg_models.Chat',
            count: int,
            date_ts: int,
            logger_account: 'tg_models.TelegramAccount'
    ) -> Optional['ChatMemberCount']:
        if db_chat is None or count is None or date_ts is None or logger_account is None:
            return None

        return self.get_queryset().update_or_create_chat_member_count(
            id=f'{db_chat.chat_id}:{date_ts}',
            defaults={
                'count': count,
                'date_ts': date_ts,
                'chat': db_chat,
                'logged_by': logger_account,
            }
        )


class ChatMemberCount(BaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat__chat_id:date_ts`

    count = models.BigIntegerField()
    date_ts = models.BigIntegerField()

    # Chat this object belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=False,
        related_name='member_count_history',
    )

    ############################
    # TODO add more fields if you can
    # Telegram account who logged this member count
    logged_by = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='member_count_history',
    )

    objects = ChatMemberCountManager()

    class Meta:
        ordering = ('-date_ts',)
        get_latest_by = ('-date_ts',)

    def __str__(self):
        return f"{self.chat} : {self.count} @ {arrow.get(self.date_ts)}"
