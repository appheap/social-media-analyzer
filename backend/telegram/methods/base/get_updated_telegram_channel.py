from typing import Optional

from django.db import transaction

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models
from users import models as site_models


class GetUpdatedTelegramChannel(Scaffold):

    def get_updated_telegram_channel(
            self,
            raw_chat: types.Chat,
            db_account: 'tg_models.TelegramAccount',
            db_site_user: 'site_models.SiteUser' = None,
            create: bool = True,
    ) -> Optional['tg_models.TelegramChannel']:
        if raw_chat is None or db_account is None:
            return None

        with transaction.atomic():
            if raw_chat.is_creator:
                db_chat_creator = db_account.telegram_user

            db_chat = self.tg_models.Chat.chats.update_or_create_from_raw(
                raw_chat=raw_chat,
                creator=db_chat_creator
            )

            db_telegram_channel = self.tg_models.TelegramChannel.channels.update_or_create_from_raw(
                raw_chat=raw_chat,
                db_site_user=db_site_user,
                db_account=db_account,
                db_chat=db_chat,
                create=create,
            )

            return db_telegram_channel
