from django.db import models
from ...base import BaseModel


class AdminLogEventActionChangeUsername(BaseModel):
    """
    Channel/supergroup username was changed
    """
    prev_value = models.CharField(max_length=32, null=True, blank=True)
    new_value = models.CharField(max_length=32, null=True, blank=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (change username)'
