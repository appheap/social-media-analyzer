from django.db import models
from ..base import BaseModel
from .entity_types import EntityTypes
from .entity_types import EntitySourceTypes


class Entity(BaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat__chat_id:message__id:offset`

    type = models.CharField(
        EntityTypes.choices,
        max_length=20,
        null=False,
    )
    source = models.CharField(
        EntitySourceTypes.choices,
        max_length=20,
        null=False,
    )
    offset = models.IntegerField()
    length = models.IntegerField()

    # entities, both from `text` and `caption`
    message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        null=False,
        related_name='entities',
    )

    # For `text_mention` only, the mentioned user.
    user = models.ForeignKey(
        'telegram.User',
        related_name='mentioned_entities',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'Entities'
        ordering = ('message',)

    def __str__(self):
        return f"{self.type} of type {self.source} in {self.message}"
