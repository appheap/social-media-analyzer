from typing import Optional

from django.core.validators import MinLengthValidator
from django.db import models, DatabaseError
from django.urls import reverse

from db.models import SoftDeletableQS
from db.models import SoftDeletableBaseModel
from pyrogram import types
from telegram import models as tg_models
from telegram.globals import logger
from users import models as site_models
from ..base import BaseModel


class TelegramChannelQuerySet(SoftDeletableQS):
    def update_or_create_channel(self, **kwargs) -> Optional['TelegramChannel']:
        try:
            return self.update_or_create(
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


class TelegramChannelManager(models.Manager):
    def get_queryset(self) -> TelegramChannelQuerySet:
        return TelegramChannelQuerySet(self.model, using=self._db)

    def update_or_create_from_raw(
            self,
            *,
            raw_chat: types.Chat,
            db_site_user: 'site_models.SiteUser',
            db_account: 'tg_models.TelegramAccount',
            db_chat: 'tg_models.Chat',
    ) -> Optional['TelegramChannel']:

        if raw_chat is None or db_site_user is None or db_account is None or db_chat is None:
            return None

        parsed_object = self._parse(raw_chat=raw_chat)
        if len(parsed_object):
            db_channel = self.get_queryset().update_or_create_channel(
                **{
                    **parsed_object,
                    'site_user': db_site_user,
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
            'channel_id': raw_chat.id,
            'is_account_creator': raw_chat.channel.is_creator,
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
