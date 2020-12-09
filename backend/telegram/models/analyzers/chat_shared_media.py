from django.db import models
import arrow

from ..base import BaseModel


class ChatSharedMedia(BaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:logged_by_id:date`

    # date of getting this query
    date = models.BigIntegerField()

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

    class Meta:
        ordering = ('-date',)
        get_latest_by = ('-date',)

    def __str__(self):
        return f"{self.chat} @ {arrow.get(self.date)}"
