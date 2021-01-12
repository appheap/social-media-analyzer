from django.db import models

from pyrogram import types
from .chat import Chat


class ChatUpdater:

    @staticmethod
    def update_or_create_chat_from_raw(
            *,
            model: models.Model,
            field_name: str,
            raw_chat: types.Chat
    ):
        field = getattr(model, field_name, None)
        if field and not isinstance(field, Chat):
            return

        if field:
            if raw_chat:
                field.update_fields_from_raw(raw_chat=raw_chat)
            else:
                setattr(model, field_name, None)
                model.save()
        else:
            setattr(
                model,
                field_name,
                Chat.chats.update_or_create_from_raw(
                    raw_chat=raw_chat
                )
            )
            model.save()
