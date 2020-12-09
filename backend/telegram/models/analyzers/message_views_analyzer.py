from django.db import models

from ..base import BaseModel


class ChatMessageViewsAnalyzerMetaData(BaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:created_at`

    enabled = models.BooleanField()
    first_analyzed_at = models.BigIntegerField(null=True, blank=True)
    last_analyzed_at = models.BigIntegerField(null=True, blank=True)
    disabled_at = models.BigIntegerField(null=True, blank=True)
    disable_reason = models.CharField(max_length=256, null=True, blank=True, )

    ######################################
    # `chat` : chat this analyzer metadata belongs to

    class Meta:
        verbose_name_plural = 'Analyzers (message view)'

    def __str__(self):
        return f"{self.id} : {self.enabled}"
