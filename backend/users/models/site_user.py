from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as AbstractUserManager
from django.db import models

from core.globals import logger
from db import models as db_models
from .time_zones import TimeZones


class SiteUserQuerySet(db_models.SoftDeletableQS):
    def admins(self):
        return self.filter(is_superuser=True)


class SiteUserManager(AbstractUserManager):
    def get_user_by_id(
            self,
            *,
            user_id: int,
    ) -> "SiteUser":
        site_user = None
        try:
            site_user = self.get_queryset().get(pk=user_id)
        except SiteUser.DoesNotExist:
            pass
        except Exception as e:
            logger.exception(e)
        return site_user

    def get_user_by_username(
            self,
            *,
            username: str,
    ) -> "SiteUser":
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

    objects = SiteUserManager()

    ################################################
    # `telegram_accounts` : telegram accounts belonging to this user
    # `telegram_channels` : telegram channels belonging to this user
    # `telegram_channel_add_requests` : requests made by this user for adding telegram channels
    # `profile_photos` : profile photos belonging to this user

    def __str__(self):
        return self.username
