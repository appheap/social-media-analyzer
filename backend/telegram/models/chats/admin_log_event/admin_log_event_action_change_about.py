from typing import Optional

from django.db import models, DatabaseError

from pyrogram import types
from telegram.globals import logger
from ...base import BaseModel


class AdminLogEventActionChangeAboutQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionChangeAbout']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionChangeAboutManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionChangeAboutQuerySet:
        return AdminLogEventActionChangeAboutQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            raw_action: 'types.ChannelAdminLogEventActionChangeAbout',
    ) -> Optional['AdminLogEventActionChangeAbout']:
        if raw_action is None:
            return None

        parsed_object = self._parse(raw_action=raw_action)
        if len(parsed_object):
            return self.get_queryset().update_or_create_action(
                **parsed_object
            )

        return None

    @staticmethod
    def _parse(*, raw_action: 'types.ChannelAdminLogEventActionChangeAbout'):
        if raw_action is None:
            return {}

        return {
            'prev_value': raw_action.prev_value,
            'new_value': raw_action.new_value,
        }


class AdminLogEventActionChangeAbout(BaseModel):
    """
    The description was changed
    """
    prev_value = models.CharField(max_length=256, null=True, blank=True)
    new_value = models.CharField(max_length=256, null=True, blank=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    objects = AdminLogEventActionChangeAboutManager()

    class Meta:
        verbose_name_plural = 'Events (change about)'
