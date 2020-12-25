from django.db import models

from ..base import BaseModel


class Membership(BaseModel):
    # id = models.CharField(
    #     max_length=256,
    #     null=False,
    #     primary_key=True,
    # )  # `chat_id:user_id`

    user = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        related_name='+',
    )

    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        related_name='+',
    )

    class Meta:
        # order_with_respect_to = 'chat'
        unique_together = [
            ('chat', 'user'),
        ]
        ordering = ['chat', 'user']

    current_status = models.OneToOneField(
        'telegram.ChatMember',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='+'
    )
    previous_status = models.OneToOneField(
        'telegram.ChatMember',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='+'
    )

    status_change_date = models.BigIntegerField(null=True, blank=True)

    ######################################
    # `participant_history` : participants related to this membership

    def __str__(self):
        return f"{self.user} @ {self.chat} : {self.current_status.type if self.current_status else ''}"
