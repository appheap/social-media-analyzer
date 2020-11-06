import os

from celery import Celery
from celery.signals import worker_ready
from kombu import Queue

from social_media_analyzer.globals import logger
from telegram import tasks as tg_tasks

# set the default Django settings module for the 'celery' program.


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_analyzer.settings')

# app = Celery('social_media_analyzer', backend='redis://localhost', broker='pyamqp://')
app = Celery('social_media_analyzer')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.

# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
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
from celery.schedules import crontab


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     Calls test('hello') every 10 seconds.
# sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

# print('celery started...')
# Calls test('world') every 30 seconds
# sender.add_periodic_task(30.0, test.s('world'), expires=10)

# Executes every Monday morning at 7:30 a.m.
# sender.add_periodic_task(
#     crontab(hour=7, minute=30, day_of_week=1),
#     test.s('Happy Mondays!'),
# )


@worker_ready.connect
def configure_workers(sender=None, conf=None, **kwargs):
    if sender.hostname == 'celery@telegram_worker':
        logger.info("Telegram consumer starting...")
        tg_tasks.init_consumer.delay()
        tg_tasks.init_clients.apply_async(countdown=5)
