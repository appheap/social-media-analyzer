import os

from celery import Celery
from celery.signals import worker_ready
from kombu import Queue

from backend.core.globals import logger
from backend.telegram import tasks as tg_tasks
from backend.utils.utils import prettify

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# app = Celery('core', backend='redis://localhost', broker='pyamqp://')
app = Celery('core')
# Using a string here means the worker doesn't have to serialize the configuration object to child processes.

# - namespace='CELERY' means all celery-related configuration keys should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_default_queue = 'default'
app.conf.task_queues = (
    Queue('default', exchange='default', routing_key='default'),
    Queue('tg_queue', exchange='tg_queue', routing_key='tg_queue'),
    Queue('slow_queue', exchange='slow_queue', routing_key='slow_queue'),
)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# filter out sensitive information
app.conf.humanize(with_defaults=False, censored=True)


############################################

@worker_ready.connect
def configure_workers(sender=None, conf=None, **kwargs):
    if sender.hostname == 'celery@telegram_worker':
        logger.info("Telegram consumer starting...")
        tg_tasks.init_consumer.delay()
        tg_tasks.init_clients.apply_async(countdown=5)

# @celeryd_init.connect
# def celery_init(sender=None, conf=None, **kwargs):
#     logger.info(f"{sender}\n\n\n")
#     logger.info(f"{prettify(conf)}\n\n\n")
#     logger.info(f"{prettify(kwargs)}\n\n\n")
