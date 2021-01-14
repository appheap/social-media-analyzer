from typing import Optional, List

from django.db import models, DatabaseError, transaction
from django.utils.functional import cached_property

from ..base import BaseModel
from telegram import models as tg_models
from pyrogram import types
from core.globals import logger
from ..chats import ChatPermissionsUpdater
from ..chats import ChatAdminRightsUpdater


class Role(models.TextChoices):  # fixme: maybe a better name?
    user = 'user'  # not member yet, only a telegram user (when banned/promoted before joining the channel)
    member = 'member'
    self = 'self'
    administrator = 'administrator'
    creator = 'creator'
    restricted = 'restricted'
    kicked = 'kicked'
    left = 'left'
    undefined = 'undefined'


class AdminShipQuerySet(models.QuerySet):
    def update_or_create_adminship(self, *, defaults: dict, **kwargs) -> Optional['AdminShip']:
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

    def update_adminship(self, **kwargs) -> bool:
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

        return None

    def filter_by_id(self, *, id: int) -> 'AdminShipQuerySet':
        return self.filter(id=id)

    def filter_by_chat(self, *, db_chat: 'tg_models.Chat') -> 'AdminShipQuerySet':
        return self.filter(chat=db_chat)

    def filter_by_admins_and_creators(self) -> 'AdminShipQuerySet':
        return self.filter(role_type__in=(Role.administrator, Role.creator))

    def filter_by_session_names(self, *, session_names: List['str']) -> 'AdminShipQuerySet':
        return self.filter(account__session_name__in=session_names)


class AdminShipManger(models.Manager):
    def get_queryset(self) -> AdminShipQuerySet:
        return AdminShipQuerySet(self.model, using=self._db)

    def get_telegram_accounts_by_account_session_names(
            self,
            *,
            db_chat: 'tg_models.Chat',
            session_names: List['str'],
            with_admin_permissions: bool = False,
    ) -> List['tg_models.TelegramAccount']:
        if db_chat is None or session_names is None or not len(session_names):
            return None

        queryset = self.get_queryset().filter_by_chat(db_chat=db_chat)
        if with_admin_permissions:
            queryset = queryset.filter_by_admins_and_creators()
        db_adminships = queryset.filter_by_session_names(session_names=session_names)

        if db_adminships:
            db_accounts = []
            for db_adminship in db_adminships:
                db_accounts.append(db_adminship.account)

            return db_accounts

        return None

    def update_or_create_from_raw(
            self,
            *,
            db_account: 'tg_models.TelegramAccount',
            db_chat: 'tg_models.Chat',
            raw_chat: types.Chat,
    ) -> Optional['AdminShip']:

        if db_account is None or db_chat is None or raw_chat is None:
            return None

        parsed_object = self._parse(raw_chat=raw_chat)
        if len(parsed_object):
            role_type = tg_models.Role.member
            if raw_chat.is_creator:
                role_type = tg_models.Role.creator

            if raw_chat.is_admin:
                role_type = tg_models.Role.administrator

            if raw_chat.has_left:
                role_type = tg_models.Role.left

            with transaction.atomic():
                db_adminship = self.get_queryset().update_or_create_adminship(
                    account=db_account,
                    chat=db_chat,
                    defaults={
                        **parsed_object,
                        'role_type': role_type,
                    }
                )
                if db_adminship:
                    self._update_related_fields(db_adminship=db_adminship, raw_chat=raw_chat)

                return db_adminship
        return None

    def update_from_raw(
            self,
            *,
            id: int,
            role_type: Role,
            raw_chat: types.Chat,
    ) -> bool:

        if id is None or role_type is None or raw_chat is None:
            return False

        parsed_object = self._parse(raw_chat=raw_chat)
        if len(parsed_object):
            _updated = False
            with transaction.atomic():
                db_adminship_qs = self.get_queryset().filter_by_id(id=id)

                _updated = db_adminship_qs.update_adminship(
                    **{
                        **parsed_object,
                        'role': role_type,
                    }
                )
                self._update_related_fields(db_adminship=db_adminship_qs[0], raw_chat=raw_chat)

            return _updated

        return False

    @staticmethod
    def _update_related_fields(*, db_adminship: 'AdminShip', raw_chat: types.Chat):
        if raw_chat.channel:
            db_adminship.update_or_create_chat_permissions_from_raw_obj(
                model=db_adminship,
                field_name='banned_rights',
                raw_chat_permissions=raw_chat.channel.banned_rights
            )
            db_adminship.update_or_create_chat_admin_rights_from_raw(
                model=db_adminship,
                field_name='admin_rights',
                raw_chat_admin_rights=raw_chat.channel.admin_rights
            )
        if raw_chat.group:
            db_adminship.update_or_create_chat_admin_rights_from_raw(
                model=db_adminship,
                field_name='admin_rights',
                raw_chat_admin_rights=raw_chat.group.admin_rights
            )

    @staticmethod
    def _parse(*, raw_chat: types.Chat) -> dict:
        if raw_chat is None:
            return {}
        _dict = {}
        if raw_chat.full_channel is not None:
            _dict.update(
                {
                    'can_view_members': raw_chat.full_channel.can_view_participants,
                    'can_set_username': raw_chat.full_channel.can_set_username,
                    'can_set_stickers': raw_chat.full_channel.can_set_stickers,
                    'can_view_stats': raw_chat.full_channel.can_view_stats,
                    'is_prehistory_hidden': raw_chat.full_channel.is_prehistory_hidden,
                }
            )
        if raw_chat.channel:
            _dict.update(
                {
                    'is_creator': raw_chat.channel.is_creator,
                    'join_date_ts': raw_chat.channel.date,
                    'is_forbidden': raw_chat.channel.is_forbidden,
                    'forbidden_until_ts': raw_chat.channel.forbidden_until,
                }
            )

        if raw_chat.full_group:
            _dict.update(
                {
                    'can_set_username': raw_chat.full_group.can_set_username,
                }
            )

        if raw_chat.group:
            _dict.update(
                {
                    'is_kicked': raw_chat.group.is_kicked,
                    'is_forbidden': raw_chat.group.is_forbidden,
                    'is_creator': raw_chat.group.is_creator,
                }
            )
        return _dict


