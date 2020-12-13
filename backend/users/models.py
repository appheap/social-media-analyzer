import arrow
from django.contrib.auth.models import AbstractUser
from django.db import models


class TimeZones(models.TextChoices):
    UTC = 'UTC'
    ASIA_TEHRAN = 'Asia/Tehran'


class BlockageTypes(models.TextChoices):
    OTHER = 'OTHER'
    FOREVER = 'FOREVER'
    TEMPORARY = 'TEMPORARY'
    SPAM = 'SPAM'


class SiteUser(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    is_deleted = models.BooleanField(null=True, blank=True)
    deleted_at = models.BigIntegerField(null=True, blank=True)
    created_at = models.BigIntegerField(default=0)
    modified_at = models.BigIntegerField(default=0)

    timezone = models.CharField(
        choices=TimeZones.choices,
        default=TimeZones.UTC,
        max_length=40
    )

    blockage = models.OneToOneField(
        'users.Blockage',
        on_delete=models.SET_NULL,
        verbose_name='the blockage object',
        null=True, blank=True,
        related_name='user',
    )

    ################################################
    # `telegram_accounts` : telegram accounts belonging to this user
    # `telegram_channels` : telegram channels belonging to this user
    # `telegram_channel_add_requests` : requests made by this user for adding telegram channels

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created = arrow.utcnow().timestamp
        self.modified = arrow.utcnow().timestamp
        return super(SiteUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class Blockage(models.Model):
    blocked = models.BooleanField(default=False)
    blocked_at = models.BigIntegerField(null=True, blank=True)
    blocked_reason = models.CharField(
        max_length=256,
        null=True, blank=True,
    )
    blocked_type = models.CharField(
        BlockageTypes.choices,
        max_length=255,
        null=True, blank=True,
    )
    blocked_until = models.BigIntegerField(
        null=True, blank=True,
        default=0,
    )

    created_at = models.BigIntegerField(default=0)
    modified_at = models.BigIntegerField(default=0)

    ##################################################
    # `user` : the user who this blockage belongs to
    # `telegram_account` : the telegram account this blockage belongs to
    # `telegram_channel` : the telegram channel this blockage belongs to

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(Blockage, self).save(*args, **kwargs)

    def __str__(self):
        return self.blocked_reason
