from django.db import models

from ..base import BaseModel


class AdminLogAnalyzerMetaData(BaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat__chat_id`

    enabled = models.BooleanField()
    first_analyzed_ts = models.BigIntegerField(null=True, blank=True)
    last_analyzed_ts = models.BigIntegerField(null=True, blank=True)
    disable_date_ts = models.BigIntegerField(null=True, blank=True)
    disable_reason = models.CharField(max_length=256, null=True, blank=True, )

    ######################################

    # current active telegram channel
    telegram_channel = models.OneToOneField(
        'telegram.TelegramChannel',
        on_delete=models.CASCADE,
        related_name='admin_log_analyzer_metadata',
        null=True, blank=True,
    )

    ######################################
    # `chat` : chat this analyzer metadata belongs to

    class Meta:
        verbose_name_plural = 'Analyzers (chat admin logs)'

    def __str__(self):
        return f"{self.id} : {self.enabled}"
