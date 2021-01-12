from typing import Optional

from django.db import models, DatabaseError

from ..base import BaseModel
from core.globals import logger
from telegram import models as tg_models


class AdminLogAnalyzerMetaDataQuerySet(models.QuerySet):
    def update_or_create_analyzer(self, *, defaults: dict, **kwargs) -> Optional['AdminLogAnalyzerMetaData']:
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

    def filter_by_id(self, *, id: int) -> 'AdminLogAnalyzerMetaDataQuerySet':
        return self.filter(id=id)


class AdminLogAnalyzerMetaDataManager(models.Manager):
    def get_queryset(self) -> AdminLogAnalyzerMetaDataQuerySet:
        return AdminLogAnalyzerMetaDataQuerySet(self.model, using=self._db)

    def update_or_create_analyzer(
            self,
            *,
            db_telegram_channel: 'tg_models.TelegramChannel',
            chat_id: int,
            enabled: bool,
    ) -> Optional['AdminLogAnalyzerMetaData']:
        if db_telegram_channel is None or chat_id is None:
            return None

        return self.get_queryset().update_or_create(
            id=chat_id,
            defaults={
                'telegram_channel': db_telegram_channel,
                'enabled': enabled,
            }
        )

    def update_analyzer(self, id: int, **kwargs) -> bool:
        return self.get_queryset().filter_by_id(id=id).update_analyzer(**kwargs)


class AdminLogAnalyzerMetaData(BaseModel):
    id = models.BigIntegerField(primary_key=True)  # `chat__chat_id`

    enabled = models.BooleanField(default=False)
    first_analyzed_ts = models.BigIntegerField(null=True, blank=True)
    last_analyzed_ts = models.BigIntegerField(null=True, blank=True)
    disable_ts = models.BigIntegerField(null=True, blank=True)
    disable_reason = models.TextField(max_length=256, null=True, blank=True)

    ######################################

    # current active telegram channel
    telegram_channel = models.OneToOneField(  # fixme: what's the usage?
        'telegram.TelegramChannel',
        on_delete=models.CASCADE,
        related_name='admin_log_analyzer_metadata',
        null=True, blank=True,
    )

    objects = AdminLogAnalyzerMetaDataManager()

    ######################################
    # `chat` : chat this analyzer metadata belongs to

    class Meta:
        verbose_name_plural = 'Analyzers (chat admin logs)'

    def __str__(self):
        return f"{self.id} : {self.enabled}"

    def update_fields(self, **kwargs) -> bool:
        return AdminLogAnalyzerMetaData.objects.update_analyzer(id=self.id, **kwargs)
