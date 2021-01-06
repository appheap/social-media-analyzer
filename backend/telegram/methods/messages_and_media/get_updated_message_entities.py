from django.db import transaction

from db.scaffold import Scaffold
from typing import List
from telegram import models as tg_models
from pyrogram import types


class GetUpdatedMessageEntities(Scaffold):

    def get_updated_message_entities(
            self,
            *,
            db_message: 'tg_models.Message',
            raw_message: 'types.Message'
    ) -> List['tg_models.Entity']:

        if db_message is None or raw_message is None:
            return None

        if raw_message.type == 'message' and raw_message.content.entities:
            entities = raw_message.content.entities
            db_entities = []
            with transaction.atomic():
                for raw_entity in entities:
                    db_entities.append(
                        self.tg_models.Entity.objects.update_or_create_from_raw(
                            raw_entity=raw_entity,
                            db_message=db_message,
                        )
                    )
            db_entities = list(filter(lambda obj: obj is not None, db_entities))
            return db_entities

        return None
