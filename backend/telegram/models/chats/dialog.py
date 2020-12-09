from django.db import models
from ..base import BaseModel


class Dialog(BaseModel):
    id = models.CharField(max_length=265, primary_key=True, )  # `user_id:chat_id`
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=False,
        related_name='dialogs',
    )

    account = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        null=False,
        related_name='dialogs',
    )

    is_member = models.BooleanField(default=True, blank=True, )
    left_at = models.BigIntegerField(null=True, blank=True, )

    def __str__(self):
        return f"{self.account} : {self.chat}"
