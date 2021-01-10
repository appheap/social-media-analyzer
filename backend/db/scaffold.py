from pyrogram import types
from typing import Optional
from telegram import models as tg_models
from users import models as site_models


class Scaffold:

    def __init__(self):
        self.tg_models = tg_models
        self.site_models = site_models

    def get_updated_user(
            self,
            *,
            raw_user: 'types.User',

            db_message_view: 'tg_models.MessageView' = None
    ) -> Optional['tg_models.User']:
        pass
