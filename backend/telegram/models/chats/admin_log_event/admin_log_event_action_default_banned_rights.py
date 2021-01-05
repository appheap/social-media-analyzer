from typing import Optional

from django.db import models, DatabaseError

from telegram import models as tg_models
from core.globals import logger
from ...base import BaseModel


class AdminLogEventActionDefaultBannedRightsQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionDefaultBannedRights']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionDefaultBannedRightsManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionDefaultBannedRightsQuerySet:
        return AdminLogEventActionDefaultBannedRightsQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            prev_banned_rights: 'tg_models.ChatPermissions',
            new_banned_rights: 'tg_models.ChatPermissions',

    ) -> Optional['AdminLogEventActionDefaultBannedRights']:
        if prev_banned_rights is None or new_banned_rights is None:
            return None

        return self.get_queryset().update_or_create_action(
            **{
                'prev_banned_rights': prev_banned_rights,
                'new_banned_rights': new_banned_rights,
            }
        )


class AdminLogEventActionDefaultBannedRights(BaseModel):
    """
    The default banned rights were modified
    """
    # Previous global banned rights
    prev_banned_rights = models.OneToOneField(
        'telegram.ChatPermissions',
        on_delete=models.CASCADE,
        related_name='action_banned_rights_prev',
        null=True, blank=True,
    )

    # New global banned rights.
    new_banned_rights = models.OneToOneField(
        'telegram.ChatPermissions',
        on_delete=models.CASCADE,
        related_name='action_banned_rights_new',
        null=True, blank=True,
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    objects = AdminLogEventActionDefaultBannedRightsManager()

    class Meta:
        verbose_name_plural = 'Events (default banned rights)'
