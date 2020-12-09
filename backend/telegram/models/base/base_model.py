import arrow
from django.db import models


class BaseModel(models.Model):
    created_at = models.BigIntegerField(null=False, blank=True, )
    modified_at = models.BigIntegerField(null=False, blank=True, )

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super().save(*args, **kwargs)
