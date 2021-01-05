from typing import Optional

from django.db import models, DatabaseError

from pyrogram import types
from core.globals import logger
from ...base import BaseModel


class AdminLogEventActionChangeLinkedChatQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionChangeLinkedChat']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionChangeLinkedChatManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionChangeLinkedChatQuerySet:
        return AdminLogEventActionChangeLinkedChatQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            raw_action: 'types.ChannelAdminLogEventActionChangeLinkedChat',
    ) -> Optional['AdminLogEventActionChangeLinkedChat']:
        if raw_action is None:
            return None

        parsed_object = self._parse(raw_action=raw_action)
        if len(parsed_object):
            return self.get_queryset().update_or_create_action(
                **parsed_object
            )
        return None

    @staticmethod
    def _parse(*, raw_action: 'types.ChannelAdminLogEventActionChangeLinkedChat'):
        if raw_action is None:
            return {}

        return {
            'prev_value': raw_action.prev_value,
            'new_value': raw_action.new_value
        }


class AdminLogEventActionChangeLinkedChat(BaseModel):
    """
    The linked chat was changed
    """

    # Previous linked chat
    prev_value = models.IntegerField(null=True, blank=True, )
    # New linked chat
    new_value = models.IntegerField(null=True, blank=True, )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    objects = AdminLogEventActionChangeLinkedChatManager()

    class Meta:
        verbose_name_plural = 'Events (change linked chat)'
