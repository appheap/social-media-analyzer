from typing import Optional

from django.db import models, DatabaseError

from pyrogram import types
from core.globals import logger
from ...base import BaseModel


class AdminLogEventActionToggleSignaturesQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionToggleSignatures']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionToggleSignaturesManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionToggleSignaturesQuerySet:
        return AdminLogEventActionToggleSignaturesQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            raw_action: 'types.ChannelAdminLogEventActionToggleSignatures',
    ) -> Optional['AdminLogEventActionToggleSignatures']:
        if raw_action is None:
            return None

        parsed_object = self._parse(raw_action=raw_action)
        if len(parsed_object):
            return self.get_queryset().update_or_create_action(
                **parsed_object
            )
        return None

    @staticmethod
    def _parse(*, raw_action: 'types.ChannelAdminLogEventActionToggleSignatures'):
        if raw_action is None:
            return {}

        return {
            'new_value': raw_action.new_value
        }


class AdminLogEventActionToggleSignatures(BaseModel):
    """
    Channel signatures were enabled/disabled
    """
    new_value = models.BooleanField()

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    objects = AdminLogEventActionToggleSignaturesManager()

    class Meta:
        verbose_name_plural = 'Events (toggle signatures)'
