from django.db import models

from .chat_member_count_analyzer import ChatMemberCountAnalyzerMetaData


class ChatMemberCountAnalyzerMetaDataUpdater:

    @staticmethod
    def update_or_create_chat_member_count_analyzer(
            model: models.Model,
            field_name: str,
            chat_id: int,
            enabled: bool,
            create: bool = True,
            **kwargs,
    ):
        if chat_id is None:
            return

        field = getattr(model, field_name, None)
        if field and not isinstance(field, ChatMemberCountAnalyzerMetaData):
            return

        if field:
            if len(kwargs) or enabled is not None:
                field.update_fields(
                    **{
                        'enabled': enabled,
                        **kwargs
                    }
                )
            else:
                field.delete()
                model.save()
        else:
            if create and enabled is not None:
                setattr(
                    model,
                    field_name,
                    ChatMemberCountAnalyzerMetaData.objects.update_or_create_analyzer(
                        chat_id=chat_id,
                        enabled=enabled
                    )
                )
                model.save()
