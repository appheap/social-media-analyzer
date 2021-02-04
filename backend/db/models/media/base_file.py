import hashlib
import uuid

from django.db import models

from ..base import BaseModel, SoftDeletableBaseModel


class FileTypes(models.TextChoices):
    file = 'file'
    photo = 'photo'
    video = 'video'
    audio = 'audio'
    document = 'document'
    undefined = 'undefined'


class BaseFile(BaseModel, SoftDeletableBaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    type = models.CharField(
        FileTypes.choices,
        max_length=15,
        default=FileTypes.file,
    )

    file = models.FileField(upload_to='files/')
    hash_hexhdigest = models.CharField(max_length=256, blank=True)
    name = models.CharField(max_length=1024, blank=True)
    content_type = models.CharField(max_length=128, blank=True)
    size = models.BigIntegerField(blank=True)

    # the user who uploaded this file
    uploaded_by = models.ForeignKey(
        'users.SiteUser',
        on_delete=models.CASCADE,
        related_name='uploaded_files',
        null=False,
        blank=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.hash_hexhdigest is None or len(self.hash_hexhdigest) < 128:

            self.name = self.file.file.name
            self.content_type = self.file.file.content_type
            self.size = self.file.file.size

            m = hashlib.sha3_512()
            for chunk in self.file.chunks():
                m.update(chunk)
            self.hash_hexhdigest = m.hexdigest()

        return super().save(*args, **kwargs)
