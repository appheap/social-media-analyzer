from threading import Thread
from typing import List
import pyrogram


class TelegramConsumerManager(Thread):

    def __init__(self, clients: List['pyrogram.Client'], index: int):
        Thread.__init__(self)

        self.daemon = True
        self.clients = clients
        self.name = f'Telegram_Consumer_Manager_Thread {index}'
        self.index = index

    def run(self) -> None:
        pass
