from typing import Optional

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models


class GetUpdatedUser(Scaffold):
    def get_updated_user(
            self,
            *,
            raw_user: types.User,

            db_message_view: 'tg_models.MessageView' = None
    ) -> Optional['tg_models.User']:
        return self.tg_models.User.users.update_or_create_from_raw(
            raw_user=raw_user,

            db_message_view=db_message_view
        )
