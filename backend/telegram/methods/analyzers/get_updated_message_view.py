from typing import Optional

from django.db import transaction

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models


class GetUpdatedMessageView(Scaffold):
    def get_updated_message_view(
            self,
            *,
            raw_message_view: types.MessageViews,
            db_chat: "tg_models.Chat",
            db_message: "tg_models.Message",
            logger_account: "tg_models.TelegramAccount",
            date_ts: int,

            create_recent_repliers: bool = True,
    ) -> Optional['tg_models.MessageView']:
        if raw_message_view is None or db_chat is None or db_message is None or logger_account is None or date_ts is None:
            return None

        with transaction.atomic():
            db_discussion_chat = None
            if raw_message_view.replies is not None and raw_message_view.replies.channel_id is not None:
                db_discussion_chat = self.get_chat_by_id(chat_id=raw_message_view.replies.channel_id)

            db_message_view = self.tg_models.MessageView.objects.update_or_create_view_from_raw(
                raw_message_view=raw_message_view,
                db_chat=db_chat,
                db_message=db_message,
                logger_account=logger_account,
                date_ts=date_ts,
                db_discussion_chat=db_discussion_chat,
            )

            if create_recent_repliers and db_message_view and raw_message_view.replies:
                if raw_message_view.replies.recent_repliers:
                    raw_recent_replies = raw_message_view.replies.recent_repliers
                    for raw_replier in raw_recent_replies:
                        if isinstance(raw_replier, types.Chat):
                            self.get_updated_chat(
                                raw_chat=raw_replier,
                                db_telegram_account=logger_account,

                                db_message_view=db_message_view,
                            )
                        elif isinstance(raw_replier, types.User):
                            self.get_updated_user(
                                raw_user=raw_replier,

                                db_message_view=db_message_view,
                            )

            return db_message_view
