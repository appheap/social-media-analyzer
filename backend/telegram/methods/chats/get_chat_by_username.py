from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models


class GetChatByUsername(Scaffold):
    def get_chat_by_username(
            self,
            *,
            username: str
    ) -> Optional['tg_models.Chat']:
        if username is None:
            return None

        return self.tg_models.Chat.chats.get_chat_by_username(
            username=username,
        )
