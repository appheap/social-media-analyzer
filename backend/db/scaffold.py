class Scaffold:
    def __init__(self):
        from telegram import models as tg_models
        from users import models as site_models

        self.tg_models = tg_models
        self.site_models = site_models