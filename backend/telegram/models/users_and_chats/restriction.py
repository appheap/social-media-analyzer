from django.db import models
from ..base import BaseModel


class Restriction(BaseModel):
    """
    The reason why this chat/bot might be unavailable to some users. This field is available only in case is_restricted of `chat` or `bot` is True.
    """

    id = models.CharField(max_length=256, primary_key=True, )  # `chat|user:_id`

    platform = models.CharField(max_length=256, null=True, blank=True)
    reason = models.CharField(max_length=256, null=True, blank=True)
    text = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        unique_together = [('id', 'platform', 'reason', 'text'), ]

    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='restrictions',
    )

    user = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='restrictions',
    )
    ##############################################
    is_deleted = models.BooleanField(default=False, null=False)
    deleted_at = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.reason
