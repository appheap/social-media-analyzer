from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models


class GetTelegramChannelById(Scaffold):

    def get_telegram_channel_by_id(
            self,
            channel_id: int,
    ) -> Optional['tg_models.TelegramChannel']:
        if channel_id is None:
            return None
        return self.tg_models.TelegramChannel.channels.get_by_channel_id(channel_id=channel_id)
