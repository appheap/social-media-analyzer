import arrow
from django.db import models

base_url_telegram = 'telegram/'
telegram_profile_photos_url = base_url_telegram + 'profile_photos/'


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

    @staticmethod
    def file_dir_path(instance, filename):
        print(type(instance))
        from telegram import models as tg_models

        if isinstance(instance, tg_models.User):
            return telegram_profile_photos_url + 'user_{0}_{1}'.format(instance.user_id, filename)
        else:
            raise ValueError(f'undefined instance {type(instance)}')
