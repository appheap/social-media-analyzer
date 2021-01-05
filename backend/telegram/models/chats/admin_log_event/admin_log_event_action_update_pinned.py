from typing import Optional

from django.db import models, DatabaseError

from telegram import models as tg_models
from telegram.globals import logger
from ...base import BaseModel


class AdminLogEventActionUpdatePinnedQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionUpdatePinned']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionUpdatePinnedManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionUpdatePinnedQuerySet:
        return AdminLogEventActionUpdatePinnedQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            db_message: 'tg_models.Message'
    ) -> Optional['AdminLogEventActionUpdatePinned']:
        if db_message is None:
            return None

        return self.get_queryset().update_or_create_action(
            **{
                'message': db_message,
            }
        )


class AdminLogEventActionUpdatePinned(BaseModel):
    """
    A message was pinned
    """

    # The message that was pinned
    message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        related_name='actions_update_pinned',
        null=True, blank=True,
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    objects = AdminLogEventActionUpdatePinnedManager()

    class Meta:
        verbose_name_plural = 'Events (message pinned)'
