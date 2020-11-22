from django.apps import AppConfig


class TelegramConfig(AppConfig):
    name = 'backend.telegram'

    def ready(self):
        import backend.telegram.signals
