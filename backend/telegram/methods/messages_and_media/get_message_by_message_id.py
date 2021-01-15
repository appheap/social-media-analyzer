from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models


class GetMessageByMessageId(Scaffold):

    def get_message_by_message_id(
            self,
            *,
            db_chat: 'tg_models.Chat',
            message_id: int,
    ) -> Optional['tg_models.Message']:
        if db_chat is None or message_id is None:
            return None

        return self.tg_models.Message.objects.get_message_by_message_id(
            db_chat=db_chat,
            message_id=message_id,
        )
