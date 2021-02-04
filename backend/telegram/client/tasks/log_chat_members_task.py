from django.db.models import QuerySet
from pyrogram.methods.chats.get_chat_members import Filters

from tasks.task_scaffold import TaskScaffold
from ..base_response import BaseResponse
import arrow
import pyrogram
from pyrogram import types
from pyrogram import errors as tg_errors
from core.globals import logger


class LogChatMembersTask(TaskScaffold):

    def log_chat_members_task(self, *args, **kwargs) -> BaseResponse:
        db_chats: QuerySet = self.db.telegram.get_chats_filter_by_analyzer(
            members_analyzer=True,
        )
        if db_chats.exists():
            for db_chat in db_chats:
                now = arrow.utcnow().timestamp
                db_telegram_accounts = self.get_telegram_accounts(db_chat, with_admin_permissions=True)
                if db_telegram_accounts is None or not len(db_telegram_accounts):
                    # return BaseResponse().done(message='No Telegram Account is available now.')
                    continue

                db_telegram_account = db_telegram_accounts[0]

                client = self.get_client(session_name=db_telegram_account.session_name)
                try:
                    response = self._analyze_chat_members(client, db_chat.chat_id, db_telegram_account, now)
                except tg_errors.ChatAdminRequired or tg_errors.ChatWriteForbidden as e:
                    logger.error(e)
                    self.db.telegram.update_chat_analyzers_status(
                        db_chat=db_chat,
                        enabled=False,
                        only_admin_based_analyzers=True,
                    )
                except Exception as e:
                    logger.exception(e)
                else:
                    if response.success:
                        self.db.telegram.update_analyzer_metadata(
                            analyzer=db_chat.members_analyzer,
                            timestamp=now,
                        )

        else:
            return BaseResponse().done(message='No analyzer is enabled.')

        return BaseResponse().done()

    def _analyze_chat_members(
            self,
            client: 'pyrogram.Client',
            chat_id: int,
            db_telegram_account: 'tg_models.TelegramAccount',
            now: int,
            _filter=None
    ):
        raw_chat: types.Chat = client.get_chat(chat_id)
        if not raw_chat:
            return BaseResponse().fail(message='cannot get chat')

        db_chat = self.db.telegram.get_updated_chat(
            raw_chat=raw_chat,
            db_telegram_account=db_telegram_account,

            downloader=client.download_media
        )

        for raw_chat_member in client.iter_chat_members(
                db_chat.chat_id,
                filter=_filter if _filter else Filters.ALL,
                last_member_count=raw_chat.members_count,
        ):
            db_chat_member, created_membership = self.db.telegram.get_updated_chat_member(
                raw_chat_member=raw_chat_member,
                db_chat=db_chat,
                event_date_ts=now,
            )
            if not created_membership:
                db_membership = self.db.telegram.get_updated_membership(
                    db_chat=db_chat,
                    new_status=db_chat_member,
                    event_date_ts=now,
                )
        return BaseResponse().done()
