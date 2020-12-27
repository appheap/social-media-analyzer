from typing import Optional

from django.db import models, DatabaseError
from ..base import BaseModel
from pyrogram import types
from telegram.globals import logger


class ChatAdminRightsQuerySet(models.QuerySet):
    def update_or_create_admin_rights(self, **kwargs) -> Optional['ChatAdminRights']:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def update_admin_rights(self, **kwargs) -> bool:
        try:
            return bool(
                self.update(
                    **kwargs
                )
            )
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def filter_by_id(self, *, id: int) -> "ChatAdminRightsQuerySet":
        return self.filter(id=id)


class ChatAdminRightsManager(models.Manager):
    def get_queryset(self) -> ChatAdminRightsQuerySet:
        return ChatAdminRightsQuerySet(self.model, using=self._db)

    def update_or_create_from_raw(
            self,
            *,
            raw_admin_rights: types.ChatAdminRights,
    ) -> Optional['ChatAdminRights']:

        if raw_admin_rights is None:
            return None

        parsed_object = self._parse(raw_admin_rights=raw_admin_rights)
        if len(parsed_object):
            db_chat_admin_rights = self.get_queryset().update_or_create_admin_rights(
                **parsed_object
            )
            return db_chat_admin_rights

        return None

    def update_chat_admin_rights_from_raw(
            self,
            *,
            id: int,
            raw_chat_admin_rights: types.ChatAdminRights,
    ) -> bool:

        if id is None or raw_chat_admin_rights is None:
            return False

        parsed_object = self._parse(raw_admin_rights=raw_chat_admin_rights)
        if len(parsed_object):
            return self.get_queryset().filter_by_id(id=id).update_or_create_admin_rights(**parsed_object)

        return False

    @staticmethod
    def _parse(*, raw_admin_rights: types.ChatAdminRights) -> dict:
        if raw_admin_rights is None:
            return {}

        return {
            'can_change_info': raw_admin_rights.can_change_info,
            'can_post_messages': raw_admin_rights.can_post_messages,
            'can_edit_messages': raw_admin_rights.can_edit_messages,
            'can_delete_messages': raw_admin_rights.can_delete_messages,
            'can_ban_users': raw_admin_rights.can_ban_users,
            'can_invite_users': raw_admin_rights.can_invite_users,
            'can_pin_messages': raw_admin_rights.can_pin_messages,
            'can_add_admins': raw_admin_rights.can_add_admins,
            'is_anonymous': raw_admin_rights.is_anonymous,
        }


class ChatAdminRights(BaseModel):
    can_change_info = models.BooleanField(null=True, blank=True)
    can_post_messages = models.BooleanField(null=True, blank=True)
    can_edit_messages = models.BooleanField(null=True, blank=True)
    can_delete_messages = models.BooleanField(null=True, blank=True)
    can_ban_users = models.BooleanField(null=True, blank=True)
    can_invite_users = models.BooleanField(null=True, blank=True)
    can_pin_messages = models.BooleanField(null=True, blank=True)
    can_add_admins = models.BooleanField(null=True, blank=True)
    is_anonymous = models.BooleanField(null=True, blank=True)

    #################################################
    # `participant` : Participant this rights belongs to
    # `adminships` : adminship object this permissions belongs to

    objects = ChatAdminRightsManager()

    class Meta:
        verbose_name_plural = 'Admin Rights'

    # def has_changed(self, chat_participant: ChatParticipant):
    #     if not chat_participant:
    #         return True
    #
    #     if self.change_info != chat_participant.can_change_info or \
    #             self.post_messages != chat_participant.can_post_messages or \
    #             self.edit_messages != chat_participant.can_edit_messages or \
    #             self.delete_messages != chat_participant.can_delete_messages or \
    #             self.ban_users != chat_participant.can_restrict_members or \
    #             self.invite_users != chat_participant.can_invite_users or \
    #             self.pin_messages != chat_participant.can_pin_messages or \
    #             self.add_admins != chat_participant.can_promote_members:
    #         return True
    #     return False

    def update_fields_from_raw(self, *, raw_chat_admin_rights: types.ChatAdminRights):
        self.objects.update_chat_admin_rights_from_raw(id=self.id, raw_chat_admin_rights=raw_chat_admin_rights)

    def __str__(self):
        return str(
            f"{self.adminships.account if self.adminships else ''} @ {self.adminships.chat if self.adminships else ''}") if self.adminships else str(
            self.pk)
