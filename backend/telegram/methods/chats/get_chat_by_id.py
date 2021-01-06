from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models


class GetChatById(Scaffold):
    def get_chat_by_id(
            self,
            *,
            chat_id: int
    ) -> Optional['tg_models.Chat']:
        if chat_id is None:
            return None

        return self.tg_models.Chat.chats.get_chat_by_id(
            chat_id=chat_id,
        )
