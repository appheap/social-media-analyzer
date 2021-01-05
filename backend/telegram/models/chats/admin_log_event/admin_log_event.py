from typing import Optional, Tuple

from django.db import models, DatabaseError, transaction

from pyrogram import types
from telegram import models as tg_models
from telegram.globals import logger
from ...base import BaseModel


class AdminLogEventQuerySet(models.QuerySet):
    def update_or_create_event(self, **kwargs) -> Tuple[Optional['AdminLogEvent'], bool]:
        try:
            return self.update_or_create(
                **kwargs
            )
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None, False

    def create_event(self, **kwargs) -> Optional['AdminLogEvent']:
        try:
            return self.create(
                **kwargs
            )
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None

    def event_exists(self, *, event_id: int, chat_id: int) -> bool:
        return self.filter(id=f"{chat_id}:{event_id}").exists()

    def get_by_id(self, *, chat_id: int, event_id: int) -> Optional['AdminLogEvent']:
        try:
            return self.get(
                id=f"{chat_id}:{event_id}"
            )
        except AdminLogEvent.DoesNotExist as e:
            pass
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return None


class AdminLogEventManager(models.Manager):
    def get_queryset(self) -> AdminLogEventQuerySet:
        return AdminLogEventQuerySet(self.model, using=self._db)

    def admin_log_exists(
            self,
            *,
            event_id: int,
            chat_id: int,
    ) -> bool:
        return self.get_queryset().event_exists(
            event_id=event_id,
            chat_id=chat_id,
        )

    def update_or_create_from_raw(
            self,
            *,
            raw_admin_log_event: 'types.ChannelAdminLogEvent',
            db_user: 'tg_models.User',
            db_chat: 'tg_models.Chat',
            logged_by: 'tg_models.TelegramAccount',
    ) -> Optional['AdminLogEvent']:
        if raw_admin_log_event is None or db_user is None or db_chat is None or logged_by is None:
            return None

        parsed_object = self._parse(raw_event=raw_admin_log_event)
        if len(parsed_object):
            with transaction.atomic():
                db_event, created = self.get_queryset().update_or_create_event(
                    **{
                        'id': f'{db_chat.chat_id}:{raw_admin_log_event.event_id}',
                        'user': db_user,
                        'chat': db_chat,
                        'logged_by': logged_by,
                        **parsed_object
                    }
                )
                if db_event and created and raw_admin_log_event.action:
                    action = raw_admin_log_event.action

                    if isinstance(action, types.ChannelAdminLogEventActionChangeTitle):
                        db_action_title = tg_models.AdminLogEventActionChangeTitle.objects.update_or_create_action(
                            raw_action=action
                        )
                        db_event.action_change_title = db_action_title

                    elif isinstance(action, types.ChannelAdminLogEventActionChangeAbout):
                        db_action_about = tg_models.AdminLogEventActionChangeAbout.objects.update_or_create_action(
                            raw_action=action
                        )
                        db_event.action_change_about = db_action_about

                    elif isinstance(action, types.ChannelAdminLogEventActionChangeUsername):
                        db_action_username = tg_models.AdminLogEventActionChangeUsername.objects.update_or_create_action(
                            raw_action=action
                        )
                        db_event.action_change_username = db_action_username

                    elif isinstance(action, types.ChannelAdminLogEventActionChangePhoto):
                        db_action_photo = tg_models.AdminLogEventActionChangePhoto.objects.update_or_create_action(
                            raw_action=action
                        )
                        db_event.action_change_photo = db_action_photo

                    elif isinstance(action, types.ChannelAdminLogEventActionToggleInvites):
                        db_action_invites = tg_models.AdminLogEventActionToggleInvites.objects.update_or_create_action(
                            raw_action=action
                        )
                        db_event.action_toggle_invites = db_action_invites

                    elif isinstance(action, types.ChannelAdminLogEventActionToggleSignatures):
                        db_action_signatures = tg_models.AdminLogEventActionToggleSignatures.objects.update_or_create_action(
                            raw_action=action
                        )
                        db_event.action_toggle_signatures = db_action_signatures

                    elif isinstance(action, types.ChannelAdminLogEventActionUpdatePinned):
                        db_action_pinned = tg_models.AdminLogEventActionUpdatePinned.objects.update_or_create_action(
                            db_message=tg_models.Message.objects.update_or_create_from_raw(
                                chat_id=db_chat.chat_id,
                                raw_message=action.message,
                                logger_account=logged_by,
                            )
                        )
                        db_event.action_update_pinned = db_action_pinned

                    elif isinstance(action, types.ChannelAdminLogEventActionEditMessage):
                        db_action_edit_message = tg_models.AdminLogEventActionEditMessage.objects.update_or_create_action(
                            prev_db_message=tg_models.Message.objects.update_or_create_from_raw(
                                chat_id=db_chat.chat_id,
                                raw_message=action.prev_message,
                                logger_account=logged_by,
                            ),
                            new_db_message=tg_models.Message.objects.update_or_create_from_raw(
                                chat_id=db_chat.chat_id,
                                raw_message=action.new_message,
                                logger_account=logged_by,
                            )
                        )
                        db_event.action_edit_message = db_action_edit_message

                    elif isinstance(action, types.ChannelAdminLogEventActionDeleteMessage):
                        db_action_delete_message = tg_models.AdminLogEventActionDeleteMessage.objects.update_or_create_action(
                            db_message=tg_models.Message.objects.update_or_create_from_raw(
                                chat_id=db_chat.chat_id,
                                raw_message=action.message,
                                logger_account=logged_by,
                            )
                        )
                        db_event.action_delete_message = db_action_delete_message

                    elif isinstance(action, types.ChannelAdminLogEventActionParticipantJoin):
                        db_membership = tg_models.Membership.objects.get_membership_by_user_id(
                            db_chat=db_chat,
                            user_id=raw_admin_log_event.user.id,
                        )
                        raw_chat_member = types.ChatMember(
                            user=raw_admin_log_event.user,
                            join_date=raw_admin_log_event.date,
                            status='member',
                            is_current_user=raw_admin_log_event.user.is_self,
                        )

                        if db_membership:
                            db_chat_member = tg_models.ChatMember.objects.update_or_create_from_raw(
                                raw_chat_member=raw_chat_member,
                                db_membership=db_membership,
                                event_date_ts=raw_admin_log_event.date,
                            )
                            db_membership.update_membership_status(
                                new_status=db_chat_member,
                                event_date_ts=raw_admin_log_event.date,
                            )
                        else:
                            db_chat_member = tg_models.ChatMember.objects.update_or_create_from_raw(
                                raw_chat_member=raw_chat_member,
                                db_membership=None,
                                event_date_ts=raw_admin_log_event.date,
                            )
                            db_membership = tg_models.Membership.objects.update_or_create_membership(
                                db_user=db_chat_member.user,
                                db_chat=db_chat,
                                new_status=db_chat_member,
                                event_date_ts=raw_admin_log_event.date
                            )
                            db_chat_member.update_fields(
                                **{
                                    'membership': db_membership,
                                }
                            )
                        db_event.action_participant_join = tg_models.AdminLogEventActionParticipantJoin.objects.update_or_create()

                    elif isinstance(action, types.ChannelAdminLogEventActionParticipantLeave):
                        db_membership = tg_models.Membership.objects.get_membership_by_user_id(
                            db_chat=db_chat,
                            user_id=raw_admin_log_event.user.id,
                        )
                        raw_chat_member = types.ChatMember(
                            user=raw_admin_log_event.user,
                            status='left',
                            is_current_user=raw_admin_log_event.user.is_self,
                        )

                        if db_membership:
                            db_chat_member = tg_models.ChatMember.objects.update_or_create_from_raw(
                                raw_chat_member=raw_chat_member,
                                db_membership=db_membership,
                                event_date_ts=raw_admin_log_event.date,
                                left_date_ts=raw_admin_log_event.date,
                            )
                            db_membership.update_membership_status(
                                new_status=db_chat_member,
                                event_date_ts=raw_admin_log_event.date,
                            )
                        else:
                            db_chat_member = tg_models.ChatMember.objects.update_or_create_from_raw(
                                raw_chat_member=raw_chat_member,
                                db_membership=None,
                                event_date_ts=raw_admin_log_event.date,
                                left_date_ts=raw_admin_log_event.date,
                            )
                            db_membership = tg_models.Membership.objects.update_or_create_membership(
                                db_user=db_chat_member.user,
                                db_chat=db_chat,
                                new_status=db_chat_member,
                                event_date_ts=raw_admin_log_event.date
                            )
                            db_chat_member.update_fields(
                                **{
                                    'membership': db_membership,
                                }
                            )

                        db_event.action_participant_leave = tg_models.AdminLogEventActionParticipantLeave.objects.update_or_create()

                    elif isinstance(action, types.ChannelAdminLogEventActionParticipantInvite):
                        db_chat_member = self._parse_chat_member(
                            raw_chat_member=action.chat_member,
                            db_chat=db_chat,
                            db_user=db_user,
                            raw_admin_log_event=raw_admin_log_event,
                        )

                        db_action_participant_invite = tg_models.AdminLogEventActionParticipantInvite.objects.update_or_create_action(
                            db_chat_member=db_chat_member,
                        )
                        db_event.action_participant_invite = db_action_participant_invite

                    elif isinstance(action, types.ChannelAdminLogEventActionParticipantToggleBan):
                        db_prev_chat_member = self._parse_chat_member(
                            raw_chat_member=action.prev_chat_member,
                            db_chat=db_chat,
                            db_user=db_user,
                            raw_admin_log_event=raw_admin_log_event,
                            toggle_ban=True,
                            is_previous=True,
                        )

                        db_new_chat_member = self._parse_chat_member(
                            raw_chat_member=action.new_chat_member,
                            db_chat=db_chat,
                            db_user=db_user,
                            raw_admin_log_event=raw_admin_log_event,
                            toggle_ban=True,
                            is_previous=False,
                        )

                        db_action_toggle_ban = tg_models.AdminLogEventActionToggleBan.objects.update_or_create_action(
                            db_prev_chat_member=db_prev_chat_member,
                            db_new_chat_member=db_new_chat_member,
                        )
                        db_event.action_participant_toggle_ban = db_action_toggle_ban

                    elif isinstance(action, types.ChannelAdminLogEventActionParticipantToggleAdmin):
                        promoted = None,
                        demoted = None
                        if action.prev_chat_member.status != action.new_chat_member.status:
                            if action.new_chat_member.status in ('member', 'user', 'restricted', 'kicked'):
                                demoted = True
                            elif action.new_chat_member.status in ('administrator', 'creator'):
                                promoted = True
                        else:
                            promoted = True

                        db_prev_chat_member = self._parse_chat_member(
                            raw_chat_member=action.prev_chat_member,
                            db_chat=db_chat,
                            db_user=db_user,
                            raw_admin_log_event=raw_admin_log_event,
                            is_previous=True,
                            promoted=promoted,
                            demoted=demoted,
                        )

                        db_new_chat_member = self._parse_chat_member(
                            raw_chat_member=action.new_chat_member,
                            db_chat=db_chat,
                            db_user=db_user,
                            raw_admin_log_event=raw_admin_log_event,
                            is_previous=False,
                            promoted=promoted,
                            demoted=demoted,
                        )

                        db_action_toggle_admin = tg_models.AdminLogEventActionToggleAdmin.objects.update_or_create_action(
                            db_prev_chat_member=db_prev_chat_member,
                            db_new_chat_member=db_new_chat_member,
                        )
                        db_event.action_participant_toggle_admin = db_action_toggle_admin

                    elif isinstance(action, types.ChannelAdminLogEventActionChangeStickerSet):
                        db_event.action_change_sticker_set = tg_models.AdminLogEventActionChangeStickerSet.objects.update_or_create()

                    elif isinstance(action, types.ChannelAdminLogEventActionTogglePreHistoryHidden):
                        db_event.action_toggle_prehistory_hidden = tg_models.AdminLogEventActionTogglePreHistoryHidden.objects.update_or_create_action(
                            raw_action=action
                        )

                    elif isinstance(action, types.ChannelAdminLogEventActionDefaultBannedRights):
                        db_action_default_banned_rights = tg_models.AdminLogEventActionDefaultBannedRights.objects.update_or_create_action(
                            prev_banned_rights=tg_models.ChatPermissions.objects.update_or_create_chat_permissions_from_raw(
                                raw_chat_permissions=action.prev_banned_rights
                            ),
                            new_banned_rights=tg_models.ChatPermissions.objects.update_or_create_chat_permissions_from_raw(
                                raw_chat_permissions=action.new_banned_rights
                            )
                        )
                        db_event.action_default_banned_rights = db_action_default_banned_rights

                    elif isinstance(action, types.ChannelAdminLogEventActionUpdatePinned):
                        db_action_stop_poll = tg_models.AdminLogEventActionStopPoll.objects.update_or_create_action(
                            db_message=tg_models.Message.objects.update_or_create_from_raw(
                                chat_id=db_chat.chat_id,
                                raw_message=action.message,
                                logger_account=logged_by,
                            )
                        )
                        db_event.action_stop_poll = db_action_stop_poll

                    elif isinstance(action, types.ChannelAdminLogEventActionChangeLinkedChat):
                        db_action_change_linked_chat = tg_models.AdminLogEventActionChangeLinkedChat.objects.update_or_create_action(
                            raw_action=action
                        )
                        db_event.action_change_linked_chat = db_action_change_linked_chat

                    elif isinstance(action, types.ChannelAdminLogEventActionChangeLocation):
                        db_action_change_location = tg_models.AdminLogEventActionChangeLocation.objects.update_or_create_action(
                            raw_action=action
                        )
                        db_event.action_change_location = db_action_change_location

                    elif isinstance(action, types.ChannelAdminLogEventActionToggleSlowMode):
                        db_action_toggle_slow_mode = tg_models.AdminLogEventActionToggleSlowMode.objects.update_or_create_action(
                            raw_action=action
                        )
                        db_event.action_toggle_slow_mode = db_action_toggle_slow_mode

                    db_event.save()

                return db_event

        return None

    @staticmethod
    def _parse_chat_member(
            *,
            raw_chat_member: 'types.ChatMember',
            db_chat: 'tg_models.ChatMember',
            db_user: 'tg_models.User',
            raw_admin_log_event: 'types.ChannelAdminLogEvent',
            invited: bool = False,
            toggle_ban: bool = False,
            promoted: bool = False,
            demoted: bool = False,

            is_previous: bool = None,

    ) -> 'tg_models.ChatMember':

        db_membership = tg_models.Membership.objects.get_membership_by_user_id(
            db_chat=db_chat,
            user_id=raw_admin_log_event.user.id,
        )
        invited_by = db_user if invited else None
        demoted_by = db_user if demoted else None
        promoted_by = db_user if promoted else None
        kicked_by = db_user if toggle_ban else None

        if invited_by is None and demoted_by is None and promoted_by is None and kicked_by is None:
            raise ValueError(f'wrong value: at least one must be true')

        if db_membership:
            db_chat_member = tg_models.ChatMember.objects.update_or_create_from_raw(
                raw_chat_member=raw_chat_member,
                db_membership=db_membership,
                event_date_ts=raw_admin_log_event.date,
                invited_by=invited_by,
                demoted_by=demoted_by,
                kicked_by=kicked_by,
                promoted_by=promoted_by,
                is_previous=is_previous
            )
            db_membership.update_membership_status(
                new_status=db_chat_member,
                event_date_ts=raw_admin_log_event.date,
            )
        else:
            db_chat_member = tg_models.ChatMember.objects.update_or_create_from_raw(
                raw_chat_member=raw_chat_member,
                db_membership=None,
                event_date_ts=raw_admin_log_event.date,
                invited_by=invited_by,
                demoted_by=demoted_by,
                kicked_by=kicked_by,
                promoted_by=promoted_by,
                is_previous=is_previous,
            )
            db_membership = tg_models.Membership.objects.update_or_create_membership(
                db_user=db_chat_member.user,
                db_chat=db_chat,
                new_status=db_chat_member,
                event_date_ts=raw_admin_log_event.date
            )
            db_chat_member.update_fields(
                **{
                    'membership': db_membership,
                }
            )
        return db_chat_member

    @staticmethod
    def _parse(*, raw_event: 'types.ChannelAdminLogEvent'):
        if raw_event is None:
            return {}

        return {
            'event_id': raw_event.event_id,
            'date': raw_event.date,
        }


