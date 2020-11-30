import asyncio
import logging
import time

log = logging.getLogger(__name__)


class Syncer:
    INTERVAL = 20

    clients = {}
    event = None
    lock = None

    @classmethod
    async def add(cls, client):
        if cls.event is None:
            cls.event = asyncio.Event()

        if cls.lock is None:
            cls.lock = asyncio.Lock()

        async with cls.lock:
            await cls.sync(client)

            cls.clients[id(client)] = client

            if len(cls.clients) == 1:
                cls.start()

    @classmethod
    async def remove(cls, client):
        async with cls.lock:
            await cls.sync(client)

            del cls.clients[id(client)]

            if len(cls.clients) == 0:
                cls.stop()

    @classmethod
    def start(cls):
        cls.event.clear()
        asyncio.get_event_loop().create_task(cls.worker())

    @classmethod
    def stop(cls):
        cls.event.set()

    @classmethod
    async def worker(cls):
        while True:
            try:
                await asyncio.wait_for(cls.event.wait(), cls.INTERVAL)
            except asyncio.TimeoutError:
                async with cls.lock:
                    for client in cls.clients.values():
                        await cls.sync(client)
            else:
                break

    @classmethod
    async def sync(cls, client):
        try:
            start = time.time()
            await client.storage.save()
        except Exception as e:
            log.critical(e, exc_info=True)
        else:
            log.info(f'Synced "{client.storage.name}" in {(time.time() - start) * 1000:.6} ms')
