from typing import Optional

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models


class GetMessageFromRaw(Scaffold):

    def get_message_from_raw(
            self,
            *,
            chat_id: int,
            raw_message: types.Message,
    ) -> Optional['tg_models.Message']:
        if chat_id is None or raw_message is None:
            return None

        return self.tg_models.Message.objects.get_message_from_raw(
            chat_id=chat_id,
            raw_message=raw_message,
        )
