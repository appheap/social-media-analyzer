import arrow
from django.db.models import QuerySet

import pyrogram
from pyrogram import errors as tg_errors
from ..base_response import BaseResponse
from tasks.task_scaffold import TaskScaffold
from core.globals import logger


class LogAdminLogsTask(TaskScaffold):

    def log_admin_logs_task(self, *args, **kwargs) -> BaseResponse:
        db_chats: QuerySet = self.db.telegram.get_chats_filter_by_analyzer(
            admin_log_analyzer=True,
        )

        if db_chats.exists():
            for db_chat in db_chats:
                now = arrow.utcnow().timestamp
                db_telegram_accounts = self.get_telegram_accounts(db_chat, with_admin_permissions=True)
                if db_telegram_accounts is None or not len(db_telegram_accounts):
                    # return BaseResponse().done(message='No Telegram Account is available now.')
                    continue

                client = self.get_client(session_name=db_telegram_accounts[0].session_name)
                response = self._analyze_chat_admin_logs(
                    db_chat=db_chat,
                    db_tg_admin_account=db_telegram_accounts[0],
                    client=client,
                )
                if response.success:
                    self.db.telegram.update_analyzer_metadata(
                        analyzer=db_chat.admin_log_analyzer,
                        timestamp=now
                    )
        else:
            return BaseResponse().done(message='No analyzer is enabled.')

        return BaseResponse().done()

    def _analyze_chat_admin_logs(
            self,
            *,
            db_chat: 'tg_models.Chat',
            db_tg_admin_account: 'tg_models.TelegramAccount',
            client: 'pyrogram.Client',
    ) -> BaseResponse:
        try:
            raw_admin_logs = client.get_admin_log(
                db_chat.chat_id,
            )
        except tg_errors.ChatAdminRequired or tg_errors.ChatWriteForbidden:
            self.db.telegram.update_chat_analyzers_status(
                db_chat=db_chat,
                enabled=False,
                only_admin_based_analyzers=True,
            )
        except Exception as e:
            logger.exception(e)
        else:
            for raw_admin_log in raw_admin_logs:
                self.db.telegram.create_admin_log(
                    raw_admin_log=raw_admin_log,
                    db_chat=db_chat,
                    logged_by=db_tg_admin_account,
                )

        return BaseResponse().done()
