from django.db import models

from ...base import BaseModel


class AdminLogEventActionChangeLinkedChat(BaseModel):
    """
    The linked chat was changed
    """

    # Previous linked chat
    prev_value = models.IntegerField(null=True, blank=True, )
    # New linked chat
    new_value = models.IntegerField(null=True, blank=True, )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (change linked chat)'
