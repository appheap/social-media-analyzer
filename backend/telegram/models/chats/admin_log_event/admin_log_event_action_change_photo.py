from django.db import models
from ...base import BaseModel


class AdminLogEventActionChangePhoto(BaseModel):
    """
    The channel/supergroup's picture was changed
    """

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (change photo)'
