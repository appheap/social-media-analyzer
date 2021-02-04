from typing import Optional

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models
from users import models as site_models


class CreateTelegramChannel(Scaffold):

    def create_telegram_channel(
            self,
            raw_chat: types.Chat,
            db_account: 'tg_models.TelegramAccount',
            db_site_user: 'site_models.SiteUser',
    ) -> Optional['tg_models.TelegramChannel']:
        if raw_chat is None or db_account is None or db_site_user is None:
            return None

        db_chat_creator = None
        if raw_chat.is_creator:
            db_chat_creator = db_account.telegram_user

        db_chat = self.tg_models.Chat.chats.update_or_create_from_raw(
            raw_chat=raw_chat,
            creator=db_chat_creator
        )
        return self.tg_models.TelegramChannel.channels.create_channel_from_raw(
            raw_chat=raw_chat,
            db_site_user=db_site_user,
            db_account=db_account,
            db_chat=db_chat,
        )
