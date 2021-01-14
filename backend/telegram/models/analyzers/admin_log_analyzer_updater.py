from django.db import models

from .admin_log_analyzer import AdminLogAnalyzerMetaData


class AdminLogAnalyzerMetaDataUpdater:

    @staticmethod
    def update_or_create_admin_log_analyzer(
            model: models.Model,
            field_name: str,
            chat_id: int,
            enabled: bool,
            create: bool = True,
            delete: bool = False,
            **kwargs,
    ):
        if chat_id is None:
            return

        field = getattr(model, field_name, None)
        if field and not isinstance(field, AdminLogAnalyzerMetaData):
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
                    AdminLogAnalyzerMetaData.objects.update_or_create_analyzer(
                        chat_id=chat_id,
                        enabled=enabled
                    )
                )
                model.save()
