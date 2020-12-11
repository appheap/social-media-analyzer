from django.db import models
from ..base import BaseModel


class Channel(BaseModel):
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

    ############################################
    # `chat` : chat this channel belongs to
