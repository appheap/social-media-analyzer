from django.db import models
from ...base import BaseModel


class AdminLogEventActionToggleAdmin(BaseModel):
    """
    The admin rights of a user were changed
    """
    prev_participant = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="action_toggle_admin_prev",
    )

    new_participant = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="action_toggle_admin_new",
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (toggle admin)'
