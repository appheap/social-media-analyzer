from django.contrib.auth.models import AbstractUser
from django.db import models

from core.globals import logger
from db import models as db_models


class TimeZones(models.TextChoices):
    UTC = 'UTC'
    ASIA_TEHRAN = 'Asia/Tehran'


class BlockageTypes(models.TextChoices):
    OTHER = 'OTHER'
    FOREVER = 'FOREVER'
    TEMPORARY = 'TEMPORARY'
    SPAM = 'SPAM'


class SiteUserQuerySet(db_models.SoftDeletableQS):
    def admins(self):
        return self.filter(is_superuser=True)


class SiteUserManager(models.Manager):
    def get_user_by_id(self, user_id: int) -> "SiteUser":
        site_user = None
        try:
            site_user = self.get_queryset().get(pk=user_id)
        except SiteUser.DoesNotExist:
            pass
        except Exception as e:
            logger.exception(e)
        return site_user

    def get_user_by_username(self, username: str) -> "SiteUser":
        site_user = None
        try:
            site_user = self.get_queryset().get(username=username.lower())
        except SiteUser.DoesNotExist:
            pass
        except Exception as e:
            logger.exception(e)
        return site_user

    def get_queryset(self):
        return SiteUserQuerySet(self.model, using=self._db)


class SiteUser(db_models.BaseModel, db_models.SoftDeletableBaseModel, AbstractUser):
    is_email_verified = models.BooleanField(default=False)
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

    users = SiteUserManager()

    ################################################
    # `telegram_accounts` : telegram accounts belonging to this user
    # `telegram_channels` : telegram channels belonging to this user
    # `telegram_channel_add_requests` : requests made by this user for adding telegram channels

    def __str__(self):
        return self.username


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
