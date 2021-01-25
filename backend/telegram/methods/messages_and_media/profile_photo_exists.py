from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models
from users import models as site_models


class ProfilePhotoExists(Scaffold):

    def profile_photo_exists(
            self,
            *,
            db_site_user: 'site_models.SiteUser' = None,
            db_user: 'tg_models.User' = None,
            db_chat: 'tg_models.Chat' = None,
            upload_date: int,
    ) -> Optional['bool']:
        if (db_site_user is None and db_user is None and db_chat is None) or upload_date is None:
            return None

        return self.tg_models.ProfilePhoto.photos.photo_exists(
            db_site_user=db_site_user,
            db_user=db_user,
            db_chat=db_chat,
            upload_date=upload_date,
        )