class AdminShip(BaseModel, ChatPermissionsUpdater, ChatAdminRightsUpdater):
    account = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        related_name='+',
    )

    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        related_name='+',
    )

    role_type = models.CharField(
        max_length=64,
        null=False,
        choices=Role.choices,
        default=Role.undefined,
    )

    # info from full_channel
    can_view_members = models.BooleanField(null=True, blank=True)
    can_set_username = models.BooleanField(null=True, blank=True)
    can_set_stickers = models.BooleanField(null=True, blank=True)
    can_view_stats = models.BooleanField(null=True, blank=True)
    is_prehistory_hidden = models.BooleanField(null=True, blank=True)

    # info from channel
    is_creator = models.BooleanField(null=True, blank=True, )
    join_date_ts = models.BigIntegerField(null=True, blank=True, )
    is_forbidden = models.BooleanField(null=True, blank=True, )
    forbidden_until_ts = models.BigIntegerField(null=True, blank=True, )
    admin_rights = models.OneToOneField(
        'telegram.ChatAdminRights',
        on_delete=models.CASCADE,
        related_name='adminship',
        null=True,
        blank=True,
    )
    banned_rights = models.OneToOneField(
        'telegram.ChatPermissions',
        on_delete=models.CASCADE,
        related_name='adminship',
        null=True,
        blank=True,
    )

    # info from full_group
    # `can_set_username`

    # info from group
    is_kicked = models.BooleanField(null=True, blank=True, )

    # `admin_rights`
    # `is_forbidden`
    # `is_creator`

    objects = AdminShipManger()

    class Meta:
        verbose_name_plural = 'Adminships'
        unique_together = [
            ('chat', 'account'),
        ]
        ordering = ['chat', 'account']

    def __str__(self):
        return self.name

    @cached_property
    def name(self):
        return f'{self.account} @ {self.chat} : {self.role_type}'
    ######################################
