from django.db import models

# this model is used as proxy to control access,etc to the objects they refer to
from ..base import BaseModel


class TelegramAccount(BaseModel):
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

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.BigIntegerField(null=True, blank=True)

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

    def __str__(self):
        return str(self.username if self.username else "") + str(self.first_name if self.first_name else "") + str(
            self.last_name if self.last_name else "")
