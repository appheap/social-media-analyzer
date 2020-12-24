from typing import Optional

from django.db import models, DatabaseError, transaction

from .message import ChatMediaTypes
from ..users import UserUpdater
from ..base import BaseModel
from .entity_types import EntityTypes
from .entity_types import EntitySourceTypes
from telegram.globals import logger
from pyrogram import types
from telegram import models as tg_models


class EntityQuerySet(models.QuerySet):
    def filter_by_id(self, *, id: str) -> "EntityQuerySet":
        return self.filter(id=id)

    def get_by_id(self, *, id: str) -> Optional["Entity"]:
        try:
            return self.get(id=id)
        except Entity.DoesNotExist as e:
            pass
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def update_or_create_entity(self, **kwargs) -> Optional["Entity"]:
        try:
            self.update_or_create(
                **kwargs
            )
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class EntityManager(models.Manager):
    def get_queryset(self) -> EntityQuerySet:
        return EntityQuerySet(self.model, using=self._db)

    def update_or_create_from_raw(
            self,
            *,
            raw_entity: types.MessageEntity,
            db_message: "tg_models.Message",
    ) -> Optional["Entity"]:

        if raw_entity is None or db_message is None:
            return None

        parsed_entity = self._parse(
            raw_entity=raw_entity,
            message__has_media=bool(db_message.media_type != ChatMediaTypes.undefined)
        )
        if parsed_entity:
            with transaction.atomic():
                db_entity = self.get_queryset().update_or_create_entity(
                    **{
                        'id': f"{db_message.id}:{raw_entity.offset}",
                        'message': db_message,
                        **parsed_entity,
                    },
                )
                if db_entity:
                    db_entity.update_or_create_user_from_raw(
                        model=db_entity,
                        field_name='user',
                        raw_user=raw_entity.user
                    )
                    return db_entity

        return None

    @staticmethod
    def _parse(*, raw_entity: types.MessageEntity, message__has_media: bool) -> dict:
        if raw_entity is None:
            return {}
        return {
            'type': EntityTypes.get_type(raw_entity.type),
            'source': EntitySourceTypes.caption if message__has_media else EntitySourceTypes.text,
            'offset': raw_entity.offset,
            'length': raw_entity.length,
        }


class Entity(BaseModel, UserUpdater):
    id = models.CharField(max_length=256, primary_key=True)  # `message__id:offset`

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

    objects = EntityManager()

    class Meta:
        verbose_name_plural = 'Entities'
        ordering = ('message',)

    def __str__(self):
        return f"{self.type} of type {self.source} in {self.message}"
