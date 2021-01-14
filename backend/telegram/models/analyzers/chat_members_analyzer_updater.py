from django.db import models

from .chat_members_analyzer import ChatMembersAnalyzerMetaData


class ChatMembersAnalyzerMetaDataUpdater:

    @staticmethod
    def update_or_create_chat_members_analyzer(
            model: models.Model,
            field_name: str,
            chat_id: int,
            enabled: bool,
            create: bool = True,
            delete: bool = True,
            **kwargs,
    ):
        if chat_id is None:
            return

        field = getattr(model, field_name, None)
        if field and not isinstance(field, ChatMembersAnalyzerMetaData):
            return

        if field:
            if delete:
                field.delete()
                model.save()
            else:
                field.update_fields(
                    **{
                        'enabled': enabled,
                        **kwargs
                    }
                )
        else:
            if create and not delete:
                setattr(
                    model,
                    field_name,
                    ChatMembersAnalyzerMetaData.objects.update_or_create_analyzer(
                        chat_id=chat_id,
                        enabled=enabled
                    )
                )
                model.save()
