from django.db import models

from .entity_types import EntityTypes
from ..base import BaseModel


class EntityType(BaseModel):
    """

    """
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:message_id:type`

    # Type of the entity
    type = models.CharField(
        EntityTypes.choices,
        max_length=20,
        null=False,
    )

    # Message this entity belongs to
    message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        null=False,
        related_name='entity_types',
    )

    class Meta:
        verbose_name_plural = 'Entity Types'

    def __str__(self):
        return f"{self.type} in {self.message}"
