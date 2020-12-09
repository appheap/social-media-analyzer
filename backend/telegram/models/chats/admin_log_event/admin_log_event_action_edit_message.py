from django.db import models

from ...base import BaseModel


class AdminLogEventActionEditMessage(BaseModel):
    """
    A message was edited
    """

    # old message
    prev_message = models.ForeignKey(
        'telegram.Message',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='actions_edit_message_prev',
    )

    # new message
    new_message = models.ForeignKey(
        'telegram.Message',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='actions_edit_message_new',
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (message edit)'
