from django.db import transaction

from db.scaffold import Scaffold
from typing import List
from telegram import models as tg_models
from pyrogram import types


class GetUpdatedMessageEntityTypes(Scaffold):

    def get_updated_message_entity_types(
            self,
            *,
            db_message: 'tg_models.Message',
            raw_message: 'types.Message'
    ) -> List['tg_models.EntityType']:

        if db_message is None or raw_message is None:
            return None

        if raw_message.type == 'message' and raw_message.content.entities:
            entity_types = set()
            entities = raw_message.content.entities
            for entity in entities:
                entity_types.add(entity.type)

            if len(entity_types):
                db_entity_types = []
                with transaction.atomic():
                    for raw_entity in entities:
                        db_entity_types.append(
                            self.tg_models.EntityType.objects.update_or_create_from_raw(
                                raw_entity=raw_entity,
                                db_message=db_message,
                            )
                        )
                db_entity_types = list(filter(lambda obj: obj is not None, db_entity_types))
                return db_entity_types

        return None
