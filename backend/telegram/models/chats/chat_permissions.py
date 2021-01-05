from typing import Optional

from django.db import DatabaseError
from django.db import models

from pyrogram import types
from core.globals import logger
from ..base import BaseModel


class ChatPermissionsQuerySet(models.QuerySet):
    def update_or_create_chat_permissions(self, **kwargs) -> Optional["ChatPermissions"]:
        try:
            return self.update_or_create(**kwargs)[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None

    def update_chat_permissions(self, **kwargs) -> bool:
        try:
            return bool(
                self.update(**kwargs)
            )
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return False

    def filter_by_id(self, *, id: int) -> "ChatPermissionsQuerySet":
        return self.filter(id=id)


class ChatPermissionsManager(models.Manager):
    def get_queryset(self) -> ChatPermissionsQuerySet:
        return ChatPermissionsQuerySet(self.model, using=self._db)

    def update_or_create_chat_permissions_from_raw(
            self,
            *,
            raw_chat_permissions: types.ChatPermissions
    ) -> Optional["ChatPermissions"]:
        if raw_chat_permissions is None:
            return None
        parsed_object = self._parse(raw_chat_permissions)
        if parsed_object:
            return self.get_queryset().update_or_create_chat_permissions(
                **parsed_object
            )
        else:
            return None

    def update_chat_permissions_from_raw(
            self,
            *,
            id: int,
            raw_chat_permissions: types.ChatPermissions
    ):
        if id is None or raw_chat_permissions is None:
            return None
        parsed_object = self._parse(raw_chat_permissions)
        if not parsed_object:
            return None
        return self.get_queryset().filter_by_id(id=id).update_chat_permissions(
            **parsed_object
        )

    @staticmethod
    def _parse(chat_permissions: types.ChatPermissions) -> Optional[dict]:
        if chat_permissions is None:
            return None
        return {
            'can_send_messages': chat_permissions.can_send_messages,
            'can_send_media_messages': chat_permissions.can_send_media_messages,
            'can_send_stickers': chat_permissions.can_send_stickers,
            'can_send_animations': chat_permissions.can_send_animations,
            'can_send_games': chat_permissions.can_send_games,
            'can_use_inline_bots': chat_permissions.can_use_inline_bots,
            'can_add_web_page_previews': chat_permissions.can_add_web_page_previews,
            'can_send_polls': chat_permissions.can_send_polls,
            'can_invite_users': chat_permissions.can_invite_users,
            'can_pin_messages': chat_permissions.can_pin_messages,
            'until_date_ts': chat_permissions.until_date,
        }


class ChatPermissions(BaseModel):
    # True, if the user is allowed to send text messages, contacts, locations and venues.
    can_send_messages = models.BooleanField(null=True, blank=True, )
    # True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages.
    can_send_media_messages = models.BooleanField(null=True, blank=True, )
    # True, if the user is allowed to send stickers, implies can_send_media_messages.
    can_send_stickers = models.BooleanField(null=True, blank=True, )
    # True, if the user is allowed to send animations (GIFs), implies can_send_media_messages.
    can_send_animations = models.BooleanField(null=True, blank=True, )
    # True, if the user is allowed to send games, implies can_send_media_messages.
    can_send_games = models.BooleanField(null=True, blank=True, )
    # True, if the user is allowed to use inline bots_and_keyboards, implies can_send_media_messages.
    can_use_inline_bots = models.BooleanField(null=True, blank=True, )
    # True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages.
    can_add_web_page_previews = models.BooleanField(null=True, blank=True, )
    # True, if the user is allowed to send polls, implies can_send_messages.
    can_send_polls = models.BooleanField(null=True, blank=True, )
    # True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups.
    can_change_info = models.BooleanField(null=True, blank=True, )
    # True, if the user is allowed to invite new users to the chat.
    can_invite_users = models.BooleanField(null=True, blank=True, )
    # True, if the user is allowed to pin messages. Ignored in public supergroups.
    can_pin_messages = models.BooleanField(null=True, blank=True, )

    until_date_ts = models.BigIntegerField(null=True, blank=True, )

    objects = ChatPermissionsManager()

    ###########################################
    # `chat` : chat this permissions belongs to
    # `adminships` : adminship object this permissions belongs to
    # `action_banned_rights_prev` : Action this Rights is the previous banned rights of it
    # `action_banned_rights_new` : Action this Rights is the new banned rights of it
    # `participant` : Participant this rights belongs to

    class Meta:
        verbose_name_plural = 'Chat permissions'

    def update_fields_from_raw(self, *, raw_chat_permissions: types.ChatPermissions):
        self.objects.update_chat_permissions_from_raw(id=self.id, raw_chat_permissions=raw_chat_permissions)


