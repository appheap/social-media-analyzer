import uuid

from db.models import BaseModel, SoftDeletableBaseModel
from django.db import models, transaction, DatabaseError
from typing import List, Optional
from telegram import models as tg_models
from users import models as site_models

from db.models import SoftDeletableQS
from core.globals import logger


class PostQuerySet(SoftDeletableQS):
    def filter_by_creator(self, creator: 'site_models.SiteUser') -> 'PostQuerySet':
        return self.filter(created_by=creator)

    def filter_by_channel(self, db_telegram_channel: 'tg_models.TelegramChannel') -> 'PostQuerySet':
        return self.filter(telegram_channel=db_telegram_channel)

    def get_post_by_id(self, *, post_id: str) -> Optional['Post']:
        try:
            return self.get(id=post_id)
        except Post.DoesNotExist as e:
            pass
        except Post.MultipleObjectsReturned as e:
            pass
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None

    def filter_by_creator_and_channel(
            self,
            db_creator: 'site_models.SiteUser',
            db_telegram_channel: 'tg_models.TelegramChannel'
    ) -> 'PostQuerySet':
        if db_creator is None or db_telegram_channel is None:
            return self.none()

        return self.filter(
            created_by=db_creator,
            telegram_channel=db_telegram_channel
        )


class PostManager(models.Manager):
    def get_queryset(self) -> 'PostQuerySet':
        return PostQuerySet(self.model, using=self._db)

    def get_site_user_posts(
            self,
            *,
            db_site_user: 'site_models.SiteUser',
    ) -> Optional['PostQuerySet']:
        if db_site_user is None:
            return None
        return self.get_queryset().filter_by_creator(db_site_user)

    def get_post_by_id(self, *, post_id: str):
        if post_id is None:
            return None
        return self.get_queryset().get_post_by_id(post_id=post_id)

    def create_post(
            self,
            *,
            db_created_by: 'site_models.SiteUser',
            db_telegram_channel: 'tg_models.TelegramChannel',
            text: str = None,
            files: List['tg_models.File'],
            is_scheduled: bool = False,
            upload_to_telegram_schedule_list: bool = None,
            schedule_date_ts: int = None,
    ) -> Optional['Post']:
        if db_created_by is None or db_telegram_channel is None:
            return None

        if text is None and len(files):
            return None

        with transaction.atomic():

            db_post = Post(
                text=text,
                has_media=bool(len(files)),
                telegram_channel=db_telegram_channel,
                is_scheduled=is_scheduled,
                upload_to_telegram_schedule_list=upload_to_telegram_schedule_list,
                schedule_date_ts=schedule_date_ts,
            )
            if db_post:
                for file in files:
                    db_post.medias.add(file)
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
        blank=True,
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
    media_group_id = models.BigIntegerField(null=True, blank=True)

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

    objects = PostManager()
    posts = PostManager()

    ##########################

    def __str__(self):
        return f'{self.created_by} : {self.telegram_channel} @ {self.created_ts}'

    def update_post_from_raw_message(
            self,
            *,
            db_message: 'tg_models.Message'
    ) -> Optional['tg_models.Post']:
        if db_message is None:
            return None

        self.sent_by = db_message.logged_by
        self.media_group_id = db_message.media_group_id
        if db_message.is_scheduled:
            self.is_uploaded_to_telegram_schedule_list = True
            self.scheduled_message = db_message
        else:
            self.is_sent = True
            self.sent_date_ts = db_message.date_ts
            self.sent_message = db_message

        self.save()

        return self
