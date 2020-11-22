from kombu import Connection, Exchange, Queue, uuid, Consumer
from backend.core.globals import logger
from backend.utils.utils import prettify

tg_exchange = Exchange('tg_exchange', 'direct', durable=True)
info_queue = Queue('tg_info_queue', exchange=tg_exchange, routing_key='tg_info_queue')
callback_queue = Queue(uuid(), auto_delete=True)

number_of_telegram_workers = 5


# reply_queue = Queue('tg_reply_queue', exchange=tg_exchange, routing_key='tg_reply_queue')


def tg_function(func_body):
    logger.info(f"@tg_function_call: {prettify(func_body)} ")

    response = None

    def callback(body, message):
        nonlocal response
        response = body
        logger.info(f"@tg_function_response: {body} ")

    # connections
    with Connection('amqp://localhost') as conn:
        # produce
        producer = conn.Producer(serializer='json')
        producer.publish(body=func_body,
                         exchange=tg_exchange, routing_key='tg_info_queue',
                         declare=[info_queue, callback_queue], retry=True,
                         correlation_id=uuid(),
                         reply_to=callback_queue.name,
                         retry_policy={
                             'interval_start': 0,
                             'interval_step': 2,
                             'interval_max': 30,
                             'max_retries': 30,
                         })
        with Consumer(conn, callbacks=[callback], queues=[callback_queue], no_ack=True):
            while response is None:
                conn.drain_events()
    return response
