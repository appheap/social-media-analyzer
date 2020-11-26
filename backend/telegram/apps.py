from django.apps import AppConfig


class TelegramConfig(AppConfig):
    name = 'telegram'

    def ready(self):
        import telegram.signals as signals
        _ = signals
