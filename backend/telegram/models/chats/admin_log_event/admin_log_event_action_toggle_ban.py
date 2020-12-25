from django.db import models
from ...base import BaseModel


class AdminLogEventActionToggleBan(BaseModel):
    """
    The banned rights of a user were changed
    """

    prev_participant = models.OneToOneField(
        'telegram.ChatMember',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="action_toggle_ban_prev",
    )

    new_participant = models.OneToOneField(
        'telegram.ChatMember',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="action_toggle_ban_new",
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (toggle ban)'
