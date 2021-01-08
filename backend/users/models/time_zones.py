from django.db import models


class TimeZones(models.TextChoices):
    UTC = 'UTC'
    ASIA_TEHRAN = 'Asia/Tehran'
