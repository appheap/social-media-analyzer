from typing import Optional

from django.db import models, DatabaseError

from telegram import models as tg_models
from telegram.globals import logger
from ...base import BaseModel


class AdminLogEventActionParticipantInviteQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionParticipantInvite']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionParticipantInviteManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionParticipantInviteQuerySet:
        return AdminLogEventActionParticipantInviteQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            db_chat_member: 'tg_models.ChatMember',
    ) -> Optional['AdminLogEventActionParticipantInvite']:
        if db_chat_member is None:
            return None

        return self.get_queryset().update_or_create_action(
            **{
                'participant': db_chat_member,
            }
        )


class AdminLogEventActionParticipantInvite(BaseModel):
    """
    A user was invited to the group
    """

    # The user that was invited
    participant = models.OneToOneField(
        'telegram.ChatMember',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="action_participant_invite",
    )

    objects = AdminLogEventActionParticipantInviteManager()

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to
    class Meta:
        verbose_name_plural = 'Events (participant invite)'
