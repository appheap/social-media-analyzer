from .get_updated_telegram_account import GetUpdatedTelegramAccount
from .get_updated_telegram_channel import GetUpdatedTelegramChannel
from .get_telegram_channel_by_id import GetTelegramChannelById
from .get_telegram_accounts_by_ids import GetTelegramAccountsByIds


class Base(
    GetUpdatedTelegramAccount,
    GetUpdatedTelegramChannel,
    GetUpdatedTelegramChannel,
    GetTelegramAccountsByIds,

):
    pass
