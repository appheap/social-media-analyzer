from typing import Optional, List
from telegram import models as tg_models

from db.scaffold import Scaffold
from pyrogram import types


class GetUpdatedChatSharedMedia(Scaffold):

    def get_updated_chat_shared_media(
            self,
            *,
            db_chat: 'tg_models.Chat',
            date_ts: int,
            raw_search_counters: List['types.SearchCounter'],
            logger_account: 'tg_models.TelegramAccount',

    ) -> Optional['tg_models.ChatMemberCount']:
        if db_chat is None or date_ts is None or raw_search_counters is None or logger_account is None:
            return None

        return self.tg_models.ChatSharedMedia.objects.update_or_create_shared_media_from_raw(
            raw_search_counters=raw_search_counters,
            db_chat=db_chat,
            date_ts=date_ts,
            logger_account=logger_account,
        )
