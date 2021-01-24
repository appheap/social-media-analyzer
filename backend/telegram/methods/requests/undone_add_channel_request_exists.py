from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models
from users import models as site_models


class UndoneAddChannelRequestExists(Scaffold):

    def undone_add_channel_request_exists(
            self,
            *,
            db_site_user: 'site_models.SiteUser',
            channel_username: str,
    ) -> Optional['tg_models.AddChannelRequest']:
        if db_site_user is None or channel_username is None:
            return None

        return self.tg_models.AddChannelRequest.objects.undone_request_exists(
            db_site_user=db_site_user,
            channel_username=channel_username,
        )
