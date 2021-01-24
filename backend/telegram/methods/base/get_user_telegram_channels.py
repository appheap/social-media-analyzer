from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models
from users import models as site_models


class GetUserTelegramChannels(Scaffold):

    def get_user_telegram_channels(
            self,
            *,
            db_site_user: 'site_models.SiteUser' = None,
    ) -> Optional['tg_models.TelegramChannel']:
        if db_site_user is None:
            return self.tg_models.TelegramChannel.channels.none()

        return self.tg_models.TelegramChannel.channels.get_user_telegram_channels(
            db_site_user=db_site_user,
        )
