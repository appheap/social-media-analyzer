from typing import Union, Optional

import arrow
from django.db import DatabaseError, transaction
from django.db import models

from pyrogram import types
from telegram import models as tg_models
from core.globals import logger
from ..base import BaseModel


class UserQuerySet(models.QuerySet):
    def filter_by_user_id(self, user_id: int) -> "UserQuerySet":
        return self.filter(user_id=user_id)

    def get_by_user_id(self, *, user_id: int) -> "User":
        try:
            instance = self.get(user_id=user_id)
        except User.DoesNotExist:
            instance = None
        except Exception as e:
            logger.exception(e)
            instance = None
        return instance

    def user_exists(self, *, user_id: int) -> bool:
        return self.filter_by_user_id(user_id=user_id).exists()

    def update_or_create_user(self, **kwargs) -> Optional["User"]:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def update_user(self, **kwargs) -> bool:
        try:
            return bool(
                self.update(
                    **kwargs
                )
            )
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return False

    def create_user(self, **kwargs) -> "User":
        try:
            return self.create(
                **kwargs
            )
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def user_deleted_account(self, *, user_id: int, delete_ts: int) -> bool:
        try:
            return bool(
                self.filter_by_user_id(user_id=user_id).update(user_deleted_ts=delete_ts)
            )
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return False


class UserManager(models.Manager):
    def get_queryset(self) -> "UserQuerySet":
        return UserQuerySet(self.model, using=self._db)

    def update_from_raw(self, *, user_id: int, raw_user: Union[types.User, types.UserFull]) -> bool:
        if not user_id or not user_id:
            return False

        is_full_type = isinstance(raw_user, types.UserFull)
        parsed_object = self._parse_full_user(raw_user) if is_full_type else self._parse_user(raw_user)
        if parsed_object is None:
            return None
        updated = False
        with transaction.atomic():
            user_qs = self.get_queryset().filter_by_user_id(user_id=user_id)
            updated = user_qs.update_user(**parsed_object)
            self.create_restrictions(raw_user.user if is_full_type else raw_user, user_qs[0])
        return updated

    def update_or_create_from_raw(
            self,
            *,
            raw_user: Union[types.User, types.UserFull],

            db_message_view: 'tg_models.MessageView' = None,
    ) -> Optional["User"]:
        if not raw_user:
            return None
        is_full_type = isinstance(raw_user, types.UserFull)
        parsed_object = self._parse_full_user(raw_user) if is_full_type else self._parse_user(raw_user)
        if parsed_object is None:
            return None
        with transaction.atomic():
            user = self.get_queryset().update_or_create_user(
                **{
                    **parsed_object,

                    'message_view': db_message_view,
                }
            )
            self.create_restrictions(raw_user.user if is_full_type else raw_user, user)
        return user

    def get_user_by_id(self, *, user_id: int) -> Optional['User']:
        if user_id is None:
            return None
        return self.get_queryset().get_by_user_id(user_id=user_id)

    def user_deleted_account(self, *, user_id: int, delete_ts: int) -> bool:
        if user_id is None or delete_ts is None:
            return False
        return self.get_queryset().user_deleted_account(user_id=user_id, delete_ts=delete_ts)

    @staticmethod
    def create_restrictions(raw_user: types.User, user: "User"):
        if user and raw_user.restrictions:
            tg_models.Restriction.objects.bulk_create_restrictions(
                raw_restrictions=raw_user.restrictions,
                user=user
            )

    @staticmethod
    def _parse_full_user(full_user: types.UserFull):  # todo: profile photo?
        if full_user is None:
            return None

        return {
            'is_blocked': full_user.blocked,
            'can_we_pin_message': full_user.can_pin_message,
            'about': full_user.about,
            'common_chats_count': full_user.common_chats_count,
            **(UserManager._parse_user(full_user.user) if full_user.user else {})
        }

    @staticmethod
    def _parse_user(user: types.User):  # todo: profile photo?
        if user is None:
            return None

        return {
            'id': user.id,
            'is_empty': user.is_empty,
            'is_mutual_contact': user.is_mutual_contact,
            'is_deleted': user.is_deleted,
            'is_bot': user.is_bot,
            'is_verified': user.is_verified,
            'is_restricted': user.is_restricted,
            'is_scam': user.is_scam,
            'is_support': user.is_support,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.last_name,
            'language_code': user.language_code,
            'dc_id': user.dc_id,
            'phone_number': user.phone_number,
            'bot_inline_placeholder': user.bot_inline_placeholder,
            'bot_can_see_history': user.bot_can_see_history,
            'bot_can_request_geo': user.bot_can_request_geo,
        }


