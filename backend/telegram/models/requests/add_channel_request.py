from django.core.validators import MinLengthValidator
from django.db import models
import arrow

from ..base import BaseModel


class AddChannelRequestStatusTypes(models.TextChoices):
    INIT = 'INIT'
    CHANNEL_MEMBER = 'CHANNEL_MEMBER'
    CHANNEL_ADMIN = 'CHANNEL_ADMIN'


class AddChannelRequest(BaseModel):
    done = models.BooleanField(null=False, default=False, )
    status = models.CharField(
        AddChannelRequestStatusTypes.choices,
        max_length=20,
        null=True, blank=True,
        default=AddChannelRequestStatusTypes.INIT,
    )
    channel_username = models.CharField(
        null=False,
        verbose_name='channel username',
        max_length=32,
        validators=[MinLengthValidator(5)])

    channel_id = models.BigIntegerField(
        null=True,
        blank=True,
        verbose_name='channel id',
    )

    # User who added made this request
    site_user = models.ForeignKey(
        'users.SiteUser',
        on_delete=models.CASCADE,
        verbose_name='Owner',
        related_name='telegram_channel_add_requests',
        null=False,
    )

    # telegram channel requested to be the admin of
    telegram_channel = models.ForeignKey(
        'telegram.TelegramChannel',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='add_requests',
    )

    # telegram account chosen to be the admin of the channel
    telegram_account = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        related_name='telegram_channel_add_requests',
        null=False,
        verbose_name='admin',
    )

    # def get_absolute_url(self):
    #     return reverse('dashboard/')
    def __str__(self):
        return str(
            f"{arrow.get(self.created_at)} : {self.custom_user} : @{self.channel_username} : {self.telegram_account}")
