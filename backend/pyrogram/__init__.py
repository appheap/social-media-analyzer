__version__ = "1.0.7"
__license__ = "GNU Lesser General Public License v3 or later (LGPLv3+)"
__copyright__ = "Copyright (C) 2017-2020 Dan <https://github.com/delivrance>"


class StopTransmission(StopAsyncIteration):
    pass


class StopPropagation(StopAsyncIteration):
    pass


class ContinuePropagation(StopAsyncIteration):
    pass


import asyncio

from . import raw, types, filters, handlers, emoji
from .client import Client
from .sync import idle

# Save the main thread loop for future references
main_event_loop = asyncio.get_event_loop()
