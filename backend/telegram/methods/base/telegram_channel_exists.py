from typing import Optional

from db.scaffold import Scaffold
from users import models as site_models


class TelegramChannelExists(Scaffold):

    def telegram_channel_exists(
            self,
            db_site_user: 'site_models.SiteUser',
            channel_username: str,
    ) -> Optional['bool']:
        if channel_username is None or db_site_user is None:
            return None
        return self.tg_models.TelegramChannel.channels.telegram_channel_exists(
            db_site_user=db_site_user,
            channel_username=channel_username,
        )
