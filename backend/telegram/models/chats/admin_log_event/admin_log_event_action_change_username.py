from typing import Optional

from django.db import models, DatabaseError

from pyrogram import types
from core.globals import logger
from ...base import BaseModel


class AdminLogEventActionChangeUsernameQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionChangeUsername']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionChangeUsernameManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionChangeUsernameQuerySet:
        return AdminLogEventActionChangeUsernameQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            raw_action: 'types.ChannelAdminLogEventActionChangeUsername',
    ) -> Optional['AdminLogEventActionChangeUsername']:
        if raw_action is None:
            return None

        parsed_object = self._parse(raw_action=raw_action)
        if len(parsed_object):
            return self.get_queryset().update_or_create_action(
                **parsed_object
            )

        return None

    @staticmethod
    def _parse(*, raw_action: 'types.ChannelAdminLogEventActionChangeUsername'):
        if raw_action is None:
            return {}

        return {
            'prev_value': raw_action.prev_value,
            'new_value': raw_action.new_value,
        }


class AdminLogEventActionChangeUsername(BaseModel):
    """
    Channel/supergroup username was changed
    """
    prev_value = models.CharField(max_length=32, null=True, blank=True)
    new_value = models.CharField(max_length=32, null=True, blank=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    objects = AdminLogEventActionChangeUsernameManager()

    class Meta:
        verbose_name_plural = 'Events (change username)'
