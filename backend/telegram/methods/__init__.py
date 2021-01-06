from .analyzers import Analyzers
from .base import Base
from .users import Users
from .chats import Chats
from .messages_and_media import MessageAndMedia
from .users_and_chats import UsersAndChats


class TelegramMethods(
    Analyzers,
    Base,
    Users,
    Chats,
    MessageAndMedia,
    UsersAndChats,

):
    pass
