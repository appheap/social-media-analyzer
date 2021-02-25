from celery import shared_task

from telegram import globals as tg_globals
from telegram.globals import telegram_task
from .client.client_manager import ClientManager
from .client.worker import TelegramConsumer

import multiprocessing as mp
from telegram.client._client_manager import *
from core.globals import logger

mgr = mp.Manager()
shared_ns = mgr.Namespace()
import time


@shared_task(queue='tg_queue', timeout=60)
def init_consumer():
    global shared_ns
    global mgr
    shared_ns.task_queues = []
    task_queues = mgr.dict()

    client_mgrs = []
    consumers = []

    # for client_name, client_details in clients_dict.items():

    for client_name in client_names:
        client_mgr = ClientManager(client_name=client_name, task_queues=task_queues)
        client_mgr.start()
        client_mgrs.append(client_mgr)

    time.sleep(1)
    for i in range(tg_globals.number_of_telegram_workers):
        consumer = TelegramConsumer(i + 1, task_queues=task_queues)
        consumer.start()
        consumers.append(consumer)

    for client_mgr in client_mgrs:
        client_mgr.join()

    for consumer in consumers:
        consumer.join()


@shared_task(queue='default', timeout=60)
def init_clients(*args, **kwargs):
    return telegram_task({
        'func': 'task_init_clients',
        'args': args,
        'kwargs': kwargs,
    })


@shared_task(queue='default', timeout=60)
def iterate_dialogs(*args, **kwargs):
    telegram_task({
        'func': 'task_iterate_dialogs',
        'args': args,
        'kwargs': kwargs,
    })


@shared_task(queue='default', timeout=60)
def get_me(*args, **kwargs):
    return telegram_task({
        'func': 'task_get_me',
        'args': args,
        'kwargs': kwargs,
    })


@shared_task(queue='default', timeout=60)
def request_add_tg_channel(*args, **kwargs):
    return telegram_task({
        'func': 'add_telegram_channel_task',
        'args': args,
        'kwargs': kwargs,
    })


@shared_task(queue='default', timeout=60)
def shared_media_analyzer(*args, **kwargs):
    telegram_task({
        'func': 'log_chat_shared_medias_task',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def member_count_analyzer(*args, **kwargs):
    telegram_task({
        'func': 'log_chat_member_count_task',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def message_view_analyzer(*args, **kwargs):
    telegram_task({
        'func': 'log_message_views_task',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def iterate_chats_history(*args, **kwargs):
    telegram_task({
        'func': 'iterate_chat_history_task',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def admin_logs_analyzer(*args, **kwargs):
    telegram_task({
        'func': 'log_admin_logs_task',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def chat_member_analyzer(*args, **kwargs):
    telegram_task({
        'func': 'log_chat_members_task',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def analyze_chat_members(*args, **kwargs):
    telegram_task({
        'func': 'task_analyze_chat_members',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def upload_post(*args, **kwargs):
    telegram_task({
        'func': 'upload_post',
        'args': args,
        'kwargs': kwargs
    })
