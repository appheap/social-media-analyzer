import uuid

from db.models import BaseModel, SoftDeletableBaseModel
from django.db import models, transaction
from typing import List, Optional
from telegram import models as tg_models
from users import models as site_models

from db.models import SoftDeletableQS


class PostQuerySet(SoftDeletableQS):
    pass


class PostManager(models.Manager):
    def get_queryset(self) -> 'PostQuerySet':
        return PostQuerySet(self.model, using=self._db)

    def create_post(
            self,
            *,
            db_created_by: 'site_models.SiteUser',
            db_telegram_channel: 'tg_models.TelegramChannel',
            text: str = None,
            input_files: List['tg_models.InputFile'],
            is_scheduled: bool = False,
            upload_to_telegram_schedule_list: bool = None,
            schedule_date_ts: int = None,
    ) -> Optional['Post']:
        if db_created_by is None or db_telegram_channel is None:
            return None

        with transaction.atomic():

            db_post = Post(
                text=text,
                has_media=bool(len(input_files)),
                telegram_channel=db_telegram_channel,
                is_scheduled=is_scheduled,
                upload_to_telegram_schedule_list=upload_to_telegram_schedule_list,
                schedule_date_ts=schedule_date_ts,
            )
            if db_post:
                for input_file in input_files:
                    input_file.save()
                    db_post.medias.add(
                        input_file.file
                    )
            return db_post


class Post(BaseModel, SoftDeletableBaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    text = models.TextField(
        max_length=4096,
        null=True,
        blank=True,
    )
    medias = models.ManyToManyField(
        'telegram.File',
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

    is_sent = models.BooleanField(default=False)
    sent_date_ts = models.BigIntegerField(null=True, blank=True)

    # telegram account that published this post on telegram
    sent_by = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        related_name='sent_posts',
        null=True,
        blank=True,
    )

    sent_message = models.OneToOneField(
        'telegram.Message',
        on_delete=models.CASCADE,
        related_name='post_from_sent_message',
        null=True,
        blank=True,
    )

    is_scheduled = models.BooleanField(default=False)
    upload_to_telegram_schedule_list = models.BooleanField(null=True, blank=True)
    is_uploaded_to_telegram_schedule_list = models.BooleanField(null=True, blank=True)
    schedule_date_ts = models.BigIntegerField(null=True, blank=True)
    scheduled_message = models.OneToOneField(
        'telegram.Message',
        on_delete=models.CASCADE,
        related_name='post_from_scheduled_message',
        null=True,
        blank=True,
    )

    # creator of this post
    created_by = models.ForeignKey(
        'users.SiteUser',
        on_delete=models.CASCADE,
        related_name='telegram_posts',
        null=False,
        blank=True,
    )

    is_edited = models.BooleanField(default=False)
    edit_date_ts = models.BigIntegerField(null=True, blank=True)

    posts = PostManager()

    ##########################

    def __str__(self):
        return f'{self.created_by} : {self.telegram_channel} @ {self.created_ts}'
