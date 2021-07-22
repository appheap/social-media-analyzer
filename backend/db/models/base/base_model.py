import arrow
from django.db import models


class BaseModel(models.Model):
    created_ts = models.BigIntegerField(null=False, blank=True, )
    modified_ts = models.BigIntegerField(null=False, blank=True, )

    class Meta:
        abstract = True
        ordering = ('-modified_ts', '-created_ts')
        get_latest_by = ('-modified_ts', '-created_ts')
        indexes = [
            models.Index(fields=('-modified_ts', '-created_ts')),
        ]

    def save(self, *args, **kwargs):
        if not self.created_ts:
            self.created_ts = arrow.utcnow().timestamp()
        self.modified_ts = arrow.utcnow().timestamp()
        return super().save(*args, **kwargs)
