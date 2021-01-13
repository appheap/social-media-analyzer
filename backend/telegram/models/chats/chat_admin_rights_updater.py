from django.db import models

from pyrogram import types
from .chat_admin_rights import ChatAdminRights


class ChatAdminRightsUpdater:

    @staticmethod
    def update_or_create_chat_admin_rights_from_raw(
            *,
            model: models.Model,
            field_name: str,
            raw_chat_admin_rights: types.ChatAdminRights
    ):
        if not raw_chat_admin_rights:
            return

        field = getattr(model, field_name, None)
        if field and not isinstance(field, ChatAdminRights):
            return

        if field:
            if raw_chat_admin_rights:
                field.update_fields_from_raw(raw_chat_admin_rights=raw_chat_admin_rights)
            else:
                field.delete()
                model.save()
        else:
            if raw_chat_admin_rights:
                setattr(
                    model,
                    field_name,
                    ChatAdminRights.objects.create_from_raw(
                        raw_chat_admin_rights=raw_chat_admin_rights
                    )
                )
                model.save()
