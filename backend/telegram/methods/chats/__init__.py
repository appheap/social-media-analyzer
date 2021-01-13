from .get_updated_chat import GetUpdatedChat
from .get_analyzer_enabled_chats import GetAnalyzerEnabledChats
from .get_updated_dialog import GetUpdatedDialog
from .get_updated_dialogs import GetUpdatedDialogs
from .admin_log_exists import AdminLogExists
from .create_admin_log import CreateAdminLog
from .get_chat_by_id import GetChatById
from .get_chat_by_username import GetChatByUsername


class Chats(
    GetUpdatedChat,
    GetAnalyzerEnabledChats,
    GetUpdatedDialog,
    GetUpdatedDialogs,
    AdminLogExists,
    CreateAdminLog,
    GetChatById,
    GetChatByUsername,

):
    pass
