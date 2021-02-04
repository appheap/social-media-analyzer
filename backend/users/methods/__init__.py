from .get_site_user_by_id import GetSiteUserById
from .get_site_user_by_username import GetSiteUserByUsername
from .get_default_site_user import GetDefaultSiteUser


class UsersMethods(
    GetSiteUserById,
    GetSiteUserByUsername,
    GetDefaultSiteUser,
):
    pass
