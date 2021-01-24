from .get_updated_telegram_account import GetUpdatedTelegramAccount
from .get_updated_telegram_channel import GetUpdatedTelegramChannel
from .get_telegram_channel_by_id import GetTelegramChannelById
from .get_telegram_accounts_by_ids import GetTelegramAccountsByIds
from .get_telegram_account_by_id import GetTelegramAccountById
from .telegram_channel_exists import TelegramChannelExists
from .get_user_telegram_channels import GetUserTelegramChannels


class Base(
    GetUpdatedTelegramAccount,
    GetUpdatedTelegramChannel,
    TelegramChannelExists,
    GetTelegramChannelById,
    GetTelegramAccountsByIds,
    GetTelegramAccountById,
    GetUserTelegramChannels,

):
    pass
