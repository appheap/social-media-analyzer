from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models
from users import models as site_models


class GetLatestProfilePhoto(Scaffold):

    def get_latest_profile_photo(
            self,
            *,
            db_site_user: 'site_models.SiteUser' = None,
            db_user: 'tg_models.User' = None,
            db_chat: 'tg_models.Chat' = None,
    ) -> Optional['tg_models.ProfilePhoto']:
        if db_site_user is None and db_user is None and db_chat is None:
            return None

        return self.tg_models.ProfilePhoto.photos.get_latest_profile_photo(
            db_site_user=db_site_user,
            db_user=db_user,
            db_chat=db_chat,
        )
