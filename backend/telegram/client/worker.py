import threading
from typing import List, Callable

from kombu import Consumer
from kombu.connection import Connection
from kombu.mixins import ConsumerProducerMixin
from kombu.transport import pyamqp

import pyrogram
from core.globals import logger
from db.database_manager import DataBaseManager
from telegram import globals as tg_globals
from utils.utils import prettify
from .base_response import BaseResponse
from .tasks.telegram_tasks import TelegramTasks

clients_lock = threading.RLock()


class Worker(ConsumerProducerMixin):
    tg_exchange = tg_globals.tg_exchange
    info_queue = tg_globals.info_queue

    def __init__(
            self,
            connection: Connection,
            clients: List['pyrogram.Client'],
            index: int
    ):
        self.connection = connection
        self.clients = clients
        self.index = index
        self.db = DataBaseManager()
        self.telegram_tasks = TelegramTasks(self.clients)

    def get_consumers(self, consumer, channel) -> List[Consumer]:
        return [
            Consumer(
                queues=[self.info_queue],
                callbacks=[self.on_task],
                channel=channel,
                prefetch_count=1,
            )
        ]

    def on_task(self, body: dict, message: pyamqp.Message):
        func = body['func']
        args = body['args']
        kwargs = body['kwargs']

        logger.info(f'on consumer {self.index} Got task: {prettify(body)}')

        if func == 'task_init_clients':
            response = self.telegram_tasks.init_clients_task(*args, **kwargs)

        elif func == 'task_get_me':
            response = self.telegram_tasks.get_me_task(*args, **kwargs)

        elif func == 'task_add_tg_channel':
            response = self.task_add_tg_channel(*args, **kwargs)

        elif func == 'task_iterate_dialogs':
            response = self.telegram_tasks.iterate_dialogs_task(*args, **kwargs)

        elif func == 'log_chat_shared_medias_task':
            response = self.telegram_tasks.log_chat_shared_medias_task(*args, **kwargs)

        elif func == 'log_chat_member_count_task':
            response = self.telegram_tasks.log_chat_member_count_task(*args, **kwargs)

        elif func == 'log_message_views_task':
            response = self.telegram_tasks.log_message_views_task(*args, **kwargs)

        elif func == 'iterate_chat_history_task':
            response = self.telegram_tasks.iterate_chat_history_task(*args, **kwargs)

        elif func == 'log_admin_logs_task':
            response = self.telegram_tasks.log_admin_logs_task(*args, **kwargs)

        elif func == 'log_chat_members_task':
            response = self.telegram_tasks.log_chat_members_task(*args, **kwargs)

        elif func == 'task_analyze_chat_members':
            response = self.task_analyze_chat_members(*args, **kwargs)

        else:
            response = BaseResponse().done()

        self.producer.publish(
            body=prettify(response, include_class_name=False),
            exchange='', routing_key=message.properties['reply_to'],
            correlation_id=message.properties['correlation_id'],
            serializer='json',
            retry=True,
        )
        message.ack()

    def acquire_clients(self, func: Callable):
        def wrapper(*args, **kwargs):
            with clients_lock as lock:
                if len(self.clients) != 0:
                    return func(*args, **kwargs) if callable(func) else BaseResponse().fail()
                else:
                    return BaseResponse().fail()

        return wrapper
