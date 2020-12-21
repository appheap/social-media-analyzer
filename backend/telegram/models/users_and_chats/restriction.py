from django.db import DatabaseError
from django.db import models

from pyrogram import types
from telegram import models as tg_models
from telegram.globals import logger
from ..base import BaseModel
from typing import List, Optional


class RestrictionQuerySet(models.QuerySet):
    def update_or_create_restriction(self, **kwargs):
        try:
            return self.update_or_create(
                **kwargs
            )
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def clear_restrictions(
            self,
            *,
            user: "tg_models.User" = None,
            chat: "tg_models.Chat" = None,
            message: "tg_models.Message" = None
    ):
        try:
            self.filter(
                user=user,
                chat=chat,
                message=message
            ).delete()
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)


class RestrictionManager(models.Manager):
    def get_queryset(self) -> "RestrictionQuerySet":
        return RestrictionQuerySet(self.model, using=self._db)

    def update_or_create(
            self,
            *,
            restriction: types.Restriction,
            user: "tg_models.User" = None,
            chat: "tg_models.Chat" = None,
            message: "tg_models.Message" = None
    ) -> Optional["Restriction"]:

        if restriction is None:
            return None
        parsed_object = RestrictionManager._parse_restriction(restriction)
        if not parsed_object:
            return None

        self.get_queryset().clear_restrictions(user=user, chat=chat, message=message)
        return self.get_queryset().update_or_create_restriction(
            **parsed_object
        )

    def bulk_create_restrictions(
            self,
            *,
            restrictions: List['types.Restriction'],
            user: "tg_models.User" = None,
            chat: "tg_models.Chat" = None,
            message: "tg_models.Message" = None
    ):
        if restrictions is None:
            return
        self.get_queryset().clear_restrictions(user=user, chat=chat, message=message)

        try:
            self.get_queryset() \
                .bulk_create(filter(lambda obj: obj is not None, map(RestrictionManager._parse, restrictions)))
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

    @staticmethod
    def _parse(restriction):
        parsed_object = RestrictionManager._parse_restriction(restriction)
        if not parsed_object:
            return None
        obj = Restriction(
            **parsed_object
        )
        return obj

    @staticmethod
    def _parse_restriction(
            restriction: types.Restriction,
            user: "tg_models.User" = None,
            chat: "tg_models.Chat" = None,
            message: "tg_models.Message" = None
    ):

        if restriction is None:
            return None
        return {
            'platform': restriction.platform,
            'reason': restriction.reason,
            'text': restriction.text,
            'user': user,
            'chat': chat,
            'message': message,
        }


class Restriction(BaseModel):
    """
    The reason why this chat/bot might be unavailable to some users. This field is available only in case is_restricted of `chat` or `bot` is True.
    """

    platform = models.CharField(max_length=256, null=True, blank=True)
    reason = models.CharField(max_length=256, null=True, blank=True)
    text = models.CharField(max_length=256, null=True, blank=True)

    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='restrictions',
    )

    user = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='restrictions',
    )

    message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='restrictions',
    )

    objects = RestrictionManager()

    ##############################################

    def __str__(self):
        return self.reason
