from .analyzers import Analyzers
from .base import Base
from .chats import Chats


class TelegramMethods(
    Analyzers,
    Base,
    Chats,

):
    pass
