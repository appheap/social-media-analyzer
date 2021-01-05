from typing import Optional

from django.db import models, DatabaseError

from core.globals import logger
from ..base import BaseModel


class SharedMediaAnalyzerMetaDataQuerySet(models.QuerySet):
    def update_or_create_analyzer(self, **kwargs) -> Optional['SharedMediaAnalyzerMetaData']:
        try:
            return self.update_or_create(
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

    def filter_by_id(self, *, id: int) -> 'SharedMediaAnalyzerMetaDataQuerySet':
        return self.filter(id=id)


class SharedMediaAnalyzerMetaDataManager(models.Manager):
    def get_queryset(self) -> SharedMediaAnalyzerMetaDataQuerySet:
        return SharedMediaAnalyzerMetaDataQuerySet(self.model, using=self._db)

    def update_or_create_analyzer(
            self,
            *,
            chat_id: int,
            enabled: bool,
    ) -> Optional['SharedMediaAnalyzerMetaData']:
        if chat_id is None:
            return None

        return self.get_queryset().update_or_create(
            **{
                'id': chat_id,
                'enabled': enabled,
            }
        )

    def update_analyzer(self, id: int, **kwargs) -> bool:
        return self.get_queryset().filter_by_id(id=id).update_analyzer(**kwargs)


class SharedMediaAnalyzerMetaData(BaseModel):
    id = models.BigIntegerField(primary_key=True)  # `chat__chat_id`

    enabled = models.BooleanField(default=False)
    first_analyzed_ts = models.BigIntegerField(null=True, blank=True)
    last_analyzed_ts = models.BigIntegerField(null=True, blank=True)
    disable_ts = models.BigIntegerField(null=True, blank=True)
    disable_reason = models.TextField(max_length=256, null=True, blank=True)

    ######################################

    ######################################
    # `chat` : chat this analyzer metadata belongs to

    objects = SharedMediaAnalyzerMetaDataManager()

    class Meta:
        verbose_name_plural = 'Analyzers (chat shared medias)'

    def __str__(self):
        return str(f" {self.id} : {self.enabled}")

    def update_fields(self, **kwargs) -> bool:
        return self.objects.update_analyzer(id=id, **kwargs)
