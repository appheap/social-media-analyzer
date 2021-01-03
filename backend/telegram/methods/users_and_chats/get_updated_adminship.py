from typing import Optional

from django.db import transaction

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models


class GetUpdatedAdminShip(Scaffold):
    def get_updated_adminship(
            self,
            *,
            db_account: 'tg_models.TelegramAccount',
            db_chat: 'tg_models.Chat',

            raw_chat: types.Chat,
    ) -> Optional['tg_models.AdminShip']:
        if db_account is None or db_chat is None or raw_chat is None:
            return None

        with transaction.atomic():
            db_adminship = self.tg_models.AdminShip.objects.update_or_create_from_raw(
                db_account=db_account,
                db_chat=db_chat,
                raw_chat=raw_chat,
            )
            db_adminship.update_or_create_chat_admin_rights_from_raw(
                model=db_adminship,
                field_name='admin_rights',
                raw_chat_admin_rights=raw_chat.admin_rights
            )
            db_adminship.update_or_create_chat_permissions_from_raw(
                model=db_adminship,
                field_name='banned_rights',
                raw_chat_permissions=raw_chat.chat_permissions
            )

            return db_adminship
