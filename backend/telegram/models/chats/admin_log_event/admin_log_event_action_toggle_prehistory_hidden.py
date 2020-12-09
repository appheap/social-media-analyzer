from django.db import models
from ...base import BaseModel


class AdminLogEventActionTogglePreHistoryHidden(BaseModel):
    """
    The hidden prehistory setting was changed
    """
    new_value = models.BooleanField()

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (prehistory hidden)'
