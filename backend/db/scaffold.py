from pyrogram import types
from typing import Optional, List
from telegram import models as tg_models
from users import models as site_models


class Scaffold:

    def __init__(self):
        self.tg_models = tg_models
        self.site_models = site_models

    def get_updated_user(
            self,
            *,
            raw_user: 'types.User',

            db_message_view: 'tg_models.MessageView' = None
    ) -> Optional['tg_models.User']:
        pass

    def get_updated_chat(
            self,
            *,
            raw_chat: types.Chat,
            db_telegram_account: 'tg_models.TelegramAccount',

            db_message_view: 'tg_models.MessageView' = None
    ) -> Optional["tg_models.Chat"]:
        pass

    def get_chat_by_id(
            self,
            *,
            chat_id: int
    ) -> Optional['tg_models.Chat']:
        pass

    def get_telegram_channel_by_id(
            self,
            channel_id: int,
    ) -> Optional['tg_models.TelegramChannel']:
        pass

    def get_updated_dialog(
            self,
            *,
            raw_chat: "types.Chat",
            db_account: "tg_models.TelegramAccount",
            is_member: bool,
            left_date_ts: int = None,
            update_chat: bool = True,
    ) -> Optional["tg_models.Dialog"]:
        pass

    def get_membership_by_user_id(
            self,
            *,
            user_id: int,
            db_chat: 'tg_models.Chat'
    ) -> Optional['tg_models.Membership']:
        pass

    def get_updated_membership(
            self,
            *,
            db_chat: 'tg_models.Chat',
            new_status: 'tg_models.ChatMember',
            event_date_ts: int,
    ) -> Optional['tg_models.Membership']:
        pass

    def get_updated_adminship(
            self,
            *,
            db_account: 'tg_models.TelegramAccount',
            db_chat: 'tg_models.Chat',

            raw_chat: types.Chat,
    ) -> Optional['tg_models.AdminShip']:
        pass

    def admin_log_exists(
            self,
            *,
            event_id: int,
            chat_id: int,
    ) -> bool:
        pass

    def get_updated_message_entities(
            self,
            *,
            db_message: 'tg_models.Message',
            raw_message: 'types.Message'
    ) -> List['tg_models.Entity']:
        pass

    def get_updated_message_entity_types(
            self,
            *,
            db_message: 'tg_models.Message',
            raw_message: 'types.Message'
    ) -> List['tg_models.EntityType']:
        pass
