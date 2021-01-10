from typing import Optional

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models


class GetUpdatedChatMember(Scaffold):

    def get_updated_chat_member(
            self,
            *,
            raw_chat_member: types.ChatMember,
            db_chat: 'tg_models.Chat',

            event_date_ts: int,
            left_date_ts: int = None,
            is_previous: bool = None,

            demoted_by: 'types.User' = None,

    ) -> Optional['tg_models.ChatMember']:
        db_membership = self.get_membership_by_user_id(
            user_id=raw_chat_member.user.id,
            db_chat=db_chat,
        )
        if db_membership is None:
            return None

        db_promoted_by = self.get_updated_user(
            raw_user=raw_chat_member.promoted_by,
        )
        db_demoted_by = self.get_updated_user(
            raw_user=demoted_by,
        )
        db_kicked_by = self.get_updated_user(
            raw_user=raw_chat_member.kicked_by,
        )
        db_invited_by = self.get_updated_user(
            raw_user=raw_chat_member.invited_by,
        )

        return self.tg_models.ChatMember.objects.update_or_create_from_raw(
            raw_chat_member=raw_chat_member,
            db_membership=db_membership,
            event_date_ts=event_date_ts,
            left_date_ts=left_date_ts,
            is_previous=is_previous,
            promoted_by=db_promoted_by,
            demoted_by=db_demoted_by,
            invited_by=db_invited_by,
            kicked_by=db_kicked_by,
        )
