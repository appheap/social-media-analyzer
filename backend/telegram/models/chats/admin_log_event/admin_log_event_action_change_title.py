from typing import Optional

from django.db import models, DatabaseError

from ...base import BaseModel
from telegram.globals import logger
from pyrogram import types


class AdminLogEventActionChangeTitleQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionChangeTitle']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionChangeTitleManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionChangeTitleQuerySet:
        return AdminLogEventActionChangeTitleQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            raw_action: 'types.ChannelAdminLogEventActionChangeTitle',
    ) -> Optional['AdminLogEventActionChangeTitle']:
        if raw_action is None:
            return None

        parsed_object = self._parse(raw_action=raw_action)
        if len(parsed_object):
            return self.get_queryset().update_or_create_action(
                **parsed_object
            )

        return None

    @staticmethod
    def _parse(*, raw_action: 'types.ChannelAdminLogEventActionChangeTitle'):
        if raw_action is None:
            return {}

        return {
            'prev_value': raw_action.prev_value,
            'new_value': raw_action.new_value,
        }


class AdminLogEventActionChangeTitle(BaseModel):
    """
    Channel/supergroup title was changed
    """
    prev_value = models.CharField(max_length=256, null=True, blank=True)
    new_value = models.CharField(max_length=256, null=True, blank=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    objects = AdminLogEventActionChangeTitleManager()

    class Meta:
        verbose_name_plural = 'Events (change title)'
