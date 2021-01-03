from .analyzers import Analyzers
from .base import Base
from .chats import Chats
from .users_and_chats import UsersAndChats


class TelegramMethods(
    Analyzers,
    Base,
    Chats,
    UsersAndChats,

):
    pass
