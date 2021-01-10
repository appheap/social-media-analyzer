import threading
from typing import List, Optional, Callable

from kombu import Consumer
from kombu.mixins import ConsumerProducerMixin
from kombu.connection import Connection
from db.database_manager import DataBaseManager
from telegram import globals as tg_globals
import pyrogram
from core.globals import logger
from utils.utils import prettify
from kombu.transport import pyamqp
from .base_response import BaseResponse

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
        logger.info(type(body))
        logger.info(type(message))
        func = body['func']
        args = body['args']
        kwargs = body['kwargs']

        logger.info(f'on consumer {self.index} Got task: {prettify(body)}')

        if func == 'task_init_clients':
            response = self.task_init_clients(*args, **kwargs)

        elif func == 'task_get_me':
            response = self.task_get_me(*args, **kwargs)

        elif func == 'task_add_tg_channel':
            response = self.task_add_tg_channel(*args, **kwargs)

        elif func == 'task_iterate_dialogs':
            response = self.task_iterate_dialogs(*args, **kwargs)

        elif func == 'task_analyze_chat_shared_medias':
            response = self.task_analyze_chat_shared_medias(*args, **kwargs)

        elif func == 'task_analyze_chat_member_count':
            response = self.task_analyze_chat_member_count(*args, **kwargs)

        elif func == 'task_analyze_message_views':
            response = self.task_analyze_message_views(*args, **kwargs)

        elif func == 'task_iterate_chat_history':
            response = self.task_iterate_chat_history(*args, **kwargs)

        elif func == 'task_analyze_admin_logs':
            response = self.task_analyze_admin_logs(*args, **kwargs)

        elif func == 'task_analyze_all_chat_members':
            response = self.task_analyze_all_chat_members(*args, **kwargs)

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

    def acquire_clients(self, func: Callable) -> BaseResponse:
        def wrapper(*args, **kwargs):
            with clients_lock as lock:
                if len(self.clients) != 0:
                    return func(*args, **kwargs) if callable(func) else BaseResponse().fail()
                else:
                    return BaseResponse().fail()

        return wrapper