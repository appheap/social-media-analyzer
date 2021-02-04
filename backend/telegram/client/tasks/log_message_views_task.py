from django.db.models import QuerySet

from tasks.task_scaffold import TaskScaffold
from ..base_response import BaseResponse
import arrow
from pyrogram import types
from core.globals import logger
from pyrogram import errors as tg_errors


class LogMessageViewsTask(TaskScaffold):

    def log_message_views_task(self, *args, **kwargs) -> BaseResponse:
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
                    last_message_id = last_raw_message.message_id
                    now = arrow.utcnow().timestamp
                    start = int((- 10000) / 100)
                    if start < 1:
                        start = 1

                    for i in range(start, int(last_message_id / 100) + 1):
                        try:
                            raw_message_views = client.get_messages_views(
                                chat_id=db_chat.chat_id,
                                message_ids=list(range(i, i + 100)),
                            )
                        except tg_errors.ChannelPrivate as e:
                            pass
                        except tg_errors.RPCError as e:
                            logger.exception(e)
                        except Exception as e:
                            logger.exception(e)
                        else:
                            for raw_message_view in raw_message_views:
                                db_message = self.db.telegram.get_message_by_message_id(
                                    db_chat=db_chat,
                                    message_id=raw_message_view.message_id
                                )
                                db_message_view = self.db.telegram.get_updated_message_view(
                                    raw_message_view=raw_message_view,
                                    db_chat=db_chat,
                                    db_message=db_message,
                                    logger_account=db_telegram_account,
                                    date_ts=now,
                                )
                    self.db.telegram.update_analyzer_metadata(
                        analyzer=db_chat.message_view_analyzer,
                        timestamp=now,
                    )
        else:
            return BaseResponse().done(message='No analyzer is enabled.')

        return BaseResponse().done()
