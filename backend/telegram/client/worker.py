from typing import List

from kombu import Consumer
from kombu.mixins import ConsumerProducerMixin
from kombu.connection import Connection
from db.database_manager import DataBaseManager
from telegram import globals as tg_globals
import pyrogram
from core.globals import logger
from utils.utils import prettify
from kombu.transport import pyamqp


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
