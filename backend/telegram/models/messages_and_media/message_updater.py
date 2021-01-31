from pyrogram import types
from django.db import models
from .message import Message
from telegram import models as tg_models


class MessageUpdater:

    @staticmethod
    def update_or_create_message_from_raw(
            *,
            model: models.Model,
            field_name: str,
            raw_message: types.Message,
            chat_id: int,
            logger_account: "tg_models.TelegramAccount" = None
    ):
        field = getattr(model, field_name, None)
        if field and not isinstance(field, Message):
            return

        if field:
            if raw_message:
                field.update_fields_from_raw(
                    raw_message=raw_message,
                    chat_id=chat_id,
                    logger_account=logger_account
                )
            else:
                setattr(model, field_name, None)
                model.save()
        else:
            if raw_message:
                setattr(
                    model,
                    field_name,
                    Message.objects.update_or_create_from_raw(
                        raw_user=raw_message,
                        chat_id=chat_id,
                        logger_account=logger_account
                    )
                )
                model.save()

    @staticmethod
    def update_or_create_message_from_db_message(
            *,
            model: models.Model,
            field_name: str,
            db_message: 'tg_models.Message',
    ):
        field = getattr(model, field_name, None)
        if field and not isinstance(field, Message):
            return

        if field:
            if db_message:
                setattr(model, field_name, db_message)
                model.save()
            else:
                setattr(model, field_name, None)
                model.save()
        else:
            if db_message:
                setattr(model, field_name, db_message)
                model.save()
