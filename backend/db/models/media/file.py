import uuid

from ..base import BaseModel, SoftDeletableBaseModel

from django.db import models


class FileTypes(models.TextChoices):
    file = 'file'
    photo = 'photo'
    video = 'video'
    undefined = 'undefined'


class File(BaseModel, SoftDeletableBaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    type = models.CharField(
        FileTypes.choices,
        max_length=15,
        default=FileTypes.file,
    )

    file = models.FileField(upload_to='files/')

    # the user who uploaded this file
    uploaded_by = models.ForeignKey(
        'users.SiteUser',
        on_delete=models.CASCADE,
        null=False,
        related_name='uploaded_files',
    )
