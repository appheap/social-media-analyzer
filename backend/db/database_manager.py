from .methods import TelegramMethods
from .scaffold import Scaffold


class DataBaseManager(Scaffold):

    def __int__(self):
        self.telegram = TelegramMethods()
