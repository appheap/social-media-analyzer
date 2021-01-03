from typing import Optional

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models


class CreateChat(Scaffold):
    def create_chat(
            self,
            *,
            raw_chat: types.Chat,
            db_telegram_account: 'tg_models.TelegramAccount',
    ) -> Optional["tg_models.Chat"]:

        if raw_chat is None or db_telegram_account is None:
            return None

        _user = db_telegram_account.telegram_user
        if raw_chat.type in ('channel', 'supergroup',):
            db_creator = _user if raw_chat.channel.is_creator else None
        elif raw_chat.type == 'group':
            db_creator = _user if raw_chat.group.is_creator else None
        else:
            db_creator = _user if raw_chat.user.is_self else None

        return self.tg_models.Chat.chats.update_or_create_from_raw(
            raw_chat=raw_chat,
            creator=db_creator
        )
