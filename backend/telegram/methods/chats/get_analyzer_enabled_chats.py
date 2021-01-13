from django.db.models.query import QuerySet

from db.scaffold import Scaffold
from telegram import models as tg_models


class GetAnalyzerEnabledChats(Scaffold):

    def get_chats_filter_by_analyzer(
            self,

            *,
            admin_log_analyzer: bool = None,
            members_analyzer: bool = None,
            shared_media_analyzer: bool = None,
            member_count_analyzer: bool = None,
            message_view_analyzer: bool = None,
    ) -> 'QuerySet[tg_models.Chat]':
        if admin_log_analyzer is None and members_analyzer is None and shared_media_analyzer is None \
                and member_count_analyzer is None and message_view_analyzer is None:
            return None

        return self.tg_models.Chat.chats.get_chats_filter_by_analyzer(
            admin_log_analyzer=admin_log_analyzer,
            members_analyzer=members_analyzer,
            shared_media_analyzer=shared_media_analyzer,
            member_count_analyzer=member_count_analyzer,
            message_view_analyzer=message_view_analyzer,
        )
