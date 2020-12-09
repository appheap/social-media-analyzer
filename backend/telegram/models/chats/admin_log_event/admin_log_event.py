from django.db import models
from ...base import BaseModel


class AdminLogEvent(BaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:event_id`

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
