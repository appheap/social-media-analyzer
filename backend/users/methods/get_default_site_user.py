from typing import Optional

from db.scaffold import Scaffold
from users import models as site_models
from decouple import config


class GetDefaultSiteUser(Scaffold):
    def get_default_site_user(
            self,
    ) -> Optional['site_models.SiteUser']:
        username = config('DEFAULT_USER_USERNAME', cast=str, default=None)
        return self.get_site_user_by_username(
            username=username
        )
