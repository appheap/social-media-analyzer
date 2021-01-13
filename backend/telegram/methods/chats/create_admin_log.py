from typing import Optional

from django.db import transaction

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models


class CreateAdminLog(Scaffold):

    def create_admin_log(
            self,
            *,
            raw_admin_log: 'types.ChannelAdminLogEvent',
            db_chat: 'tg_models.Chat',
            logged_by: 'tg_models.TelegramAccount',

    ) -> Optional['tg_models.AdminLogEvent']:
        if raw_admin_log is None or db_chat is None or logged_by is None:
            return None

        if not self.admin_log_exists(
                event_id=raw_admin_log.event_id,
                chat_id=db_chat.chat_id,
        ):
            db_user = self.get_updated_user(
                raw_user=raw_admin_log.user
            )
            if not db_user:
                return None

            return self.tg_models.AdminLogEvent.objects.update_or_create_from_raw(
                raw_admin_log=raw_admin_log,
                db_user=db_user,
                db_chat=db_chat,
                logged_by=logged_by,
            )

        return None
