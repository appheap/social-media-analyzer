from django.db import models
import arrow

from ..base import BaseModel


class ChatMemberCount(BaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:logged_by_id:date`

    count = models.BigIntegerField()
    date = models.BigIntegerField()

    # Chat this object belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=False,
        related_name='member_count_history',
    )

    ############################
    # TODO add more fields if you can
    # Telegram account who logged this member count
    logged_by = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='member_count_history',
    )

    class Meta:
        ordering = ('-date',)
        get_latest_by = ('-date',)

    def __str__(self):
        return f"{self.chat} : {self.count} @ {arrow.get(self.date)}"
