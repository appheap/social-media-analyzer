from django.db import models

from .admin_log_analyzer import AdminLogAnalyzerMetaData


class AdminLogAnalyzerMetaDataUpdater:

    @staticmethod
    def update_or_create_admin_log_analyzer(
            model: models.Model,
            field_name: str,
            db_telegram_channel,
            chat_id: int,
            enabled: bool,
            **kwargs,
    ):
        if not db_telegram_channel or chat_id is None:
            return

        field = getattr(model, field_name, None)
        if field and not isinstance(field, AdminLogAnalyzerMetaData):
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
            if db_telegram_channel:
                setattr(
                    model,
                    field_name,
                    AdminLogAnalyzerMetaData.objects.update_or_create_analyzer(
                        db_telegram_channel=db_telegram_channel,
                        chat_id=chat_id,
                        enabled=enabled
                    )
                )
                model.save(model)
