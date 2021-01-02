from .create_telegram_account import CreateTelegramAccount
from .create_telegram_channel import CreateTelegramChannel


class Base(
    CreateTelegramAccount,
    CreateTelegramChannel,

):
    pass
