from typing import Optional

from django.db import models, DatabaseError

from telegram import models as tg_models
from core.globals import logger
from ...base import BaseModel


class AdminLogEventActionDeleteMessageQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionDeleteMessage']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionDeleteMessageManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionDeleteMessageQuerySet:
        return AdminLogEventActionDeleteMessageQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            db_message: 'tg_models.Message'
    ) -> Optional['AdminLogEventActionDeleteMessage']:
        if db_message is None:
            return None

        return self.get_queryset().update_or_create_action(
            **{
                'message': db_message,
            }
        )


class AdminLogEventActionDeleteMessage(BaseModel):
    """
    A message was deleted
    """

    # The message that was deleted
    message = models.OneToOneField(
        'telegram.Message',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='action_delete_message',
    )

    objects = AdminLogEventActionDeleteMessageManager()

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (message deletion)'
