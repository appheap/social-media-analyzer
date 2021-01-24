from typing import Optional

from django.core.validators import MinLengthValidator
from django.db import models, DatabaseError
from django.urls import reverse

from core.globals import logger
from db.models import SoftDeletableBaseModel
from db.models import SoftDeletableQS
from pyrogram import types
from telegram import models as tg_models
from users import models as site_models
from ..base import BaseModel


class TelegramChannelQuerySet(SoftDeletableQS):
    def update_or_create_channel(self, *, defaults: dict, **kwargs) -> Optional['TelegramChannel']:
        try:
            return self.update_or_create(
                defaults=defaults,
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def get_by_channel_id(self, channel_id: int) -> Optional['TelegramChannel']:
        try:
            return self.get(channel_id=channel_id)
        except TelegramChannel.DoesNotExist as e:
            pass
        except TelegramChannel.MultipleObjectsReturned as e:
            pass
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def filter_by_site_user(self, *, db_site_user: 'site_models.SiteUser') -> 'TelegramChannelQuerySet':
        return self.filter(site_user=db_site_user)

    def filter_by_channel_username(self, *, username: 'str') -> 'TelegramChannelQuerySet':
        return self.filter(username=username)


class TelegramChannelManager(models.Manager):
    def get_queryset(self) -> TelegramChannelQuerySet:
        return TelegramChannelQuerySet(self.model, using=self._db)

    def get_by_channel_id(self, *, channel_id: int) -> Optional['TelegramChannel']:
        return self.get_queryset().get_by_channel_id(channel_id=channel_id)

    def telegram_channel_exists(
            self,
            *,
            db_site_user: 'site_models.SiteUser',
            channel_username: str,
    ) -> Optional['bool']:
        if db_site_user is None or channel_username is None:
            return None

        return self.get_queryset() \
            .filter_by_site_user(db_site_user=db_site_user) \
            .filter_by_channel_username(username=channel_username) \
            .exists()

    def get_user_telegram_channels(
            self,
            db_site_user: 'site_models.SiteUser',
    ) -> 'TelegramChannelQuerySet':
        return self.get_queryset().filter_by_site_user(db_site_user=db_site_user)

    def update_or_create_from_raw(
            self,
            *,
            raw_chat: types.Chat,
            db_site_user: 'site_models.SiteUser',
            db_account: 'tg_models.TelegramAccount',
            db_chat: 'tg_models.Chat',

            create: bool = True,
    ) -> Optional['TelegramChannel']:

        if raw_chat is None or db_account is None or db_chat is None:
            return None

        if create and db_site_user is None:
            raise ValueError('`db_site_user` cannot be None')

        parsed_object = self._parse(raw_chat=raw_chat)
        if len(parsed_object):
            if create:
                parsed_object.update(
                    {
                        'site_user': db_site_user,
                    }
                )
            db_channel = self.get_queryset().update_or_create_channel(
                channel_id=raw_chat.id,
                defaults={
                    **parsed_object,
                    'chat': db_chat,
                    'telegram_account': db_account
                }
            )

            return db_channel

        return None

    @staticmethod
    def _parse(*, raw_chat: types.Chat) -> dict:
        if raw_chat is None:
            return {}

        return {
            'is_account_creator': raw_chat.channel.is_creator,
            'is_account_admin': raw_chat.is_admin,
            'username': raw_chat.channel.username.lower() if getattr(raw_chat.channel, 'username', None) else None,
            'is_public': raw_chat.channel.username is not None
        }


class TelegramChannel(BaseModel, SoftDeletableBaseModel):
    channel_id = models.BigIntegerField()
    is_account_creator = models.BooleanField(null=True, blank=True)
    is_account_admin = models.BooleanField(null=False, default=False)
    is_active = models.BooleanField(null=False, default=False)

    username = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name='username',
        validators=[MinLengthValidator(5)],
    )
    is_public = models.BooleanField(default=False, null=True, blank=True)

    # User who added this telegram channel
    site_user = models.ForeignKey(
        'users.SiteUser',
        on_delete=models.CASCADE,
        related_name='telegram_channels',
        null=True, blank=True,
    )

    # telegram account which added this channel
    telegram_account = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        related_name='telegram_channels',
        null=False,
        verbose_name='admin',
    )

    # Chat this channel belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='telegram_channels',
    )

    # the blockage object
    blockage = models.OneToOneField(
        'users.Blockage',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='telegram_channel',
    )

    ################################################
    # `chat_member_analyzer_metadata` : chat member analyzer of this channel
    # `admin_log_analyzer_metadata` : admin log analyzer of this channel
    # `add_requests` : requests made for adding this channel to an user's accounts

    channels = TelegramChannelManager()

    def __str__(self):
        return str(self.chat.title) if self.chat else str(self.username)

    def get_absolute_url(self):
        return reverse('dashboard:accounts')
