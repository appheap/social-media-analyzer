import uuid

from db.models import BaseModel, SoftDeletableBaseModel
from django.db import models


class Post(BaseModel, SoftDeletableBaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    text = models.TextField(
        max_length=1024,
        null=True,
        blank=True,
    )
    medias = models.ManyToManyField(
        'db.File',
        related_name='telegram_posts',
    )
    has_media = models.BooleanField(default=False)

    # channel this post is uploaded to
    telegram_channel = models.ForeignKey(
        'telegram.TelegramChannel',
        on_delete=models.CASCADE,
        related_name='posts',
        null=False,
    )

    # creator of this post
    created_by = models.ForeignKey(
        'users.SiteUser',
        on_delete=models.CASCADE,
        null=False,
        related_name='telegram_posts',
    )

    is_edited = models.BooleanField(default=False)
    edit_date_ts = models.BigIntegerField(null=True, blank=True)
    is_scheduled = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)
    sent_date_ts = models.BigIntegerField(null=True, blank=True)

    ##########################

    def __str__(self):
        return f'{self.created_by} : {self.telegram_channel} @ {self.created_ts}'
