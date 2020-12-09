from django.db import models

from ...base import BaseModel


class AdminLogEventActionChangeLocation(BaseModel):
    """
    The geogroup location was changed
    """

    prev_address = models.CharField(max_length=256, null=True, blank=True)
    prev_lat = models.FloatField(null=True, blank=True)
    prev_long = models.FloatField(null=True, blank=True)
    prev_access_hash = models.BigIntegerField(null=True, blank=True)

    new_address = models.CharField(max_length=256, null=True, blank=True)
    new_lat = models.FloatField(null=True, blank=True)
    new_long = models.FloatField(null=True, blank=True)
    new_access_hash = models.BigIntegerField(null=True, blank=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (change location)'
