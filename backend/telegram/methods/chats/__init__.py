from .get_updated_chat import GetUpdatedChat
from .get_updated_dialog import GetUpdatedDialog
from .admin_log_exists import AdminLogExists
from .create_admin_log import CreateAdminLog


class Chats(
    GetUpdatedChat,
    GetUpdatedDialog,
    AdminLogExists,
    CreateAdminLog,

):
    pass