class User(BaseModel):
    user_id = models.BigIntegerField(primary_key=True)

    # info from raw full_user
    is_blocked = models.BooleanField(null=True, blank=True)
    can_we_pin_message = models.BooleanField(null=True, blank=True)
    about = models.TextField(max_length=256, null=True, blank=True)
    common_chats_count = models.IntegerField(null=True, blank=True)

    # info from both
    # `profile_photos`

    # info from raw user
    is_empty = models.BooleanField(null=True, blank=True)
    is_mutual_contact = models.BooleanField(null=True, blank=True)
    is_deleted = models.BooleanField(null=True, blank=True)
    is_bot = models.BooleanField(null=True, blank=True)
    is_verified = models.BooleanField(null=True, blank=True)
    is_restricted = models.BooleanField(null=True, blank=True)
    is_scam = models.BooleanField(null=True, blank=True)
    is_support = models.BooleanField(null=True, blank=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    username = models.CharField(max_length=32, null=True, blank=True)
    language_code = models.CharField(max_length=20, null=True, blank=True)
    dc_id = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    bot_inline_placeholder = models.CharField(max_length=256, null=True, blank=True)
    bot_can_see_history = models.BooleanField(null=True, blank=True)
    bot_can_request_geo = models.BooleanField(null=True, blank=True)

    ##############################################################
    user_deleted_ts = models.BigIntegerField(null=True, blank=True)

    message_view = models.ForeignKey(
        'telegram.MessageView',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='recent_user_repliers',
    )

    users = UserManager()

    # `telegram_accounts` : telegram accounts connected to this user
    # `restrictions` : restrictions of this user if it's a bot
    # `admin_log_mentions` : admin logs this user is mentioned in
    # `admin_log_events` : admin logs this user has committed
    # `forwarded_messages` : forwarded messages from this user
    # `saved_messages` : saved messages from this user
    # `sent_messages` : sent messages from this user
    # `message_replies` : replies to this user
    # `via_bot_messages` : messages (inline queries) that were generated by this bot in a chat
    # `mentioned_entities` : entities that this user is mentioned in
    # `chats` : chats this users is/was member of (including state; is current member or left the chat)
    # `chat_peers` : chats with this user fixme: maybe a better name?
    # `promoted_participants` : channel participants promoted by this user
    # `demoted_participants` : channel participants demoted by this user
    # `invited_participants` : channel participants invited by this user
    # `kicked_participants` : channel participants kicked by this user
    # `profile_photos` : profile photos belonging to this user

    class Meta:
        pass

    def __str__(self):
        # return str(self.first_name if self.first_name else "") + str(self.last_name if self.last_name else "")
        return f"{self.first_name if self.first_name else self.last_name if self.last_name else ''} `@{self.username if self.username else self.user_id}`"

    def user_deleted_account(self, *, delete_ts: int = None):
        self.user_deleted_ts = delete_ts if delete_ts else arrow.now().utcnow()
        self.save()

    def update_fields_from_raw(self, *, raw_user: Union[types.User, types.UserFull]) -> bool:
        return self.users.update_from_raw(user_id=self.user_id, raw_user=raw_user)
