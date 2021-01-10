from typing import Optional, List

from django.db import models, DatabaseError

# this model is used as proxy to control access,etc to the objects they refer to
from ..base import BaseModel
from db.models import SoftDeletableBaseModel
from db.models import SoftDeletableQS
from core.globals import logger
from pyrogram import types
import pyrogram
from users import models as site_models
from telegram import models as tg_models


class TelegramAccountQuerySet(SoftDeletableQS):
    def update_or_create_account(self, **kwargs) -> Optional['TelegramAccount']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def get_by_user_id(self, user_id: int) -> Optional['TelegramAccount']:
        try:
            return self.get(user_id=user_id)
        except TelegramAccount.DoesNotExist as e:
            pass
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def get_telegram_accounts_by_ids(
            self,
            *,
            ids: List['int']
    ) -> List['TelegramAccount']:
        return self.filter(
            user_id__in=ids
        )


class TelegramAccountManager(models.Manager):
    def get_queryset(self) -> TelegramAccountQuerySet:
        return TelegramAccountQuerySet(self.model, using=self._db)

    def get_telegram_accounts_by_ids(
            self,
            *,
            ids: List['int']
    ) -> Optional[List['TelegramAccount']]:

        if ids is None or not len(ids):
            return None

        return self.get_queryset().get_telegram_accounts_by_ids(
            ids=ids
        )

    def update_or_create_from_raw(
            self,
            *,
            db_site_user: 'site_models.SiteUser',
            db_user: 'tg_models.User',
            client: 'pyrogram.Client',

    ) -> Optional['TelegramAccount']:

        if db_site_user is None or db_user is None or client is None:
            return None

        parsed_object = self._parse(db_user=db_user)
        if len(parsed_object):
            db_account = self.get_queryset().update_or_create_account(
                **{
                    **parsed_object,
                    'site_user': db_site_user,
                    'telegram_user': db_user,
                    'api_id': client.api_id,
                    'api_hash': client.api_hash,
                    'session_name': client.session_name,
                }
            )
            return db_account

        return None

    @staticmethod
    def _parse(*, db_user: 'tg_models.User') -> dict:
        if db_user is None:
            return {}

        return {
            'user_id': db_user.user_id,
            'username': db_user.username,
            'first_name': db_user.first_name,
            'last_name': db_user.last_name,
            'is_bot': db_user.is_bot,
            'is_restricted': db_user.is_restricted,
            'is_scam': db_user.is_scam,
            'is_verified': db_user.is_verified,
            'phone_number': db_user.phone_number,
            'dc_id': db_user.dc_id,
            'language_code': db_user.language_code,
        }


class TelegramAccount(BaseModel, SoftDeletableBaseModel):
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=32, null=True, blank=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    is_bot = models.BooleanField(default=False)
    is_restricted = models.BooleanField(default=False)
    is_scam = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    dc_id = models.IntegerField(null=True, blank=True)
    language_code = models.CharField(max_length=5, null=True, blank=True)

    # fields needed for telegram client api
    api_id = models.CharField(max_length=256, null=True, blank=True)
    api_hash = models.CharField(max_length=256, null=True, blank=True)
    session_name = models.CharField(max_length=256, null=True, blank=True)

    # `telegram_channels` : telegram channels added by this account
    # `chats` : chats added by this account
    # `telegram_channel_add_requests` : requests for adding telegram channel this account is requested to be admin of
    # `admin_log_events` : admin log events logged by this account
    # `logged_messages` : messages logged by this account
    # `message_views` : message views logged by this account
    # `member_count_history` : member counts logged by this account
    # `shared_media_history` : shared media counts logged by this account
    # `dialogs` : dialogs belonging to this account

    # User who is the owner of this telegram account
    site_user = models.ForeignKey(
        'users.SiteUser',
        on_delete=models.CASCADE,
        related_name='telegram_accounts',
        null=True, blank=True,
    )

    # Telegram User this account belongs to
    telegram_user = models.ForeignKey(
        'telegram.User',
        related_name='telegram_accounts',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )

    # the blockage object
    blockage = models.OneToOneField(
        'users.Blockage',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='telegram_account',
    )

    accounts = TelegramAccountManager()

    def __str__(self):
        return str(self.username if self.username else "") + str(self.first_name if self.first_name else "") + str(
            self.last_name if self.last_name else "")
