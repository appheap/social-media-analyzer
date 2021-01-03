from .update_membership_status import UpdateMembershipStatus
from .get_updated_adminship import GetUpdatedAdminShip
from .get_membership import GetMembership
from .get_membership_by_user_id import GetMembershipByUserId
from .get_updated_chat_member import GetUpdatedChatMember


class UsersAndChats(
    UpdateMembershipStatus,
    GetUpdatedAdminShip,
    GetMembership,
    GetMembershipByUserId,
    GetUpdatedChatMember,

):
    pass
