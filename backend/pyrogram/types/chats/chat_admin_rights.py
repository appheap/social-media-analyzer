from ..object import Object


class ChatAdminRights(Object):
    def __init__(
            self,
            *,
            client: "Client" = None,
            can_change_info: bool = None,
            can_post_messages: bool = None,
            can_edit_messages: bool = None,
            can_delete_messages: bool = None,
            can_ban_users: bool = None,
            can_invite_users: bool = None,
            can_pin_messages: bool = None,
            can_add_admins: bool = None,
            is_anonymous: bool = None,
    ):
        super().__init__(client)

        self.can_change_info = can_change_info
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_delete_messages = can_delete_messages
        self.can_ban_users = can_ban_users
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_add_admins = can_add_admins
        self.is_anonymous = is_anonymous
