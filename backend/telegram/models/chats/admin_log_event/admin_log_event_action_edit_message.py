from typing import Optional

from django.db import models, DatabaseError

from telegram import models as tg_models
from telegram.globals import logger
from ...base import BaseModel


class AdminLogEventActionEditMessageQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionEditMessage']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionEditMessageManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionEditMessageQuerySet:
        return AdminLogEventActionEditMessageQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            prev_db_message: 'tg_models.Message',
            new_db_message: 'tg_models.Message',

    ) -> Optional['AdminLogEventActionEditMessage']:
        if prev_db_message is None or new_db_message is None:
            return None

        return self.get_queryset().update_or_create_action(
            **{
                'prev_message': prev_db_message,
                'new_message': new_db_message,
            }
        )


class AdminLogEventActionEditMessage(BaseModel):
    """
    A message was edited
    """

    # old message
    prev_message = models.ForeignKey(
        'telegram.Message',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='actions_edit_message_prev',
    )

    # new message
    new_message = models.ForeignKey(
        'telegram.Message',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='actions_edit_message_new',
    )

    objects = AdminLogEventActionEditMessageManager()

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (message edit)'
