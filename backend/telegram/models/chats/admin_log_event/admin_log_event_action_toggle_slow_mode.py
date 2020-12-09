from django.db import models

from ...base import BaseModel


class AdminLogEventActionToggleSlowMode(BaseModel):
    """
    Slow mode setting for supergroups was changed
    """

    # Previous slow mode value
    prev_value = models.IntegerField(null=True, blank=True, )
    # New slow mode value
    new_value = models.IntegerField(null=True, blank=True, )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (toggle slow mode)'
