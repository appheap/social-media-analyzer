from typing import List

from ..object import Object


class Channel(Object):
    def __init__(
            self,
            *,
            client: "Client" = None,
            id: int = None,
            title: str = None,
            is_forbidden: bool = None,
            username: str = None,
            photo: "Photo" = None,
            is_broadcast: bool = None,
            is_supergroup: bool = None,
            is_creator: bool = None,
            left: bool = None,
            is_verified: bool = None,
            is_restricted: bool = None,
            is_scam: bool = None,
            signatures: bool = None,
            has_private_join_link: bool = None,
            has_geo: bool = None,
            date: int = None,
            restrictions=List["Restriction"],
            admin_rights: "ChatAdminRights" = None,
            banned_rights: "ChatPermissions" = None,
            default_banned_rights: "ChatPermissions" = None,
            members_count: int = None,

    ):
        super().__init__(client)

        self.client = client
        self.id = id
        self.title = title
        self.is_forbidden = is_forbidden
        self.username = username
        self.photo = photo
        self.is_broadcast = is_broadcast
        self.is_supergroup = is_supergroup
        self.is_creator = is_creator
        self.left = left
        self.is_verified = is_verified
        self.is_restricted = is_restricted
        self.is_scam = is_scam
        self.signatures = signatures
        self.has_private_join_link = has_private_join_link
        self.has_geo = has_geo
        self.date = date
        self.restrictions = restrictions
        self.admin_rights = admin_rights
        self.banned_rights = banned_rights
        self.default_banned_rights = default_banned_rights
        self.members_count = members_count
