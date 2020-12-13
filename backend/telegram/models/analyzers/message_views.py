from django.db import models
from ..base import BaseModel
import arrow


class MessageView(BaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:message_id:date`

    date = models.BigIntegerField()

    views = models.BigIntegerField()
    forwards = models.BigIntegerField()
    # info from replies
    replies = models.BigIntegerField()
    # `recent_repliers`
    discussion_chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        related_name='discussion_message_views',
        null=True,
        blank=True,
    )

    message_id_orig = models.BigIntegerField()
    # message this view belongs to
    message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        null=False,
        related_name='message_views',
    )

    # TODO add more fields if necessary
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

    ###################################################
    # `recent_repliers` : last few comment posters for a specific thread

    class Meta:
        ordering = ['-date', 'message', ]
        get_latest_by = ['-date', 'message', ]

    def __str__(self):
        return f"{self.views} @ ({arrow.get(self.date, tzinfo='utc').format('YYYY-MM-DD HH:mm:ss')}) of {self.message}"
