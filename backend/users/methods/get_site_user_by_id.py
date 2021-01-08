from typing import Optional

from db.scaffold import Scaffold
from users import models as site_models


class GetSiteUserById(Scaffold):
    def get_user_by_id(
            self,
            *,
            user_id: int,

    ) -> Optional['site_models.SiteUser']:
        if user_id is None:
            return None

        return self.site_models.SiteUser.objects.get_user_by_id(
            user_id=user_id
        )
