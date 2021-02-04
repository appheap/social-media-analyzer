from .get_updated_telegram_account import GetUpdatedTelegramAccount
from .get_updated_telegram_channel import GetUpdatedTelegramChannel
from .create_telegram_channel import CreateTelegramChannel
from .get_telegram_channel_by_id import GetTelegramChannelById
from .get_telegram_accounts_by_ids import GetTelegramAccountsByIds
from .get_telegram_account_by_id import GetTelegramAccountById
from .telegram_channel_exists import TelegramChannelExists
from .get_user_telegram_channels import GetUserTelegramChannels
from .get_all_available_telegram_accounts import GetAllAvailableTelegramAccounts
from .get_telegram_account_by_session_name import GetTelegramAccountBySessionName


class Base(
    GetUpdatedTelegramAccount,
    GetUpdatedTelegramChannel,
    CreateTelegramChannel,
    TelegramChannelExists,
    GetTelegramChannelById,
    GetTelegramAccountsByIds,
    GetTelegramAccountById,
    GetUserTelegramChannels,
    GetAllAvailableTelegramAccounts,
    GetTelegramAccountBySessionName,

):
    pass
