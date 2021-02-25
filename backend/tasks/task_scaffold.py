import time
from typing import List, Optional, Generator, Dict

import pyrogram
from core.globals import logger
from db.database_manager import DataBaseManager
from pyrogram import types
import kombu
from telegram.globals import *
from tasks.client_proxy import ClientProxy


class TaskScaffold:

    def __init__(self, task_queues: Dict['str', 'kombu.Queue']):
        self.db = DataBaseManager()
        self.task_queues = task_queues

    def get_client(self, session_name: str) -> Optional['ClientProxy']:
        for client_session_name, task_queue in self.task_queues.items():
            if client_session_name == session_name:
                return ClientProxy(task_queue)

        return None

    def get_client_session_names(self) -> List['str']:
        _lst = []
        for client_session_name, task_queue in self.task_queues.items():
            _lst.append(client_session_name)

        return _lst

    def get_last_valid_message(
            self,
            client: 'ClientProxy',
            chat_id: int,
            limit: int = 20,
            is_first=True
    ) -> Optional['types.Message']:
        if client is None or chat_id is None:
            return None

        messages: List['types.Message'] = client('get_history', chat_id, limit=limit)
        message = None
        if not messages:
            return None
        for msg in messages:
            if not msg.service and not msg.empty:
                message = msg
                break

        if is_first and message is None:
            return self.get_last_valid_message(client, chat_id, limit=limit + 20, is_first=False)
        return message

    def get_telegram_accounts(
            self,
            db_chat: 'tg_models.Chat',
            with_admin_permissions: bool = False
    ) -> List['tg_models.TelegramAccount']:
        client_session_names = self.get_client_session_names()
        return self.db.telegram.get_telegram_accounts_by_session_names(
            db_chat=db_chat,
            session_names=client_session_names,
            with_admin_permissions=with_admin_permissions
        )

    @staticmethod
    def iter_messages(
            client: 'ClientProxy',
            chat_id: int,
            last_message_id: int,
    ) -> Generator['types.Message', None, None]:
        offset_id = last_message_id
        last_offset_id = last_message_id
        row = 0
        sleep_counter = 0
        sleep_time = 1
        total_msgs = 0
        started = time.perf_counter()

        while True:
            if not row % 5:
                sleep_counter += 1
                time.sleep(sleep_time)
            else:
                time.sleep(0.1)
            messages = client(
                'get_history',
                chat_id=chat_id,
                limit=100,
                offset=-1,
                offset_id=offset_id
            )
            if not messages:
                return
            last_offset_id, offset_id = offset_id, messages[-1].message_id
            row += 1
            total_msgs += len(messages)
            # logger.info((messages[0].message_id, messages[-1].message_id, len(messages)))
            logger.info(
                f"got {total_msgs} messages in {time.perf_counter() - started - sleep_counter * sleep_time:.3f} of chat: {chat_id}")

            # all_messages.extend(messages)
            for message in messages:
                yield message

            if last_offset_id == offset_id:
                return
            if offset_id == 1:
                return
