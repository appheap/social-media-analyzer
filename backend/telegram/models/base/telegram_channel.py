from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse

from ..base import BaseModel


class TelegramChannel(BaseModel):
    channel_id = models.BigIntegerField()
    is_account_creator = models.BooleanField(null=True, blank=True)
    is_account_admin = models.BooleanField(null=False, default=False, )
    is_active = models.BooleanField(null=False, default=False, )

    username = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name='username',
        validators=[MinLengthValidator(5)],
    )
    is_public = models.BooleanField(default=False, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.BigIntegerField(null=True, blank=True)

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

    def __str__(self):
        return str(self.chat.title) if self.chat else str(self.username)

    def get_absolute_url(self):
        return reverse('dashboard:accounts')
