from django.db.models import QuerySet

from tasks.task_scaffold import TaskScaffold
from ..base_response import BaseResponse
import arrow


class LogChatSharedMediasTask(TaskScaffold):

    def log_chat_shared_medias_task(self, *args, **kwargs) -> BaseResponse:
        db_chats: QuerySet = self.db.telegram.get_chats_filter_by_analyzer(
            shared_media_analyzer=True,
        )
        if db_chats.exists():
            for db_chat in db_chats:
                now = arrow.utcnow().timestamp
                client_session_names = self.get_client_session_names()
                db_telegram_accounts = self.db.telegram.get_telegram_accounts_by_session_names(
                    db_chat=db_chat,
                    session_names=client_session_names
                )
                if db_telegram_accounts is None or not len(db_telegram_accounts):
                    # return BaseResponse().done(message='No Telegram Account is available now.')
                    continue

                db_telegram_account = db_telegram_accounts[0]

                client = self.get_client(session_name=db_telegram_account.session_name)
                raw_search_counters = client.get_search_counters(db_chat.chat_id)
                if raw_search_counters is not None:
                    self.db.telegram.get_updated_chat_shared_media(
                        db_chat=db_chat,
                        date_ts=now,
                        raw_search_counters=raw_search_counters,
                        logger_account=db_telegram_account,
                    )
                    self.db.telegram.update_analyzer_metadata(
                        analyzer=db_chat.shared_media_analyzer,
                        timestamp=now
                    )
        else:
            return BaseResponse().done(message='No analyzer is enabled.')

        return BaseResponse().done()
