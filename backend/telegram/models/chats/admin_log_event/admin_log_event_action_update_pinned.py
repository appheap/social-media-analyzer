from django.db import models
from ...base import BaseModel


class AdminLogEventActionUpdatePinned(BaseModel):
    """
    A message was pinned
    """

    # The message that was pinned
    message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        related_name='actions_update_pinned',
        null=True, blank=True,
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (message pinned)'
