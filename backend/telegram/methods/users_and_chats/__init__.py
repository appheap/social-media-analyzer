from .get_updated_membership import GetUpdatedMembership
from .get_updated_adminship import GetUpdatedAdminShip
from .get_telegram_accounts_by_session_names import GetTelegramAccountsBySessionNames
from .get_membership import GetMembership
from .get_membership_by_user_id import GetMembershipByUserId
from .get_updated_chat_member import GetUpdatedChatMember


class UsersAndChats(
    GetUpdatedMembership,
    GetUpdatedAdminShip,
    GetTelegramAccountsBySessionNames,
    GetMembership,
    GetMembershipByUserId,
    GetUpdatedChatMember,

):
    pass
