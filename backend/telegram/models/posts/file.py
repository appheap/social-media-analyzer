from db.models import BaseFile
from django.db import models

from db.models import SoftDeletableQS


class FileQuerySet(SoftDeletableQS):
    pass


class FileManager(models.Manager):
    def get_queryset(self) -> 'FileQuerySet':
        return FileQuerySet(self.model, using=self._db)


class File(BaseFile):
    caption = models.TextField(
        max_length=1024,
        null=True,
        blank=True,
    )

    objects = FileManager()
    files = FileManager()
