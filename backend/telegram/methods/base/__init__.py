from .get_updated_telegram_account import GetUpdatedTelegramAccount
from .get_updated_telegram_channel import GetUpdatedTelegramChannel


class Base(
    GetUpdatedTelegramAccount,
    GetUpdatedTelegramChannel,

):
    pass
