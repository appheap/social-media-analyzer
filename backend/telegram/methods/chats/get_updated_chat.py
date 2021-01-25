from typing import Optional, Callable

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models


class GetUpdatedChat(Scaffold):
    def get_updated_chat(
            self,
            *,
            raw_chat: types.Chat,
            db_telegram_account: 'tg_models.TelegramAccount',

            db_message_view: 'tg_models.MessageView' = None,
            downloader: Callable = None,
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

        db_chat = self.tg_models.Chat.chats.update_or_create_from_raw(
            raw_chat=raw_chat,
            creator=db_creator,

            db_message_view=db_message_view,
        )
        self.get_updated_adminship(
            db_chat=db_chat,
            raw_chat=raw_chat,
            db_account=db_telegram_account,
        )

        if raw_chat.chat_photo and downloader:
            if not self.profile_photo_exists(
                    db_chat=db_chat,
                    upload_date=raw_chat.chat_photo.date
            ):
                file_path = downloader(
                    file_name='/tmp/',
                    message=raw_chat.chat_photo.file_id
                )
                self.get_updated_profile_photo(
                    db_chat=db_chat,
                    upload_date=raw_chat.chat_photo.date,
                    file_path=file_path,
                    width=raw_chat.chat_photo.width,
                    height=raw_chat.chat_photo.height,
                    file_size=raw_chat.chat_photo.file_size,
                )

        return db_chat
