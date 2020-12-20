from django.db import models
from ..base import BaseModel
from pyrogram import types
from typing import Optional, Union
from django.db import DatabaseError
from telegram.globals import logger
from telegram import models as tg_models


class GroupQuerySet(models.QuerySet):
    def update_or_create_group(self, **kwargs) -> Optional["Group"]:
        try:
            return self.update_or_create(**kwargs)[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None

    def get_group_by_id(self, *, group_id: int) -> Optional["Group"]:
        try:
            return self.get(id=group_id)
        except Group.DoesNotExist as e:
            return None
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None

    def filter_by_id(self, *, id: int) -> "GroupQuerySet":
        return self.filter(id=id)


class GroupManager(models.Manager):
    def get_queryset(self) -> GroupQuerySet:
        return GroupQuerySet(self.model, using=self._db)

    def get_group_by_id(self, group_id: int) -> Optional["Group"]:
        return self.get_queryset().get_group_by_id(group_id=group_id)

    def update_from_raw(
            self,
            *,
            id: int,
            raw_chat: types.Chat,
    ) -> bool:
        if raw_chat is None:
            return False

        updated = False
        parsed_full_group = self._parse_full_group(group=raw_chat.full_group)
        parsed_group = self._parse_group(group=raw_chat.group)
        if not parsed_full_group and not parsed_group:
            return None
        group_qs = self.get_queryset().filter_by_id(id=id)
        updated = bool(
            group_qs.update(
                **{
                    **parsed_full_group,
                    **parsed_group,
                }
            )
        )
        if updated:
            db_group = group_qs[0]
            if db_group:
                db_group.update_or_create_chat_permissions_from_raw(
                    model=db_group,
                    field_name='default_banned_rights',
                    raw_chat_permissions=raw_chat.group.default_banned_rights
                )

        return updated

    def update_or_create_group_from_raw(
            self,
            *,
            full_group: types.GroupFull,
            group: types.Group,
            creator: tg_models.User = None
    ) -> Optional["Group"]:
        if full_group is None and group is None:
            return None

        parsed_full_group = self._parse_full_group(group=full_group)
        parsed_group = self._parse_group(group=group)
        if not parsed_full_group and not parsed_group:
            return None
        db_group = self.get_queryset().update_or_create_group(
            **{
                **parsed_full_group,
                **parsed_group,
                'creator': creator
            }
        )
        if db_group:
            db_group.update_or_create_chat_permissions_from_raw(
                model=db_group,
                field_name='default_banned_rights',
                raw_chat_permissions=group.default_banned_rights
            )

        return db_group

    @staticmethod
    def _parse_group(*, group: types.Group) -> Optional[dict]:
        if group is None:
            return {}
        return {
            'id': group.id,
            'title': group.title,
            'is_empty': group.is_empty,
            'is_deactivated': group.is_deactivated,
            'members_count': group.members_count,
            'create_date_ts': group.create_date,
        }

    @staticmethod
    def _parse_full_group(*, group: types.GroupFull) -> Optional[dict]:
        if group is None:
            return {}
        return {
            'can_set_username': group.can_set_username,
            'about': group.about,
            'invite_link': group.invite_link,
        }


class Group(BaseModel, tg_models.ChatPermissionsUpdater):
    id = models.BigIntegerField(primary_key=True)

    # info from full_group
    can_set_username = models.BooleanField(null=True, blank=True)
    about = models.TextField(max_length=1024, null=True, blank=True, )
    invite_link = models.CharField(max_length=256, null=True, blank=True, )

    # info from group
    title = models.CharField(max_length=256, null=True, blank=True, )
    is_empty = models.BooleanField(null=True, blank=True, )
    is_deactivated = models.BooleanField(null=True, blank=True, )
    members_count = models.IntegerField(null=True, blank=True, )
    create_date_ts = models.BigIntegerField(null=True, blank=True, )
    creator = models.ForeignKey(
        'telegram.User',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='created_groups',
    )
    default_banned_rights = models.OneToOneField(
        'telegram.ChatPermissions',
        models.CASCADE,
        null=True,
        blank=True,
        related_name='group'
    )
    # `migrated_to`
    # `admin_rights`

    objects = GroupManager()

    ########################################################
    # `chat` : chat this channel belongs to

    def update_fields_from_raw_chat(self, *, raw_chat: types.Chat) -> bool:
        if not raw_chat:
            return False
        return self.objects.update_from_raw_chat(
            id=self.id,
            raw_chat=raw_chat
        )
