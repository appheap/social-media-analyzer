from typing import Optional

from django.db import models, DatabaseError

from telegram import models as tg_models
from telegram.globals import logger
from ...base import BaseModel


class AdminLogEventActionStopPollQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionStopPoll']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionStopPollManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionStopPollQuerySet:
        return AdminLogEventActionStopPollQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            db_message: 'tg_models.Message'
    ) -> Optional['AdminLogEventActionStopPoll']:
        if db_message is None:
            return None

        return self.get_queryset().update_or_create_action(
            **{
                'message': db_message,
            }
        )


class AdminLogEventActionStopPoll(BaseModel):
    """
    A poll was stopped
    """

    # The poll that was stopped
    message = models.ForeignKey(
        'telegram.Message',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='actions_stop_poll',
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (stop poll)'
