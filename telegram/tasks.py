from celery import shared_task

from telegram.client import client_utils
from telegram.globals import tg_function


@shared_task(queue='tg_queue', timeout=60)
def init_consumer():
    client_utils.init_consumer()


@shared_task(queue='default', timeout=60)
def init_clients():
    return tg_function({'func': 'init_clients', 'args': {}, 'kwargs': {}})


@shared_task(queue='default', timeout=60)
def iterate_dialogs():
    tg_function({
        'func': 'iterate_dialogs',
        'args': {},
        'kwargs': {},
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
