from django.db.models import QuerySet

from tasks.task_scaffold import TaskScaffold
from ..base_response import BaseResponse
import arrow
from pyrogram import types
from pyrogram import errors as tg_errors
from core.globals import logger
import time


class LogChatMemberCountTask(TaskScaffold):
    def log_chat_member_count_task(self, *args, **kwargs) -> BaseResponse:
        db_chats: QuerySet = self.db.telegram.get_chats_filter_by_analyzer(
            member_count_analyzer=True,
        )
        if db_chats.exists():
            made_request = False
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
                try:
                    if made_request:
                        time.sleep(0.7)
                    # todo: a better way to get member_count?
                    raw_chat: types.Chat = client.get_chat(chat_id=db_chat.chat_id)
                except tg_errors.RPCError as e:
                    made_request = False
                except Exception as e:
                    logger.exception(e)
                    made_request = False
                else:
                    made_request = True
                    if raw_chat is not None:
                        self.db.telegram.get_updated_chat(
                            raw_chat=raw_chat,
                            db_telegram_account=db_telegram_account,

                            downloader=client.download_media,
                        )
                        self.db.telegram.get_updated_chat_member_count(
                            db_chat=db_chat,
                            raw_chat=raw_chat,
                            date_ts=now,
                            logger_account=db_telegram_account,
                        )
                        self.db.telegram.update_analyzer_metadata(
                            analyzer=db_chat.member_count_analyzer,
                            timestamp=now
                        )

        else:
            return BaseResponse().done(message='No analyzer is enabled.')

        return BaseResponse().done()
