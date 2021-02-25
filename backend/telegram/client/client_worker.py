from threading import Thread
from typing import Dict
from typing import List

import kombu
from kombu.mixins import ConsumerProducerMixin
from kombu.transport import pyamqp

import pyrogram
from telegram.globals import *


class ClientTaskConsumer(ConsumerProducerMixin):
    def __init__(
            self,
            connection: Connection,
            client: 'pyrogram.Client',
            db,
            task_queues: Dict['str', 'kombu.Queue'],
    ):
        logger.info('client task consumer started...')
        self.connection = connection
        self.client = client
        self.db = db
        self.task_queues = task_queues

        task_queue = Queue(
            f'{self.client.session_name}_queue',
            exchange=tg_exchange,
            routing_key=f'{self.client.session_name}_queue'
        )
        self.task_queue = task_queue
        self.task_queues[self.client.session_name] = task_queue
        logger.info(f"task_queues: {self.task_queues}")

    def get_consumers(self, consumer, channel) -> List[Consumer]:
        return [
            Consumer(
                queues=[self.task_queue],
                callbacks=[self.on_task],
                channel=channel,
                prefetch_count=1,
            )
        ]

    def on_task(self, body: dict, message: pyamqp.Message):
        attr_name = body['func']
        args = body['args']
        kwargs = body['kwargs']
        logger.info(f"client_task_consumer_on_task : {self.client.session_name}")

        response = {}
        if self.client.is_connected and attr_name:
            logger.info(attr_name)
            if attr_name == '__get_client_info__':
                response = {
                    'app_version': self.client.app_version,
                    'api_id': self.client.api_id,
                    'api_hash': self.client.api_hash,
                    'bot_token': self.client.bot_token,
                    'session_name': self.client.session_name,
                    'phone_number': self.client.phone_number,
                }

            attr = getattr(self.client, attr_name, None)
            if not len(response) and attr:
                if callable(attr):
                    if attr_name.startswith('iter'):
                        response = list((item for item in attr(*args, **kwargs)))
                    else:
                        response = attr(*args, **kwargs)
                else:
                    response = attr

        self.producer.publish(
            body=response,
            exchange='',
            routing_key=message.properties['reply_to'],
            correlation_id=message.properties['correlation_id'],
            serializer='pickle',
            retry=True,
        )
        message.ack()


class ClientWorkerThread(Thread):

    def __init__(self, client: 'pyrogram.Client', index: int, db, task_queues: Dict['str', 'kombu.Queue']):
        super().__init__()
        self.daemon = True
        self.client = client
        self.name = f'Client_Worker_Thread {index}'
        self.index = index
        self.db = db
        self.task_queues = task_queues
        self.consumer = None

    def run(self) -> None:
        logger.info(f"Client Worker {self.index} started ....")
        self.consumer = ClientTaskConsumer(
            connection=Connection('amqp://localhost'),
            client=self.client,
            db=self.db,
            task_queues=self.task_queues,
        )
        self.consumer.run()
