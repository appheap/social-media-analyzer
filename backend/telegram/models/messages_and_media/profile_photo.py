from django.db import models
from ..base import BaseModel
from db.models import SoftDeletableBaseModel


class ProfilePhoto(BaseModel, SoftDeletableBaseModel):
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    upload_date = models.BigIntegerField(blank=True, null=True)

    photo = models.ImageField(upload_to=BaseModel.file_dir_path, null=True, blank=True)

    user = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        related_name='profile_photos',
        null=True,
        blank=True,
    )

    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        related_name='profile_photos',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.upload_date if self.upload_date else self.id}"
