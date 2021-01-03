from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models


class UpdateMembershipStatus(Scaffold):
    def update_membership_status(
            self,
            *,
            db_user: 'tg_models.User',
            db_chat: 'tg_models.Chat',
            new_status: 'tg_models.ChatMember',
            event_date_ts: int,
    ) -> Optional['tg_models.Membership']:
        if db_user is None or db_chat is None or new_status is None or event_date_ts is None:
            return None

        return self.tg_models.Membership.objects.update_or_create_membership(
            db_user=db_user,
            db_chat=db_chat,
            new_status=new_status,
            event_date_ts=event_date_ts,
        )
