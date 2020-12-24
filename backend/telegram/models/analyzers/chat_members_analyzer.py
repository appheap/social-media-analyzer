from django.db import models

from ..base import BaseModel


class ChatMembersAnalyzerMetaData(BaseModel):
    id = models.BigIntegerField(primary_key=True)  # `chat__chat_id`

    enabled = models.BooleanField(default=False)
    first_analyzed_ts = models.BigIntegerField(null=True, blank=True)
    last_analyzed_ts = models.BigIntegerField(null=True, blank=True)
    disable_ts = models.BigIntegerField(null=True, blank=True)
    disable_reason = models.TextField(max_length=256, null=True, blank=True)

    ######################################
    # current active telegram channel
    telegram_channel = models.OneToOneField(  # fixme: what's the usage?
        'telegram.TelegramChannel',
        on_delete=models.SET_NULL,
        related_name='chat_member_analyzer_metadata',
        null=True, blank=True,
    )

    ######################################
    # `chat` : chat this analyzer metadata belongs to

    class Meta:
        verbose_name_plural = 'Analyzers (chat members)'

    def __str__(self):
        return f"{self.id} : {self.enabled}"
