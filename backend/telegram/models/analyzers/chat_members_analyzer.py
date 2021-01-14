from django.db import models, DatabaseError

from typing import Optional

from ..base import BaseModel

from core.globals import logger
from telegram import models as tg_models


class ChatMembersAnalyzerMetaDataQuerySet(models.QuerySet):
    def update_or_create_analyzer(self, *, defaults: dict, **kwargs) -> Optional['ChatMembersAnalyzerMetaData']:
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

    def update_analyzer(self, **kwargs) -> bool:
        try:
            return bool(
                self.update(
                    **kwargs
                )
            )
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return False

    def filter_by_id(self, *, id: int) -> 'ChatMembersAnalyzerMetaDataQuerySet':
        return self.filter(id=id)


class ChatMembersAnalyzerMetaDataManager(models.Manager):
    def get_queryset(self) -> ChatMembersAnalyzerMetaDataQuerySet:
        return ChatMembersAnalyzerMetaDataQuerySet(self.model, using=self._db)

    def update_or_create_analyzer(
            self,
            *,
            chat_id: int,
            enabled: bool,
    ) -> Optional['ChatMembersAnalyzerMetaData']:
        if chat_id is None:
            return None

        return self.get_queryset().update_or_create(
            id=chat_id,
            defaults={
                'enabled': enabled,
            }
        )

    def update_analyzer(self, *, id: int, **kwargs) -> bool:
        return self.get_queryset().filter_by_id(id=id).update_analyzer(**kwargs)


class ChatMembersAnalyzerMetaData(BaseModel):
    id = models.BigIntegerField(primary_key=True)  # `chat__chat_id`

    enabled = models.BooleanField(default=False)
    first_analyzed_ts = models.BigIntegerField(null=True, blank=True)
    last_analyzed_ts = models.BigIntegerField(null=True, blank=True)
    disable_ts = models.BigIntegerField(null=True, blank=True)
    disable_reason = models.TextField(max_length=256, null=True, blank=True)

    ######################################
    # current active telegram channel
    # telegram_channel = models.OneToOneField(  # fixme: what's the usage?
    #     'telegram.TelegramChannel',
    #     on_delete=models.SET_NULL,
    #     related_name='chat_member_analyzer_metadata',
    #     null=True, blank=True,
    # )

    ######################################
    # `chat` : chat this analyzer metadata belongs to

    objects = ChatMembersAnalyzerMetaDataManager()

    class Meta:
        verbose_name_plural = 'Analyzers (chat members)'

    def __str__(self):
        return f"{self.id} : {self.enabled}"

    def update_fields(self, **kwargs) -> bool:
        return ChatMembersAnalyzerMetaData.objects.update_analyzer(id=self.id, **kwargs)
