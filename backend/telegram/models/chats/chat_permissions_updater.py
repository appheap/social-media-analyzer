from django.db import models

from pyrogram import types
from .chat_permissions import ChatPermissions


class ChatPermissionsUpdater:

    @staticmethod
    def update_or_create_chat_permissions_from_raw_obj(
            *,
            model: models.Model,
            field_name: str,
            raw_chat_permissions: types.ChatPermissions
    ):
        if not raw_chat_permissions:
            return

        field = getattr(model, field_name, None)
        if field and not isinstance(field, ChatPermissions):
            return

        if field:
            if raw_chat_permissions:
                field.update_fields_from_raw(raw_chat_permissions=raw_chat_permissions)
            else:
                field.delete()
                model.save()
        else:
            if raw_chat_permissions:
                setattr(
                    model,
                    field_name,
                    ChatPermissions.objects.create_chat_permissions_from_raw(
                        raw_chat_permissions=raw_chat_permissions
                    )
                )
                model.save()
