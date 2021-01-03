from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models


class GetUser(Scaffold):
    def get_user(self, *, user_id: int) -> Optional['tg_models.User']:
        return self.tg_models.User.users.get_user_by_id(user_id=user_id)
