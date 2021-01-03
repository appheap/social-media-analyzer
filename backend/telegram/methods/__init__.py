from .analyzers import Analyzers
from .base import Base
from .users import Users
from .chats import Chats
from .users_and_chats import UsersAndChats


class TelegramMethods(
    Analyzers,
    Base,
    Users,
    Chats,
    UsersAndChats,

):
    pass
