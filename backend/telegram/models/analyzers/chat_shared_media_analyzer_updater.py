from django.db import models

from .chat_shared_media_analyzer import SharedMediaAnalyzerMetaData


class ChatSharedMediaAnalyzerMetaDataUpdater:

    @staticmethod
    def update_or_create_chat_members_analyzer(
            model: models.Model,
            field_name: str,
            chat_id: int,
            enabled: bool,
            **kwargs,
    ):
        if chat_id is None:
            return

        field = getattr(model, field_name, None)
        if field and not isinstance(field, SharedMediaAnalyzerMetaData):
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
                model.save(model)
        else:
            if enabled is not None:
                setattr(
                    model,
                    field_name,
                    SharedMediaAnalyzerMetaData.objects.update_or_create_analyzer(
                        chat_id=chat_id,
                        enabled=enabled
                    )
                )
                model.save(model)
