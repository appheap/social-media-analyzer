from typing import Optional

from django.db import models, DatabaseError

from pyrogram import types
from telegram.globals import logger
from ...base import BaseModel


class AdminLogEventActionTogglePreHistoryHiddenQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionTogglePreHistoryHidden']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionTogglePreHistoryHiddenManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionTogglePreHistoryHiddenQuerySet:
        return AdminLogEventActionTogglePreHistoryHiddenQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            raw_action: 'types.ChannelAdminLogEventActionTogglePreHistoryHidden',
    ) -> Optional['AdminLogEventActionTogglePreHistoryHidden']:
        if raw_action is None:
            return None

        parsed_object = self._parse(raw_action=raw_action)
        if len(parsed_object):
            return self.get_queryset().update_or_create_action(
                **parsed_object
            )
        return None

    @staticmethod
    def _parse(*, raw_action: 'types.ChannelAdminLogEventActionTogglePreHistoryHidden'):
        if raw_action is None:
            return {}

        return {
            'new_value': raw_action.new_value
        }


class AdminLogEventActionTogglePreHistoryHidden(BaseModel):
    """
    The hidden prehistory setting was changed
    """
    new_value = models.BooleanField()

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    objects = AdminLogEventActionTogglePreHistoryHiddenManager()

    class Meta:
        verbose_name_plural = 'Events (prehistory hidden)'
