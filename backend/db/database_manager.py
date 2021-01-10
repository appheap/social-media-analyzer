class DataBaseManager:

    def __init__(self):
        from telegram import models as tg_models
        from users import models as site_models

        self.tg_models = tg_models
        self.site_models = site_models

        from .methods import TelegramMethods
        from .methods import UsersMethods
        self._telegram = TelegramMethods()
        self._users = UsersMethods()

    @property
    def telegram(self):
        return self._telegram

    @property
    def users(self):
        return self._users
