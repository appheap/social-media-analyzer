from typing import Optional

from db.models import BaseFile
from django.db import models

from db.models import SoftDeletableQS
from telegram import models as tg_models


class FileQuerySet(SoftDeletableQS):
    def filter_post_by_hash_digest(self, *, hash_digest: str) -> 'FileQuerySet':
        return self.filter(hash_hexdigest=hash_digest)


class FileManager(models.Manager):
    def get_queryset(self) -> 'FileQuerySet':
        return FileQuerySet(self.model, using=self._db)

    def get_file_by_hash_digest(self, *, hash_digest: str) -> Optional['tg_models.Post']:
        if hash_digest is None:
            return None
        return self.get_queryset().filter_post_by_hash_digest(hash_digest=hash_digest).first()


class File(BaseFile):
    caption = models.TextField(
        max_length=1024,
        null=True,
        blank=True,
    )

    objects = FileManager()
    files = FileManager()
