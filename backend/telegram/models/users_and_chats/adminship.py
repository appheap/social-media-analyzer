from django.db import models

from ..base import BaseModel


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


class AdminShip(BaseModel):
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
    is_creator = models.BooleanField(null=True, blank=True, )
    join_date_ts = models.BigIntegerField(null=True, blank=True, )
    can_view_members = models.BooleanField(null=True, blank=True)
    can_set_username = models.BooleanField(null=True, blank=True)
    can_set_stickers = models.BooleanField(null=True, blank=True)
    can_view_stats = models.BooleanField(null=True, blank=True)
    is_prehistory_hidden = models.BooleanField(null=True, blank=True)
    admin_rights = models.ForeignKey(
        'telegram.AdminRights',
        on_delete=models.CASCADE,
        related_name='adminships',
        null=True,
        blank=True,
    )
    banned_rights = models.ForeignKey(
        'telegram.ChatPermissions',
        on_delete=models.CASCADE,
        related_name='adminships',
        null=True,
        blank=True,
    )

    # info from channel
    is_forbidden = models.BooleanField(null=True, blank=True, )
    forbidden_until_ts = models.BigIntegerField(null=True, blank=True, )

    # info from full_group
    # `can_set_username`

    # info from group
    is_kicked = models.BooleanField(null=True, blank=True, )

    # `admin_rights`
    # `is_forbidden`
    # `is_creator`

    class Meta:
        verbose_name_plural = 'Adminships'
        unique_together = [
            ('chat', 'account'),
        ]
        ordering = ['chat', 'account']

    ######################################
