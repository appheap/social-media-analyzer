from typing import Optional

from django.db import models, DatabaseError, transaction

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
    def update_or_create_adminship(self, **kwargs) -> Optional['AdminShip']:
        try:
            return self.update_or_create(
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


class AdminShipManger(models.Manager):
    def get_queryset(self) -> AdminShipQuerySet:
        return AdminShipQuerySet(self.model, using=self._db)

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
                    **{
                        **parsed_object,
                        'account': db_account,
                        'chat': db_chat,
                        'role': role_type,
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
            db_adminship.update_or_create_chat_permissions_from_raw(
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
                    'can_set_username': raw_chat.full_channel.can_set_username,

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
        related_name='adminships',
        null=True,
        blank=True,
    )
    banned_rights = models.OneToOneField(
        'telegram.ChatPermissions',
        on_delete=models.CASCADE,
        related_name='adminships',
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

    ######################################