class AdminLogEvent(BaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat__chat_id:event_id`

    event_id = models.BigIntegerField()
    date = models.BigIntegerField()
    user = models.ForeignKey(
        'telegram.User',
        null=False,
        on_delete=models.CASCADE,
        related_name='admin_log_events',
    )

    # Chat this Event belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='admin_log_events',
    )

    # Telegram account that logged this event
    logged_by = models.ForeignKey(
        'telegram.TelegramAccount',
        null=False,
        on_delete=models.CASCADE,
        related_name="admin_log_events",
    )

    # Channel/supergroup title was changed
    action_change_title = models.OneToOneField(
        'telegram.AdminLogEventActionChangeTitle',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # The description was changed
    action_change_about = models.OneToOneField(
        'telegram.AdminLogEventActionChangeAbout',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )
    # Channel/supergroup username was changed
    action_change_username = models.OneToOneField(
        'telegram.AdminLogEventActionChangeUsername',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # The channel/supergroup's picture was changed
    action_change_photo = models.OneToOneField(
        'telegram.AdminLogEventActionChangePhoto',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # Invites were enabled/disabled
    action_toggle_invites = models.OneToOneField(
        'telegram.AdminLogEventActionToggleInvites',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # Channel signatures were enabled/disabled
    action_toggle_signatures = models.OneToOneField(
        'telegram.AdminLogEventActionToggleSignatures',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # A message was pinned
    action_update_pinned = models.OneToOneField(
        'telegram.AdminLogEventActionUpdatePinned',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # A message was deleted
    action_edit_message = models.OneToOneField(
        'telegram.AdminLogEventActionEditMessage',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # A message was deleted
    action_delete_message = models.OneToOneField(
        'telegram.AdminLogEventActionDeleteMessage',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # A user has joined the group (in the case of big groups, info of the user that has joined isn't shown)
    action_participant_join = models.OneToOneField(
        'telegram.AdminLogEventActionParticipantJoin',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # A user left the channel/supergroup (in the case of big groups, info of the user that has joined isn't shown)
    action_participant_leave = models.OneToOneField(
        'telegram.AdminLogEventActionParticipantLeave',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # A user was invited to the group
    action_participant_invite = models.OneToOneField(
        'telegram.AdminLogEventActionParticipantInvite',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # The banned rights of a user were changed
    action_participant_toggle_ban = models.OneToOneField(
        'telegram.AdminLogEventActionToggleBan',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # The admin rights of a user were changed
    action_participant_toggle_admin = models.OneToOneField(
        'telegram.AdminLogEventActionToggleAdmin',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # The supergroup's stickerset was changed
    action_change_sticker_set = models.OneToOneField(
        'telegram.AdminLogEventActionChangeStickerSet',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # The hidden prehistory setting was changed
    action_toggle_prehistory_hidden = models.OneToOneField(
        'telegram.AdminLogEventActionTogglePreHistoryHidden',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # The default banned rights were modified
    action_default_banned_rights = models.OneToOneField(
        'telegram.AdminLogEventActionDefaultBannedRights',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # A poll was stopped
    action_stop_poll = models.OneToOneField(
        'telegram.AdminLogEventActionStopPoll',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # The linked chat was changed
    action_change_linked_chat = models.OneToOneField(
        'telegram.AdminLogEventActionChangeLinkedChat',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # The geogroup location was changed
    action_change_location = models.OneToOneField(
        'telegram.AdminLogEventActionChangeLocation',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    # Slow mode setting for supergroups was changed
    action_toggle_slow_mode = models.OneToOneField(
        'telegram.AdminLogEventActionToggleSlowMode',
        on_delete=models.CASCADE,
        related_name='admin_log_event',
        null=True, blank=True,
    )

    objects = AdminLogEventManager()

    #############################################
    def get_event_description(self):
        desc = ""
        if self.action_change_title:
            desc = f"changed title of {self.chat} from {self.action_change_title.prev_value} to {self.action_change_title.new_value}"
        elif self.action_change_about:
            desc = f"changed description of {self.chat} from {self.action_change_about.prev_value} to {self.action_change_about.new_value}"
        elif self.action_change_username:
            desc = f"changed username of {self.chat} from {self.action_change_username.prev_value} to {self.action_change_username.new_value}"
        elif self.action_change_photo:
            desc = f"changed photo of {self.chat}"
        elif self.action_toggle_invites:
            desc = f"changed invites of {self.chat} to {self.action_toggle_invites.new_value}"
        elif self.action_toggle_signatures:
            desc = f"changed signature of {self.chat} to {self.action_toggle_signatures.new_value}"
        elif self.action_update_pinned:
            desc = f"pinned {self.action_update_pinned.message} on {self.chat}"
        elif self.action_edit_message:
            desc = f"edited a message from {self.action_edit_message.prev_message} to {self.action_edit_message.new_message}"
        elif self.action_delete_message:
            desc = f"deleted {self.action_delete_message.message}"
        elif self.action_participant_join:
            desc = f"joined chat {self.chat}"
        elif self.action_participant_invite:
            desc = f"invited {self.action_participant_invite.participant.user} to chat {self.chat}"
        elif self.action_participant_toggle_ban:
            desc = f"banned {self.action_participant_toggle_ban.new_participant.user} in chat {self.chat}"
        elif self.action_participant_toggle_admin:
            desc = f"promoted/demoted {self.action_participant_toggle_admin.new_participant.user} in chat {self.chat}"

        return desc

    #############################################

    class Meta:
        verbose_name_plural = 'Admin Log Events'
        ordering = ['chat', '-date']
        get_latest_by = ['chat', '-date']

    def __str__(self):
        return f"{self.user} @ {self.date} {self.get_event_description()}"
