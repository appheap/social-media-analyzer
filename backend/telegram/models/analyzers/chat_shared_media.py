from typing import Optional, List

from django.db import models, DatabaseError
import arrow
from pyrogram import types
from telegram import models as tg_models
from ..base import BaseModel
from telegram.globals import logger

_filter_names = (
    'photo',
    'video',
    'document',
    'music',
    'voice',
    'url',
    'video_note',
    'animation',
    'location',
    'contact',
)


class ChatSharedMediaQuerySet(models.QuerySet):
    def update_or_create_shared_media(self, **kwargs) -> Optional["ChatSharedMedia"]:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class ChatShardMediaManager(models.Manager):
    def get_queryset(self) -> ChatSharedMediaQuerySet:
        return ChatSharedMediaQuerySet(self.model, using=self._db)

    def update_or_create_shared_media_from_raw(
            self,
            *,
            raw_search_counters: List['types.SearchCounter'],
            db_chat: 'tg_models.Chat',
            logger_account: 'tg_models.TelegramAccount',
            date_ts: int,
    ) -> Optional['ChatSharedMedia']:

        if raw_search_counters is None or not len(raw_search_counters) or db_chat is None or date_ts is None:
            return None

        kwargs = {}
        for raw_search_counter in raw_search_counters:
            if raw_search_counter.filter_name in _filter_names:
                kwargs[raw_search_counter.filter_name] = raw_search_counter.count
            else:
                raise ValueError(f'Invalid filter name : {raw_search_counter.filter_name}')

        return self.get_queryset().update_or_create_shared_media(
            **{
                **kwargs,
                'id': f'{db_chat.chat_id}:{date_ts}',
                'chat': db_chat,
                'logged_by': logger_account,
            }
        )


class ChatSharedMedia(BaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat__chat_id:date_ts`

    # date of getting this query
    date_ts = models.BigIntegerField()

    photo = models.IntegerField(default=0)
    video = models.IntegerField(default=0)
    document = models.IntegerField(default=0)
    music = models.IntegerField(default=0)
    url = models.IntegerField(default=0)
    voice = models.IntegerField(default=0)
    video_note = models.IntegerField(default=0)
    animation = models.IntegerField(default=0)
    location = models.IntegerField(default=0)
    contact = models.IntegerField(default=0)

    # Chat this shared media belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=False,
        related_name='shared_media_history',
    )

    ############################
    # TODO add more fields if you can
    # Telegram account who logged this member count
    logged_by = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='shared_media_history',
    )

    objects = ChatShardMediaManager()

    class Meta:
        ordering = ('-date_ts',)
        get_latest_by = ('-date_ts',)

    def __str__(self):
        return f"{self.chat} @ {arrow.get(self.date_ts)}"
