from django.db import models

from ...base import BaseModel


class AdminLogEventActionChangeTitle(BaseModel):
    """
    Channel/supergroup title was changed
    """
    prev_value = models.CharField(max_length=256, null=True, blank=True)
    new_value = models.CharField(max_length=256, null=True, blank=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (change title)'
