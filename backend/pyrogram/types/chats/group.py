from ..object import Object


class Group(Object):
    def __init__(
            self,
            *,
            client: "Client" = None,
            id: int = None,
            is_forbidden: bool = None,
            is_empty: bool = None,
            is_creator: bool = None,
            is_kicked: bool = None,
            left: bool = None,
            is_migrated: bool = None,
            title: str = None,
            photo: "Photo" = None,
            members_count: int = None,
            create_date: int = None,
            migrated_to: "" = None,
            admin_rights: "ChatAdminRights" = None,
            default_banned_rights: "ChatPermissions" = None,

    ):
        super().__init__(client)

        self.id = id
        self.is_forbidden = is_forbidden
        self.is_empty = is_empty
        self.is_creator = is_creator
        self.is_kicked = is_kicked
        self.left = left
        self.is_migrated = is_migrated
        self.title = title
        self.photo = photo
        self.members_count = members_count
        self.create_date = create_date
        self.migrated_to = migrated_to
        self.admin_rights = admin_rights
        self.default_banned_rights = default_banned_rights
