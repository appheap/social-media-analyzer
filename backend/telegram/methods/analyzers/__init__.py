from .update_chat_analyzers_status import UpdateChatAnalyzersStatus
from .create_base_chat_analyzers import CreateBaseChatAnalyzers
from .create_admin_based_chat_analyzers import CreateAdminBasedChatAnalyzers
from .get_updated_message_view import GetUpdatedMessageView
from .get_updated_message_views import GetUpdatedMessageViews
from .get_updated_chat_member_count import GetUpdatedChatMemberCount
from .get_updated_chat_shared_media import GetUpdatedChatSharedMedia
from .update_analyzer_metadata import UpdateAnalyzerMetaData


class Analyzers(
    CreateBaseChatAnalyzers,
    CreateAdminBasedChatAnalyzers,
    UpdateChatAnalyzersStatus,
    GetUpdatedMessageView,
    GetUpdatedMessageViews,
    GetUpdatedChatMemberCount,
    GetUpdatedChatSharedMedia,
    UpdateAnalyzerMetaData,

):
    pass
