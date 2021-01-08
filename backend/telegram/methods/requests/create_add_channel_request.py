from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models
from users import models as site_models


class CreateAddChannelRequest(Scaffold):

    def create_add_channel_request(
            self,
            *,
            db_site_user: 'site_models.SiteUser',
            db_admin: 'tg_models.TelegramAccount',
            channel_username: str,
            db_telegram_channel: 'tg_models.TelegramChannel',
    ) -> Optional['tg_models.AddChannelRequest']:
        if db_site_user is None or db_admin is None or channel_username is None or db_telegram_channel is None:
            return None

        db_request = self.tg_models.AddChannelRequest.objects.get_undone_request(
            channel_username=channel_username,
            db_site_user=db_site_user,
        )
        if db_request:
            raise Exception('Request already exists')

        return self.tg_models.AddChannelRequest.objects.create_request(
            db_site_user=db_site_user,
            db_admin=db_admin,
            channel_username=channel_username,
            db_telegram_channel=db_telegram_channel,
        )
