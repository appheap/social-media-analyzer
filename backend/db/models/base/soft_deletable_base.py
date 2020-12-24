import arrow
from django.db import models


class SoftDeletableQS(models.QuerySet):
    """A queryset that allows soft-delete on its objects"""

    def delete(self, **kwargs):
        self.update(deleted_ts=kwargs.get('deleted_ts', arrow.now().timestamp), **kwargs)

    def hard_delete(self):
        super().delete()

    def not_deleted(self) -> "SoftDeletableQS":
        return self.filter(deleted_ts__isnull=True)


class SoftDeletableManager(models.Manager):
    """Manager that filters out soft-deleted objects"""

    def get_queryset(self) -> "SoftDeletableQS":
        return SoftDeletableQS(
            model=self.model, using=self._db, hints=self._hints
        ).not_deleted()


class SoftDeletableBaseModel(models.Model):
    deleted_ts = models.BigIntegerField(null=True, blank=True)
    is_exact_ts = models.BooleanField(null=True, blank=True)

    objects = SoftDeletableManager()
    archived_objects = models.Manager()

    def delete(self, **kwargs):
        """Softly delete the entry"""
        self.deleted_ts = kwargs.get('deleted_ts', arrow.now().timestamp)
        self.is_exact_ts = 'deleted_ts' in kwargs
        for k, v in kwargs:
            if hasattr(self, k):
                setattr(self, k, v)
        self.save()

    def hard_delete(self):
        """Remove the entry from the database permanently"""
        super().delete()

    class Meta:
        abstract = True
        ordering = ('-deleted_ts',)
