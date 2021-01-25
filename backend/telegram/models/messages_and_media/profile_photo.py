import os
from typing import Optional

from django.core.files import File
from django.db import models, DatabaseError

from core.globals import logger
from db.models import SoftDeletableBaseModel, SoftDeletableQS
from telegram import models as tg_models
from users import models as site_models
from ..base import BaseModel


class ProfilePhotoQuerySet(SoftDeletableQS):
    def filter_by_photo_id(self, *, photo_id: str) -> 'ProfilePhotoQuerySet':
        return self.filter(photo_id=photo_id)

    def update_or_create_photo(self, *, defaults: dict, **kwargs) -> Optional["ProfilePhoto"]:
        try:
            return self.update_or_create(
                defaults=defaults,
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None


class ProfilePhotoManager(models.Manager):
    def get_queryset(self) -> 'ProfilePhotoQuerySet':
        return ProfilePhotoQuerySet(self.model, using=self._db)

    def photo_exists(
            self,
            *,
            db_site_user: 'site_models.SiteUser',
            db_user: 'tg_models.User',
            db_chat: 'tg_models.Chat',
            upload_date: int,
    ) -> Optional['bool']:
        if (db_site_user is None and db_user is None and db_chat is None) or upload_date is None:
            return None

        return self.get_queryset().filter_by_photo_id(photo_id=self._get_photo_id(
            db_site_user=db_site_user,
            db_user=db_user,
            db_chat=db_chat,
            upload_date=upload_date,
        )).exists()

    @staticmethod
    def _get_photo_id(
            db_site_user: 'site_models.SiteUser',
            db_user: 'tg_models.User',
            db_chat: 'tg_models.Chat',
            upload_date: int,
    ) -> Optional['str']:
        if (db_site_user is None and db_user is None and db_chat is None) or upload_date is None:
            return None
        if db_site_user:
            _id = f'site_user:{db_site_user.id}'
        elif db_user:
            _id = f'user:{db_user.user_id}'
        else:
            _id = f'chat:{db_chat.chat_id}'
        _id += f':{upload_date}'
        return _id

    def update_or_create_profile_photo(
            self,
            *,
            db_site_user: 'site_models.SiteUser',
            db_user: 'tg_models.User',
            db_chat: 'tg_models.Chat',
            file_path: str,
            upload_date: int,
            width: float,
            height: float,
            file_size: float,
    ) -> Optional['ProfilePhoto']:
        if (db_site_user is None and db_user is None and db_chat is None) or upload_date is None or file_path is None:
            return None

        _id = self._get_photo_id(
            db_site_user=db_site_user,
            db_chat=db_chat,
            db_user=db_user,
            upload_date=upload_date
        )

        db_photo = self.get_queryset().update_or_create_photo(
            photo_id=_id,
            defaults={
                'chat': db_chat,
                'user': db_user,
                'site_user': db_site_user,
                'upload_date': upload_date,
                'width': width,
                'height': height,
                'file_size': file_size,
            }
        )
        if db_photo:
            db_photo.photo.save(
                os.path.basename(file_path),
                File(open(file_path, 'rb'))
            )
            db_photo.save()

        return db_photo


class ProfilePhoto(BaseModel, SoftDeletableBaseModel):
    photo_id = models.CharField(max_length=256, primary_key=True, blank=True)
    # `{chat|user|site_user}:{chat__chat_id|user__user_id|site_user__id}:upload_date`

    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    file_size = models.FloatField(blank=True, null=True)
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

    site_user = models.ForeignKey(
        'users.SiteUser',
        on_delete=models.CASCADE,
        related_name='profile_photos',
        null=True,
        blank=True,
    )

    photos = ProfilePhotoManager()

    def save(self, *args, **kwargs):
        if not self.photo_id:
            self.photo_id = ProfilePhotoManager._get_photo_id(
                db_site_user=self.site_user,
                db_user=self.user,
                db_chat=self.chat,
                upload_date=self.upload_date,
            )
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.photo_id}"
