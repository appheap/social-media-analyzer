from celery import shared_task

from social_media_analyzer.globals import logger
from telegram.client import client_utils
from telegram.globals import tg_function


@shared_task(queue='tg_queue', timeout=60)
def init_consumer():
    client_utils.init_consumer()


@shared_task(queue='default', timeout=60)
def init_clients():
    return tg_function({'func': 'init_clients', 'args': {}, 'kwargs': {}})


@shared_task(queue='default', timeout=60)
def iterate_dialogs(*args, **kwargs):
    tg_function({
        'func': 'iterate_dialogs',
        'args': args,
        'kwargs': kwargs,
    })


@shared_task(queue='default', timeout=60)
def get_me():
    return tg_function({
        'func': 'get_me',
        'args': {},
        'kwargs': {},
    })


@shared_task(queue='default', timeout=60)
def request_add_tg_channel(*args, **kwargs):
    return tg_function({
        'func': 'request_add_tg_channel',
        'args': args,
        'kwargs': kwargs,
    })


@shared_task(queue='default', timeout=60)
def shared_media_analyzer(*args, **kwargs):
    tg_function({
        'func': 'run_shared_media_analyzer',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def member_count_analyzer(*args, **kwargs):
    tg_function({
        'func': 'run_member_count_analyzer',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def message_view_analyzer(*args, **kwargs):
    tg_function({
        'func': 'run_message_view_analyzer',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def admin_logs_analyzer(*args, **kwargs):
    tg_function({
        'func': 'run_admin_logs_analyzer',
        'args': args,
        'kwargs': kwargs
    })


@shared_task(queue='default', timeout=60)
def chat_member_analyzer(*args, **kwargs):
    tg_function({
        'func': 'run_chat_members_analyzer',
        'args': args,
        'kwargs': kwargs
    })
