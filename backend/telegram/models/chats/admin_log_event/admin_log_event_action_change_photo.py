from typing import Optional

from django.db import models, DatabaseError

from pyrogram import types
from telegram.globals import logger
from ...base import BaseModel


class AdminLogEventActionChangePhotoQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionChangePhoto']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionChangePhotoManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionChangePhotoQuerySet:
        return AdminLogEventActionChangePhotoQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            raw_action: 'types.ChannelAdminLogEventActionChangePhoto',
    ) -> Optional['AdminLogEventActionChangePhoto']:
        if raw_action is None:
            return None

        parsed_object = self._parse(raw_action=raw_action)
        return self.get_queryset().update_or_create_action(
            **parsed_object
        )

    @staticmethod
    def _parse(*, raw_action: 'types.ChannelAdminLogEventActionChangePhoto'):
        if raw_action is None:
            return {}

        return {
        }


class AdminLogEventActionChangePhoto(BaseModel):
    """
    The channel/supergroup's picture was changed
    """

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    objects = AdminLogEventActionChangePhotoManager()

    class Meta:
        verbose_name_plural = 'Events (change photo)'
