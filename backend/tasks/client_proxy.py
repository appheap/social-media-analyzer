import kombu
from telegram.globals import *


class ClientProxy():
    def __init__(self, task_queue: 'kombu.Queue'):
        self.task_queue = task_queue
        self.api_id = None
        self.api_hash = None
        self.bot_token = None
        self.session_name = None
        self.phone_number = None
        self.init_attrs()

    def init_attrs(self):
        response = client_task(
            func_body={
                'func': '__get_client_info__',
                'args': [],
                'kwargs': {},
            },
            target_queue=self.task_queue,
        )
        self.api_id = response.get('api_id', None)
        self.api_hash = response.get('api_hash', None)
        self.bot_token = response.get('bot_token', None)
        self.session_name = response.get('session_name', None)
        self.phone_number = response.get('phone_number', None)

    def __call__(self, *args, **kwargs):
        func, *args = args
        response = client_task(
            func_body={
                'func': func,
                'args': args,
                'kwargs': kwargs,
            },
            target_queue=self.task_queue,
        )
        return response
