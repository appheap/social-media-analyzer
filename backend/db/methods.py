from telegram.methods import TelegramMethods
from users.methods import UsersMethods


class Methods(
    UsersMethods,
    TelegramMethods,

):
    pass
