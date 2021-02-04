from typing import Optional

from db.scaffold import Scaffold
from users import models as site_models


class GetSiteUserByUsername(Scaffold):
    def get_site_user_by_username(
            self,
            *,
            username: int,

    ) -> Optional['site_models.SiteUser']:
        if username is None:
            return None

        return self.site_models.SiteUser.objects.get_user_by_username(
            username=username
        )
