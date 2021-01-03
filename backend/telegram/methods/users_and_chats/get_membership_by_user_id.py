from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models


class GetMembershipByUserId(Scaffold):

    def get_membership_by_user_id(
            self,
            *,
            user_id: int,
            db_chat: 'tg_models.Chat'
    ) -> Optional['tg_models.Membership']:
        if user_id is None or db_chat is None:
            return None

        return self.tg_models.Membership.objects.get_membership_by_user_id(
            user_id=user_id,
            db_chat=db_chat,
        )
