import arrow
from django.db.models import QuerySet

from core.globals import logger
from pyrogram import types
from tasks.task_scaffold import TaskScaffold
from ..base_response import BaseResponse


class IterateChatHistoryTask(TaskScaffold):

    def iterate_chat_history_task(self, *args, **kwargs) -> BaseResponse:
        db_chats: QuerySet = self.db.telegram.get_chats_filter_by_analyzer(
            message_view_analyzer=True,
        )
        if db_chats.exists():
            for db_chat in db_chats:
                db_telegram_accounts = self.get_telegram_accounts(db_chat)
                if db_telegram_accounts is None or not len(db_telegram_accounts):
                    # return BaseResponse().done(message='No Telegram Account is available now.')
                    continue

                db_telegram_account = db_telegram_accounts[0]

                client = self.get_client(session_name=db_telegram_account.session_name)
                last_raw_message: 'types.Message' = self.get_last_valid_message(client, db_chat.chat_id)
                if last_raw_message is not None:
                    now = arrow.utcnow().timestamp()
                    for raw_message in self.iter_messages(
                            client,
                            db_chat.chat_id,
                            last_raw_message.message_id,
                    ):
                        self.db.telegram.update_message_and_view(
                            db_chat=db_chat,
                            raw_message=raw_message,
                            logger_account=db_telegram_account,
                            now=now
                        )

                    self.db.telegram.update_analyzer_metadata(
                        analyzer=db_chat.message_view_analyzer,
                        timestamp=now,
                    )
        else:
            return BaseResponse().done(message='No analyzer is enabled.')

        return BaseResponse().done()
