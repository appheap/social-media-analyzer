from db.database_manager import DataBaseManager
from typing import List, Optional
import pyrogram
from core.globals import logger


class TaskScaffold:

    def __init__(self, clients: List['pyrogram.Client']):
        self.db = DataBaseManager()
        self.clients = clients

    def get_client(self, session_name: str) -> Optional['pyrogram.Client']:
        for client in self.clients:
            logger.info(client.session_name)
            if client.session_name == session_name:
                return client

        return None

    def get_client_session_names(self) -> List['str']:
        _lst = []
        for client in self.clients:
            _lst.append(client.session_name)

        return _lst
