from typing import Optional, Tuple

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
    ) -> Tuple[Optional['tg_models.TelegramChannel'], 'bool']:
        if raw_chat is None or db_account is None:
            return None, False

        if db_site_user is None:
            db_site_user = self.get_default_site_user()

        db_telegram_channel = self.tg_models.TelegramChannel.channels.get_telegram_channel_by_site_user_and_channel_id(
            db_site_user=db_site_user,
            channel_id=raw_chat.id,
        )
        if db_telegram_channel is None:
            return None, False

        _updated = db_telegram_channel.update_fields_from_raw(
            raw_chat=raw_chat
        )

        return db_telegram_channel, _updated
