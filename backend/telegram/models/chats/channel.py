from typing import Optional

from django.db import DatabaseError
from django.db import models, transaction

from pyrogram import types
from core.globals import logger
from .chat_permissions_updater import ChatPermissionsUpdater
from .chat_updater import ChatUpdater
from ..base import BaseModel


class ChannelQuerySet(models.QuerySet):
    def update_or_create_channel(self, **kwargs) -> Optional["Channel"]:
        try:
            return self.update_or_create(**kwargs)
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None

    def filter_by_id(self, *, id: int) -> "ChannelQuerySet":
        return self.filter(id=id)


class ChannelManager(models.Manager):
    def get_queryset(self) -> ChannelQuerySet:
        return ChannelQuerySet(self.model, using=self._db)

    def update_from_raw_chat(
            self,
            *,
            id: int,
            raw_chat: types.Chat
    ) -> bool:

        if not id or not raw_chat:
            return False

        updated = False
        channel_qs = self.get_queryset().filter_by_id(id=id)
        parsed_full_channel = self._parse_full_channel(channel=raw_chat.full_channel)
        parsed_channel = self._parse_channel(channel=raw_chat.channel)
        if parsed_full_channel or parsed_channel:
            with transaction.atomic():
                updated = bool(
                    channel_qs.update(
                        **{
                            **parsed_full_channel,
                            **parsed_channel,
                        }
                    )
                )
                if updated:
                    db_channel = channel_qs[0]
                    if db_channel:
                        db_channel.update_or_create_chat_permissions_from_raw_obj(
                            model=db_channel,
                            field_name='default_banned_rights',
                            raw_chat_permissions=raw_chat.channel.default_banned_rights
                        )
                        if len(parsed_full_channel):
                            db_channel.update_or_create_chat_from_raw(
                                model=self,
                                field_name='migrated_from',
                                raw_chat=raw_chat.full_channel.migrated_from
                            )
                            db_channel.update_or_create_chat_from_raw(
                                model=self,
                                field_name='linked_chat',
                                raw_chat=raw_chat.full_channel.linked_chat
                            )
        return updated

    def update_or_create_from_raw(
            self,
            *,
            full_channel: types.ChannelFull,
            channel: types.Channel,
            creator: types.User = None
    ):
        if full_channel is None and channel is None:
            return None
        parsed_full_channel = self._parse_full_channel(channel=full_channel)
        parsed_channel = self._parse_channel(channel=channel)
        if parsed_full_channel or parsed_channel:
            with transaction.atomic():
                db_channel = self.get_queryset().update_or_create_channel(
                    **{
                        **parsed_full_channel,
                        **parsed_channel,
                        'creator': creator,  # fixme: what about creator?
                    }
                )
                if db_channel:
                    db_channel.update_or_create_chat_permissions_from_raw(
                        model=self,
                        field_name='default_banned_rights',
                        raw_chat_permissions=channel.default_banned_rights
                    )
                    if full_channel:
                        db_channel.update_or_create_chat_from_raw(
                            model=self,
                            field_name='migrated_from',
                            raw_chat=full_channel.migrated_from
                        )
                        db_channel.update_or_create_chat_from_raw(
                            model=self,
                            field_name='linked_chat',
                            raw_chat=full_channel.linked_chat
                        )
        else:
            return None

    @staticmethod
    def _parse_channel(*, channel: types.Channel) -> Optional[dict]:
        if channel is None:
            return {}
        return {
            'has_private_join_link': channel.has_private_join_link,
            'has_geo': channel.has_geo,
            'is_restricted': channel.is_restricted,
            'is_scam': channel.is_scam,
            'is_verified': channel.is_verified,
            'signatures_enabled': channel.signatures_enabled,
            'slow_mode_enabled': channel.slow_mode,
            'create_date_ts': channel.date if channel.left else None,
        }

    @staticmethod
    def _parse_full_channel(*, channel: types.ChannelFull) -> Optional[dict]:
        if channel is None:
            return {}
        return {
            'is_anonymous_admin_blocked': channel.is_blocked,
            'members_count': channel.members_count,
            'admins_count': channel.admins_count,
            'kicked_count': channel.kicked_count,
            'banned_count': channel.banned_count,
            'about': channel.about,
            'invite_link': channel.invite_link,
            'migrated_from_message_id': channel.migrated_from_max_id,
            'min_available_message_id': channel.min_available_message_id,
            'slow_mode_seconds': channel.slowmode_seconds,
            'stats_dc': channel.stats_dc,
        }


class Channel(BaseModel, ChatPermissionsUpdater, ChatUpdater):
    id = models.BigIntegerField(primary_key=True)

    # info from full_channel
    is_anonymous_admin_blocked = models.BooleanField(null=True, blank=True)
    members_count = models.IntegerField(null=True, blank=True)
    admins_count = models.IntegerField(null=True, blank=True)
    kicked_count = models.IntegerField(null=True, blank=True)
    banned_count = models.IntegerField(null=True, blank=True)
    about = models.TextField(max_length=256, null=True, blank=True)
    invite_link = models.CharField(max_length=256, null=True, blank=True)
    migrated_from = models.OneToOneField(
        'telegram.Chat',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='migrated_to',
    )
    migrated_from_message_id = models.IntegerField(null=True, blank=True, )
    min_available_message_id = models.IntegerField(null=True, blank=True, )
    linked_chat = models.ForeignKey(
        'telegram.Chat',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='linked_chat_reverse',
    )
    slow_mode_seconds = models.IntegerField(null=True, blank=True, )
    stats_dc = models.IntegerField(null=True, blank=True, )

    # info from channel
    title = models.CharField(max_length=256, null=True, blank=True, )
    username = models.CharField(max_length=32, null=True, blank=True, )
    creator = models.ForeignKey(
        'telegram.User',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='created_channels',
    )
    has_private_join_link = models.BooleanField(null=True, blank=True, )
    has_geo = models.BooleanField(null=True, blank=True, )
    is_restricted = models.BooleanField(null=True, blank=True, )
    is_scam = models.BooleanField(null=True, blank=True, )
    is_verified = models.BooleanField(null=True, blank=True)
    signatures_enabled = models.BooleanField(null=True, blank=True, )
    slow_mode_enabled = models.BooleanField(null=True, blank=True, )
    create_date_ts = models.BigIntegerField(null=True, blank=True, )
    default_banned_rights = models.OneToOneField(
        'telegram.ChatPermissions',
        models.CASCADE,
        null=True,
        blank=True,
        related_name='channel'
    )
    # `admin_rights`
    # `banned_rights`

    objects = ChannelManager()

    ############################################
    # `chat` : chat this channel belongs to

    def update_fields_from_raw_chat(self, *, raw_chat: types.Chat) -> bool:
        if not raw_chat:
            return False
        return self.objects.update_from_raw_chat(id=self.id, raw_chat=raw_chat)
