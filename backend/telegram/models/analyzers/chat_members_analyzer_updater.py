from django.db import models

from .chat_members_analyzer import ChatMembersAnalyzerMetaData


class ChatMembersAnalyzerMetaDataUpdater:

    @staticmethod
    def update_or_create_chat_members_analyzer(
            model: models.Model,
            field_name: str,
            db_telegram_channel,
            chat_id: int,
            enabled: bool,
            create: bool = True,
            **kwargs,
    ):
        if not db_telegram_channel or chat_id is None:
            return

        field = getattr(model, field_name, None)
        if field and not isinstance(field, ChatMembersAnalyzerMetaData):
            return

        if field:
            if db_telegram_channel:
                field.update_fields(
                    **{
                        'enabled': enabled,
                        **kwargs
                    }
                )
            else:
                field.delete()
                model.save(model)
        else:
            if create and db_telegram_channel:
                setattr(
                    model,
                    field_name,
                    ChatMembersAnalyzerMetaData.objects.update_or_create_analyzer(
                        db_telegram_channel=db_telegram_channel,
                        chat_id=chat_id,
                        enabled=enabled
                    )
                )
                model.save(model)
