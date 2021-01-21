from typing import Optional

from django.db import models, DatabaseError
from ..base import BaseModel
import arrow
from ..chats import ChatUpdater
from telegram import models as tg_models
from pyrogram import types
from core.globals import logger


class MessageViewQuerySet(models.QuerySet):
    def update_or_create_view(self, *, defaults: dict, **kwargs) -> Optional["MessageView"]:
        try:
            self.update_or_create(
                defaults=defaults,
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class MessageViewManager(models.Manager):
    def get_queryset(self) -> MessageViewQuerySet:
        return MessageViewQuerySet(self.model, using=self._db)

    def update_or_create_view_from_raw(
            self,
            *,
            raw_message_view: types.MessageViews,
            db_chat: "tg_models.Chat",
            db_message: "tg_models.Message",
            logger_account: "tg_models.TelegramAccount",
            date_ts: int,
            db_discussion_chat: "tg_models.Chat" = None,
    ) -> Optional["MessageView"]:

        if raw_message_view is None or db_chat is None or logger_account is None:
            return None

        parsed_view = self._parse(raw_message_view=raw_message_view)
        if parsed_view:
            db_view = self.get_queryset().update_or_create_view(
                id=f'{db_message.id}:{date_ts}',
                defaults={
                    **parsed_view,
                    'date_ts': date_ts,
                    'chat': db_chat,
                    'message': db_message,
                    'message_id_orig': db_message.message_id,
                    'logged_by': logger_account,
                    'discussion_chat': db_discussion_chat
                }
            )
            return db_view
        return None

    @staticmethod
    def _parse(*, raw_message_view: types.MessageViews):
        if raw_message_view is None:
            return {}

        r = {
            'views': raw_message_view.views,
            'forwards': raw_message_view.forwards,
        }
        if raw_message_view.replies:
            r.update(
                {
                    'replies': raw_message_view.replies.replies,
                }
            )
        return r


class MessageView(BaseModel, ChatUpdater):
    id = models.CharField(max_length=256, primary_key=True)  # `message__id:date`

    date_ts = models.BigIntegerField()

    views = models.BigIntegerField(null=True, blank=True)
    forwards = models.BigIntegerField(null=True, blank=True)
    # info from replies
    replies = models.BigIntegerField(null=True, blank=True)
    # `recent_repliers`
    discussion_chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        related_name='discussion_message_views',
        null=True,
        blank=True,
    )

    message_id_orig = models.BigIntegerField()
    # message this view belongs to (left null so message can be fetched later.)
    message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='message_views',
    )

    # Telegram account who logged this view
    logged_by = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='messages_views',
    )
    # Chat this view belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='message_views',
    )

    objects = MessageViewManager()

    ###################################################
    # `recent_user_repliers` : last few comment posters for a specific thread
    # `recent_chat_repliers` : last few comment posters for a specific thread

    class Meta:
        ordering = ['-date_ts', 'message', ]
        get_latest_by = ['-date_ts', 'message', ]

    def __str__(self):
        return f"{self.views} @ ({arrow.get(self.date_ts, tzinfo='utc').format('YYYY-MM-DD HH:mm:ss')}) of {self.message}"
