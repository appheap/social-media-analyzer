from django.db import models

from ...base import BaseModel


class AdminLogEventActionStopPoll(BaseModel):
    """
    A poll was stopped
    """

    # The poll that was stopped
    message = models.ForeignKey(
        'telegram.Message',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='actions_stop_poll',
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (stop poll)'
