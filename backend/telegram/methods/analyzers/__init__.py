from .update_chat_analyzers_status import UpdateChatAnalyzersStatus
from .create_base_chat_analyzers import CreateBaseChatAnalyzers
from .create_admin_based_chat_analyzers import CreateAdminBasedChatAnalyzers
from .get_updated_message_view import GetUpdatedMessageView


class Analyzers(
    CreateBaseChatAnalyzers,
    CreateAdminBasedChatAnalyzers,
    UpdateChatAnalyzersStatus,
    GetUpdatedMessageView,

):
    pass
