from threading import Thread
from typing import List

from kombu import Connection

import pyrogram
from core.globals import logger
from .worker import Worker


class TelegramConsumerManager(Thread):

    def __init__(self, clients: List['pyrogram.Client'], index: int):
        Thread.__init__(self)

        self.daemon = True
        self.clients = clients
        self.name = f'Telegram_Consumer_Manager_Thread {index}'
        self.index = index

    def run(self) -> None:
        logger.info(f"Telegram Consumer {self.index} started ....")
        Worker(connection=Connection('amqp://localhost'), clients=self.clients, index=self.index).run()
