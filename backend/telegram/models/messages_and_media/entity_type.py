from typing import Optional

from django.db import models, DatabaseError

from pyrogram import types
from telegram import models as tg_models
from core.globals import logger
from .entity_types import EntityTypes
from ..base import BaseModel


class EntityTypeQuerySet(models.QuerySet):
    def filter_by_id(self, *, id: str) -> "EntityTypeQuerySet":
        return self.filter(id=id)

    def get_by_id(self, *, id: str) -> Optional["EntityType"]:
        try:
            return self.get(id=id)
        except EntityType.DoesNotExist as e:
            pass
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def update_or_create_entity(self, *, defaults: dict, **kwargs) -> Optional["EntityType"]:
        try:
            return self.update_or_create(
                defaults=defaults,
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class EntityTypeManager(models.Manager):
    def get_queryset(self) -> EntityTypeQuerySet:
        return EntityTypeQuerySet(self.model, using=self._db)

    def update_or_create_from_raw(
            self,
            *,
            raw_entity: types.MessageEntity,
            db_message: "tg_models.Message",
    ) -> Optional["EntityType"]:

        if raw_entity is None or db_message is None:
            return None

        parsed_entity = self._parse(
            raw_entity=raw_entity,
        )
        if parsed_entity:
            db_entity = self.get_queryset().update_or_create_entity(
                id=f'{db_message.id}:{raw_entity.type}',
                defaults={
                    'message': db_message,
                    **parsed_entity,
                },
            )
            return db_entity

        return None

    @staticmethod
    def _parse(*, raw_entity: types.MessageEntity) -> dict:
        if raw_entity is None:
            return {}
        return {
            'type': EntityTypes.get_type(raw_entity.type),
        }


class EntityType(BaseModel):
    """

    """
    id = models.CharField(max_length=256, primary_key=True)  # `message__id:type`

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

    objects = EntityTypeManager()

    class Meta:
        verbose_name_plural = 'Entity Types'

    def __str__(self):
        return f"{self.type} in {self.message}"
