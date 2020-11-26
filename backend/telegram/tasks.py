from celery import shared_task

from telegram.client import client_utils
from telegram.globals import tg_function


@shared_task(queue='tg_queue', timeout=60)
def init_consumer():
    client_utils.init_consumer()


@shared_task(queue='default', timeout=60)
def init_clients(*args, **kwargs):
    return tg_function({
        'func': 'task_init_clients',
        'args': args,
        'kwargs': kwargs,
    })


@shared_task(queue='default', timeout=60)
def iterate_dialogs(*args, **kwargs):
    tg_function({
        'func': 'task_iterate_dialogs',
        'args': args,
        'kwargs': kwargs,
    })


@shared_task(queue='default', timeout=60)
def get_me(*args, **kwargs):
    return tg_function({
        'func': 'task_get_me',
        'args': args,
        'kwargs': kwargs,
    })


@shared_task(queue='default', timeout=60)
def request_add_tg_channel(*args, **kwargs):
    return tg_function({
        'func': 'task_add_tg_channel',
        'args': args,
        'kwargs': kwargs,
    })


@shared_task(queue='default', timeout=60)
def shared_media_analyzer(*args, **kwargs):
    tg_function({
        'func': 'task_analyze_chat_shared_medias',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def member_count_analyzer(*args, **kwargs):
    tg_function({
        'func': 'task_analyze_chat_member_count',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def message_view_analyzer(*args, **kwargs):
    tg_function({
        'func': 'task_analyze_message_views',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def iterate_chats_history(*args, **kwargs):
    tg_function({
        'func': 'task_iterate_chat_history',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def admin_logs_analyzer(*args, **kwargs):
    tg_function({
        'func': 'task_analyze_admin_logs',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def chat_member_analyzer(*args, **kwargs):
    tg_function({
        'func': 'task_analyze_all_chat_members',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def analyze_chat_members(*args, **kwargs):
    tg_function({
        'func': 'task_analyze_chat_members',
        'args': args,
        'kwargs': kwargs
    })
