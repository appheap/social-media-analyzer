from typing import Optional

from django.db import models, DatabaseError

from pyrogram import types
from core.globals import logger
from ...base import BaseModel


class AdminLogEventActionChangeLocationQuerySet(models.QuerySet):
    def update_or_create_action(self, **kwargs) -> Optional['AdminLogEventActionChangeLocation']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventActionChangeLocationManager(models.Manager):
    def get_queryset(self) -> AdminLogEventActionChangeLocationQuerySet:
        return AdminLogEventActionChangeLocationQuerySet(self.model, using=self._db)

    def update_or_create_action(
            self,
            *,
            raw_action: 'types.ChannelAdminLogEventActionChangeLocation',
    ) -> Optional['AdminLogEventActionChangeLocation']:
        if raw_action is None:
            return None

        parsed_object = self._parse(raw_action=raw_action)
        if len(parsed_object):
            return self.get_queryset().update_or_create_action(
                **parsed_object
            )
        return None

    @staticmethod
    def _parse(*, raw_action: 'types.ChannelAdminLogEventActionChangeLocation'):
        if raw_action is None:
            return {}

        _dict = {}
        if raw_action.prev_value:
            _dict.update(
                {
                    'prev_address': raw_action.prev_value.address,
                    'prev_lat': raw_action.prev_value.geo_point.latitude if raw_action.prev_value.geo_point else None,
                    'prev_long': raw_action.prev_value.geo_point.longitude if raw_action.prev_value.geo_point else None,
                    'prev_access_hash': raw_action.prev_value.geo_point.access_hash if raw_action.prev_value.geo_point else None,
                }
            )

        if raw_action.new_value:
            _dict.update(
                {

                    'new_address': raw_action.new_value.address,
                    'new_lat': raw_action.new_value.geo_point.latitude if raw_action.new_value.geo_point else None,
                    'new_long': raw_action.new_value.geo_point.longitude if raw_action.new_value.geo_point else None,
                    'new_access_hash': raw_action.new_value.geo_point.access_hash if raw_action.new_value.geo_point else None,
                }
            )
        return _dict


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

    objects = AdminLogEventActionChangeLocationManager()

    class Meta:
        verbose_name_plural = 'Events (change location)'
