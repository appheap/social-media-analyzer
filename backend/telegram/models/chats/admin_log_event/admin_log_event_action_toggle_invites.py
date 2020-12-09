from django.db import models
from ...base import BaseModel


class AdminLogEventActionToggleInvites(BaseModel):
    """
    Invites were enabled/disabled
    """
    new_value = models.BooleanField()

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (toggle invites)'
