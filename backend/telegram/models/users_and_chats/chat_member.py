from typing import Optional

from django.db import models, DatabaseError, transaction
from ..base import BaseModel
from telegram.globals import logger
from pyrogram import types
from telegram import models as tg_models
from ..users import UserUpdater
from ..chats import ChatPermissionsUpdater
from ..chats import ChatAdminRightsUpdater


class ChatMemberTypes(models.TextChoices):
    user = 'user'  # not member yet, only a telegram user (when banned/promoted before joining the channel)
    member = 'member'
    administrator = 'administrator'
    creator = 'creator'
    restricted = 'restricted'
    kicked = 'kicked'
    left = 'left'
    undefined = 'undefined'

    @staticmethod
    def get_type(participant: "types.ChatMember"):
        for choice in ChatMemberTypes.choices:
            if choice[0] == participant.status:
                _type = getattr(ChatMemberTypes, str(choice[1]).lower())
        else:
            _type = ChatMemberTypes.undefined
        return _type


class ChatMemberQuerySet(models.QuerySet):
    def update_or_create_chat_member(
            self,
            **kwargs
    ) -> Optional['ChatMember']:

        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None


class ChatMemberManager(models.Manager):
    def get_queryset(self) -> ChatMemberQuerySet:
        return ChatMemberQuerySet(self.model, using=self._db)

    def update_or_create_from_raw(
            self,
            *,
            raw_chat_member: types.ChatMember,
            db_membership: 'tg_models.Membership',

            event_date_ts: int = None,
            left_date_ts: int = None,
            is_previous: bool = None,

            promoted_by: 'tg_models.User' = None,
            demoted_by: 'tg_models.User' = None,
            kicked_by: 'tg_models.User' = None,
            invited_by: 'tg_models.User' = None,

    ) -> Optional['ChatMember']:

        if raw_chat_member is None or db_membership is None:
            return None

        parsed_object = self._parse(raw_chat_member=raw_chat_member)
        if len(parsed_object):
            if left_date_ts is not None and event_date_ts is not None:
                parsed_object['type'] = ChatMemberTypes.left

            with transaction.atomic():
                db_chat_member = self.get_queryset().update_or_create_chat_member(
                    **{
                        **parsed_object,
                        'membership': db_membership,
                        'event_date_ts': event_date_ts,
                        'left_date_ts': left_date_ts,
                        'is_previous': is_previous,
                    }
                )
                if db_chat_member:
                    db_chat_member.update_or_create_user_from_raw(
                        model=db_chat_member,
                        field_name='promoted_by',
                        raw_user=promoted_by,
                    )
                    db_chat_member.update_or_create_user_from_raw(
                        model=db_chat_member,
                        field_name='demoted_by',
                        raw_user=demoted_by,
                    )
                    db_chat_member.update_or_create_user_from_raw(
                        model=db_chat_member,
                        field_name='kicked_by',
                        raw_user=kicked_by,
                    )
                    db_chat_member.update_or_create_user_from_raw(
                        model=db_chat_member,
                        field_name='invited_by',
                        raw_user=invited_by,
                    )

                    db_chat_member.update_or_create_chat_permissions_from_raw(
                        model=db_chat_member,
                        field_name='banned_rights',
                        raw_chat_permissions=raw_chat_member.banned_rights
                    )

                    db_chat_member.update_or_create_chat_admin_rights_from_raw(
                        model=db_chat_member,
                        field_name='admin_rights',
                        raw_chat_admin_rights=raw_chat_member.admin_rights
                    )

            return db_chat_member

        return None

    @staticmethod
    def _parse(*, raw_chat_member: types.ChatMember):
        if raw_chat_member is None:
            return {}

        return {
            'type': ChatMemberTypes.get_type(raw_chat_member),
            'join_date_ts': raw_chat_member.join_date,
            'can_promote_admins': raw_chat_member.can_promote_admins,
            'rank': raw_chat_member.status,
            'has_left': raw_chat_member.has_left,
        }


class ChatMember(BaseModel, UserUpdater, ChatPermissionsUpdater, ChatAdminRightsUpdater):
    """
        Channel/supergroup participant
    """
    user = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        related_name='+',
    )

    type = models.CharField(
        max_length=64,
        null=False,
        choices=ChatMemberTypes.choices,
        default=ChatMemberTypes.undefined,
    )

    ### participant (user_id, join_date, demoted_by?, )
    # Date joined
    join_date_ts = models.BigIntegerField(null=True, blank=True, )  # null for the creator

    #### participantSelf (user_id,inviter_id,join_date)

    #### participantCreator (user_id, rank)

    #### participantAdmin (user_id, join_date, promoted_by, can_edit, admin_rights, rank)
    # Can this admin promote other admins with the same permissions?
    can_promote_admins = models.BooleanField(null=True, blank=True)  # only for admin participant
    # User that promoted the user to admin
    admin_rights = models.OneToOneField(
        'telegram.ChatAdminRights',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='participant',
    )  # only for admin participant
    rank = models.CharField(
        max_length=256,
        null=True, blank=True,
    )  # only for creator and admin

    #### participantBanned (user_id, join_date, inviter_id, left, kicked_by, banned_rights, )
    # Whether the user has left the group
    has_left = models.BooleanField(null=True, blank=True, )  # only for banned participant
    # Banned rights
    banned_rights = models.OneToOneField(
        'telegram.ChatPermissions',
        on_delete=models.CASCADE,
        related_name='participant',
        null=True, blank=True,
    )  # only for banned participant

    ### participantLeft (user_id, left_date, ?)
    left_date_ts = models.BigIntegerField(null=True, blank=True, )

    #################################################
    # `action_participant_invite` : Action that this participant is the invited participant
    # `action_toggle_ban_prev' : Action that this participant is the prev participant of the action
    # `action_toggle_ban_new' : Action that this participant is the new participant of the action
    # `action_toggle_admin_prev` : Action that this participant was the the prev participant
    # `action_toggle_admin_new` : Action that this participant was the the new participant

    membership = models.ForeignKey(
        'telegram.Membership',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='participant_history'
    )

    invited_by = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='invited_participants',
    )
    promoted_by = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='promoted_participants',
    )
    demoted_by = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='demoted_participants',
    )
    kicked_by = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='kicked_participants',
    )

    # the time of event happened to this participant (from adminLogs)
    event_date_ts = models.BigIntegerField(null=True, blank=True, )
    is_previous = models.BooleanField(null=True, blank=True, )

    objects = ChatMemberManager()

    class Meta:
        ordering = ['-event_date_ts', 'is_previous']

    def __str__(self):
        return f"participant {self.id} of type :{self.type}"
