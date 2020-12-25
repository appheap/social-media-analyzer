from django.db import models

from ...base import BaseModel


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

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to
    class Meta:
        verbose_name_plural = 'Events (participant invite)'
