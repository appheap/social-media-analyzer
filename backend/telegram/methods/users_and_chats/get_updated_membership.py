from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models


class GetUpdatedMembership(Scaffold):
    def get_updated_membership(
            self,
            *,
            db_chat: 'tg_models.Chat',
            new_status: 'tg_models.ChatMember',
            event_date_ts: int,
    ) -> Optional['tg_models.Membership']:
        if db_chat is None or new_status is None or event_date_ts is None:
            return None

        db_membership = self.tg_models.Membership.objects.get_membership(
            db_chat=db_chat,
            db_user=new_status.user
        )
        if db_membership:
            db_membership.update_membership_status(
                new_status=new_status,
                event_date_ts=event_date_ts,
            )
        else:
            db_membership = self.tg_models.Membership.objects.update_or_create_membership(
                db_user=new_status.user,
                db_chat=db_chat,
                new_status=new_status,
                event_date_ts=event_date_ts,
            )

        return db_membership
