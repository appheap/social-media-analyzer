from db.models import BaseFile
from django.db import models


class File(BaseFile):
    caption = models.TextField(
        max_length=1024,
        null=True,
        blank=True,
    )
