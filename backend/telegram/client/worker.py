import threading
from typing import List, Callable, Dict

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
from .tasks import TelegramTasks

clients_lock = threading.RLock()
from telegram.globals import *
import kombu
from threading import Thread


class Worker(ConsumerProducerMixin):
    info_queue = tg_globals.info_queue

    def __init__(
            self,
            connection: Connection,
            index: int,
            task_queues: Dict['str', 'kombu.Queue']
    ):
        self.connection = connection
        self.index = index
        self.db = DataBaseManager()
        self.telegram_tasks = TelegramTasks(task_queues)
        self.response = None
        self.task_queues = task_queues

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

        logger.info(f"task_queue_length: {len(self.task_queues)}")

        # if len(self.task_queues):
        #     messages = client_task(
        #         {
        #             'func': 'iter_history',
        #             'args': [],
        #             'kwargs': {
        #                 'chat_id':'just_123_test',
        #             },
        #         },
        #         self.task_queues.values()[0]
        #     )
        #     logger.info(messages)

        if func == 'task_init_clients':
            response = self.telegram_tasks.init_clients_task(*args, **kwargs)

        elif func == 'task_get_me':
            response = self.telegram_tasks.get_me_task(*args, **kwargs)

        elif func == 'add_telegram_channel_task':
            response = self.telegram_tasks.add_telegram_channel_task(*args, **kwargs)

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

        elif func == 'upload_post':
            response = self.telegram_tasks.upload_post(*args, **kwargs)

        else:
            response = BaseResponse().done()

        self.producer.publish(
            body=prettify(response, include_class_name=False),
            exchange='',
            routing_key=message.properties['reply_to'],
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


class TelegramConsumer(Thread):

    def __init__(self, index: int, task_queues: Dict['str', 'kombu.Queue']):
        Thread.__init__(self)

        self.daemon = True
        self.name = f'Telegram_Consumer_Manager_Thread {index}'
        self.index = index
        self.task_queues = task_queues

    def run(self) -> None:
        logger.info(f"Telegram Consumer {self.index} started ....")
        Worker(connection=Connection('amqp://localhost'), index=self.index, task_queues=self.task_queues).run()
