#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
import logging
from signal import signal, SIGINT, SIGTERM, SIGABRT

log = logging.getLogger(__name__)

is_idling = False


async def idle():
    """Block the main script execution until a signal is received.

    This function will run indefinitely in order to block the main script execution and prevent it from
    exiting while having client(s) that are still running in the background.

    It is useful for event-driven application only, that are, applications which react upon incoming Telegram
    updates through handlers, rather than executing a set of methods sequentially.

    The way Pyrogram works, it will keep your handlers in a pool of worker threads, which are executed concurrently
    outside the main thread; calling idle() will ensure the client(s) will be kept alive by not letting the main
    script to end, until you decide to quit.

    Once a signal is received (e.g.: from CTRL+C) the function will terminate and your main script will continue.
    Don't forget to call :meth:`~pyrogram.Client.stop` for each running client before the script ends.

    Example:
        .. code-block:: python
            :emphasize-lines: 13

            from pyrogram import Client, idle

            app1 = Client("account1")
            app2 = Client("account2")
            app3 = Client("account3")

            ...  # Set handlers up

            app1.start()
            app2.start()
            app3.start()

            idle()

            app1.stop()
            app2.stop()
            app3.stop()
    """
    global is_idling

    def signal_handler(_, __):
        global is_idling

        logging.info("Stop signal received ({}). Exiting...".format(_))
        is_idling = False

    for s in (SIGINT, SIGTERM, SIGABRT):
        signal(s, signal_handler)

    is_idling = True

    while is_idling:
        await asyncio.sleep(1)
