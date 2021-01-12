from typing import Optional

from django.core.validators import MinLengthValidator
from django.db import models, DatabaseError
import arrow

from ..base import BaseModel
from users import models as site_models
from core.globals import logger
from telegram import models as tg_models


class AddChannelRequestStatusTypes(models.TextChoices):
    INIT = 'INIT'
    CHANNEL_MEMBER = 'CHANNEL_MEMBER'
    CHANNEL_ADMIN = 'CHANNEL_ADMIN'


class AddChannelRequestQuerySet(models.QuerySet):
    def undone(self) -> 'AddChannelRequestQuerySet':
        return self.filter(done=False)

    def done(self) -> 'AddChannelRequestQuerySet':
        return self.filter(done=True)

    def get_by_username_and_user(
            self,
            *,
            channel_username: str,
            db_site_user: 'site_models.SiteUser'
    ) -> Optional['AddChannelRequest']:

        try:
            return self.get(channel_username=channel_username, site_user=db_site_user)
        except AddChannelRequest.DoesNotExist as e:
            pass
        except AddChannelRequest.MultipleObjectsReturned as e:
            logger.exception(e)
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def create_request(
            self,
            *,
            db_site_user: 'site_models.SiteUser',
            db_admin: 'tg_models.TelegramAccount',
            channel_username: str,
            db_telegram_channel: 'tg_models.TelegramChannel',
    ) -> Optional['AddChannelRequest']:

        try:
            return self.create(
                admin=db_admin,
                status=AddChannelRequestStatusTypes.CHANNEL_MEMBER,
                channel_username=channel_username,
                done=False,
                telegram_channel=db_telegram_channel,
                site_user=db_site_user,
            )
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AddChannelRequestManager(models.Manager):
    def get_queryset(self) -> AddChannelRequestQuerySet:
        return AddChannelRequestQuerySet(self.model, using=self._db)

    def get_undone_request(
            self,
            *,
            channel_username: str,
            db_site_user: 'site_models.SiteUser'
    ) -> Optional['AddChannelRequest']:
        if channel_username is None or db_site_user is None:
            return None

        return self.get_queryset().undone().get_by_username_and_user(
            channel_username=channel_username,
            db_site_user=db_site_user
        )

    def create_request(
            self,
            *,
            db_site_user: 'site_models.SiteUser',
            db_admin: 'tg_models.TelegramAccount',
            channel_username: str,
            db_telegram_channel: 'tg_models.TelegramChannel',
    ) -> Optional['AddChannelRequest']:
        if db_site_user is None or db_admin is None or channel_username is None or db_telegram_channel is None:
            return None

        return self.get_queryset().create_request(
            db_site_user=db_site_user,
            db_admin=db_admin,
            channel_username=channel_username,
            db_telegram_channel=db_telegram_channel
        )


class AddChannelRequest(BaseModel):
    done = models.BooleanField(null=False, default=False, )
    status = models.CharField(
        AddChannelRequestStatusTypes.choices,
        max_length=20,
        null=True, blank=True,
        default=AddChannelRequestStatusTypes.INIT,
    )
    channel_username = models.CharField(
        null=False,
        verbose_name='channel username',
        max_length=32,
        validators=[MinLengthValidator(5)])

    channel_id = models.BigIntegerField(
        null=True,
        blank=True,
        verbose_name='channel id',
    )

    # User who added made this request
    site_user = models.ForeignKey(
        'users.SiteUser',
        on_delete=models.CASCADE,
        verbose_name='Owner',
        related_name='telegram_channel_add_requests',
        null=False,
    )

    # telegram channel requested to be the admin of
    telegram_channel = models.ForeignKey(
        'telegram.TelegramChannel',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='add_requests',
    )

    # telegram account chosen to be the admin of the channel
    admin = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        related_name='telegram_channel_add_requests',
        null=False,
        verbose_name='admin',
    )

    # def get_absolute_url(self):
    #     return reverse('dashboard/')
    objects = AddChannelRequestManager()

    def __str__(self):
        return str(
            f"{arrow.get(self.created_ts)} : {self.site_user} : @{self.channel_username} : {self.admin}")
