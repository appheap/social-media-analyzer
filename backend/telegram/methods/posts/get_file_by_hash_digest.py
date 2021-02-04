from typing import Optional

from db.scaffold import Scaffold
from telegram import models as tg_models


class GetFileByHashDigest(Scaffold):
    def get_file_by_hash_digest(self, *, hash_digest: str) -> Optional['tg_models.Post']:
        if hash_digest is None:
            return None

        return self.tg_models.File.files.get_file_by_hash_digest(hash_digest=hash_digest)
