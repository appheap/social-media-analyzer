from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models


class GetMembership(Scaffold):

    def get_membership(
            self,
            *,
            db_user: 'tg_models.User',
            db_chat: 'tg_models.Chat'
    ) -> Optional['tg_models.Membership']:
        if db_user is None or db_chat is None:
            return None

        return self.tg_models.Membership.objects.get_membership(
            db_user=db_user,
            db_chat=db_chat,
        )
