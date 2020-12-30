from django.db import DatabaseError
from django.db import models

from pyrogram import types
from telegram import models as tg_models
from telegram.globals import logger
from ..base import BaseModel
from typing import List, Optional


class RestrictionQuerySet(models.QuerySet):
    def update_or_create_restriction(self, **kwargs) -> Optional['Restriction']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def clear_restrictions(
            self,
            *,
            db_user: "tg_models.User" = None,
            db_chat: "tg_models.Chat" = None,
            db_message: "tg_models.Message" = None
    ):
        try:
            self.filter(
                user=db_user,
                chat=db_chat,
                message=db_message
            ).delete()
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)


class RestrictionManager(models.Manager):
    def get_queryset(self) -> "RestrictionQuerySet":
        return RestrictionQuerySet(self.model, using=self._db)

    def update_or_create_from_raw(
            self,
            *,
            raw_restriction: types.Restriction,
            user: "tg_models.User" = None,
            chat: "tg_models.Chat" = None,
            message: "tg_models.Message" = None
    ) -> Optional["Restriction"]:

        if raw_restriction is None:
            return None
        parsed_object = RestrictionManager._parse_restriction(raw_restriction=raw_restriction)
        if not parsed_object:
            return None

        self.get_queryset().clear_restrictions(db_user=user, db_chat=chat, db_message=message)
        return self.get_queryset().update_or_create_restriction(
            **parsed_object
        )

    def bulk_create_restrictions(
            self,
            *,
            raw_restrictions: List['types.Restriction'],
            user: "tg_models.User" = None,
            chat: "tg_models.Chat" = None,
            message: "tg_models.Message" = None
    ):
        if raw_restrictions is None:
            return
        self.get_queryset().clear_restrictions(db_user=user, db_chat=chat, db_message=message)

        try:
            self.get_queryset() \
                .bulk_create(filter(lambda obj: obj is not None, map(RestrictionManager._parse, raw_restrictions)))
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

    @staticmethod
    def _parse(raw_restriction) -> dict:
        parsed_object = RestrictionManager._parse_restriction(raw_restriction=raw_restriction)
        if not parsed_object:
            return None
        obj = Restriction(
            **parsed_object
        )
        return obj

    @staticmethod
    def _parse_restriction(
            *,
            raw_restriction: types.Restriction,
            db_user: "tg_models.User" = None,
            db_chat: "tg_models.Chat" = None,
            db_message: "tg_models.Message" = None
    ):

        if raw_restriction is None:
            return None
        return {
            'platform': raw_restriction.platform,
            'reason': raw_restriction.reason,
            'text': raw_restriction.text,
            'user': db_user,
            'chat': db_chat,
            'message': db_message,
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
