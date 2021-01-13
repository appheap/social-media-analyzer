from db.scaffold import Scaffold
from django.db import models
from telegram import models as tg_models


class UpdateAnalyzerMetaData(Scaffold):

    def update_analyzer_metadata(
            self,
            *,
            analyzer: 'models.Model',
            timestamp: int,
    ) -> bool:

        if analyzer is None or timestamp is None:
            return False

        _fields = {}
        if not analyzer.first_analyzed_ts:
            _fields['first_analyzed_ts'] = timestamp
        _fields['last_analyzed_ts'] = timestamp

        if isinstance(analyzer, tg_models.AdminLogAnalyzerMetaData):
            return analyzer.update_fields(
                **_fields
            )
        elif isinstance(analyzer, tg_models.ChatMembersAnalyzerMetaData):
            return analyzer.update_fields(
                **_fields
            )
        elif isinstance(analyzer, tg_models.ChatMemberCountAnalyzerMetaData):
            return analyzer.update_fields(
                **_fields
            )
        elif isinstance(analyzer, tg_models.SharedMediaAnalyzerMetaData):
            return analyzer.update_fields(
                **_fields
            )
        elif isinstance(analyzer, tg_models.ChatMessageViewsAnalyzerMetaData):
            return analyzer.update_fields(
                **_fields
            )

        return False
