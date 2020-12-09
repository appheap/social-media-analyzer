from django.db import models

from ...base import BaseModel


class AdminLogEventActionDeleteMessage(BaseModel):
    """
    A message was deleted
    """

    # The message that was deleted
    message = models.OneToOneField(
        'telegram.Message',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='action_delete_message',
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (message deletion)'
