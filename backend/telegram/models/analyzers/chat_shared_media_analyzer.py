from django.db import models

from ..base import BaseModel


class SharedMediaAnalyzerMetaData(BaseModel):
    id = models.BigIntegerField(primary_key=True)  # `chat__chat_id`

    enabled = models.BooleanField(default=False)
    first_analyzed_ts = models.BigIntegerField(null=True, blank=True)
    last_analyzed_ts = models.BigIntegerField(null=True, blank=True)
    disable_ts = models.BigIntegerField(null=True, blank=True)
    disable_reason = models.TextField(max_length=256, null=True, blank=True)

    ######################################

    ######################################
    # `chat` : chat this analyzer metadata belongs to

    class Meta:
        verbose_name_plural = 'Analyzers (chat shared medias)'

    def __str__(self):
        return str(f" {self.id} : {self.enabled}")
