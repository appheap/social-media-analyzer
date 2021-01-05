from typing import Optional

from django.db import models, DatabaseError

from telegram import models as tg_models
from core.globals import logger
from ...base import BaseModel


class AdminLogEventActionToggleAdminQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionToggleAdmin']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionToggleAdminManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionToggleAdminQuerySet:
        return AdminLogEventActionToggleAdminQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            db_prev_chat_member: 'tg_models.ChatMember',
            db_new_chat_member: 'tg_models.ChatMember',
    ) -> Optional['AdminLogEventActionToggleAdmin']:
        if db_prev_chat_member is None or db_new_chat_member is None:
            return None

        return self.get_queryset().update_or_create_action(
            **{
                'prev_participant': db_prev_chat_member,
                'new_participant': db_new_chat_member,
            }
        )


class AdminLogEventActionToggleAdmin(BaseModel):
    """
    The admin rights of a user were changed
    """
    prev_participant = models.OneToOneField(
        'telegram.ChatMember',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="action_toggle_admin_prev",
    )

    new_participant = models.OneToOneField(
        'telegram.ChatMember',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="action_toggle_admin_new",
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    objects = AdminLogEventActionToggleAdminManager()

    class Meta:
        verbose_name_plural = 'Events (toggle admin)'
