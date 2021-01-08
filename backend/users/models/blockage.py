from django.db import models

from db import models as db_models


class TimeZones(models.TextChoices):
    UTC = 'UTC'
    ASIA_TEHRAN = 'Asia/Tehran'


class BlockageTypes(models.TextChoices):
    OTHER = 'OTHER'
    FOREVER = 'FOREVER'
    TEMPORARY = 'TEMPORARY'
    SPAM = 'SPAM'


class Blockage(db_models.BaseModel):
    blocked = models.BooleanField(default=False)
    blocked_ts = models.BigIntegerField(null=True, blank=True)
    blocked_reason = models.CharField(
        max_length=256,
        null=True, blank=True,
    )
    blocked_type = models.CharField(
        BlockageTypes.choices,
        max_length=255,
        null=True, blank=True,
    )
    blocked_until_ts = models.BigIntegerField(
        null=True, blank=True,
        default=0,
    )

    ##################################################
    # `user` : the user who this blockage belongs to
    # `telegram_account` : the telegram account this blockage belongs to
    # `telegram_channel` : the telegram channel this blockage belongs to

    def __str__(self):
        return self.blocked_reason
