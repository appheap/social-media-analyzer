from ..object import Object
import pyrogram
from pyrogram import raw, types


class ChatAdminRights(Object):
    def __init__(
            self,
            *,
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
        super().__init__(None)

        self.can_change_info = can_change_info
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_delete_messages = can_delete_messages
        self.can_ban_users = can_ban_users
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_add_admins = can_add_admins
        self.is_anonymous = is_anonymous

    @staticmethod
    def _parse(admin_rights: "raw.types.ChatAdminRights"):
        if admin_rights is None:
            return None

        return ChatAdminRights(
            can_change_info=getattr(admin_rights, 'change_info', None),
            can_post_messages=getattr(admin_rights, 'post_messages', None),
            can_edit_messages=getattr(admin_rights, 'edit_messages', None),
            can_delete_messages=getattr(admin_rights, 'delete_messages', None),
            can_ban_users=getattr(admin_rights, 'ban_users', None),
            can_invite_users=getattr(admin_rights, 'invite_users', None),
            can_pin_messages=getattr(admin_rights, 'pin_messages', None),
            can_add_admins=getattr(admin_rights, 'add_admins', None),
            is_anonymous=getattr(admin_rights, 'anonymous', None),
        )
