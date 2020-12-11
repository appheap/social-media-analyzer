from django.db import models
from ..base import BaseModel


class ChannelParticipantTypes(models.TextChoices):
    user = 'user'  # not member yet, only a telegram user (when banned/promoted before joining the channel)
    member = 'member'
    self = 'self'
    administrator = 'administrator'
    creator = 'creator'
    restricted = 'restricted'
    kicked = 'kicked'
    left = 'left'
    undefined = 'undefined'

    # @staticmethod
    # def get_type(participant: "ChannelParticipant"):
    #     for choice in ChannelParticipantTypes.choices:
    #         if choice[0] == participant.type:
    #             return getattr(ChannelParticipantTypes, str(choice[1]).lower())
    #     else:
    #         return ChannelParticipantTypes.undefined


class ChannelParticipant(BaseModel):
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
        choices=ChannelParticipantTypes.choices,
        default=ChannelParticipantTypes.undefined,
    )

    ### participant (user_id, join_date, demoted_by?, )
    # Date joined
    join_date = models.BigIntegerField(null=True, blank=True, )  # null for the creator

    #### participantSelf (user_id,inviter_id,join_date)

    #### participantCreator (user_id, rank)

    #### participantAdmin (user_id, join_date, promoted_by, can_edit, admin_rights, rank)
    # Can this admin promote other admins with the same permissions?
    can_edit = models.BooleanField(null=True, blank=True)  # only for admin participant
    # User that promoted the user to admin
    admin_rights = models.OneToOneField(
        'telegram.AdminRights',
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
    left = models.BooleanField(null=True, blank=True, )  # only for banned participant
    # Banned rights
    banned_rights = models.OneToOneField(
        'telegram.ChatPermissions',
        on_delete=models.CASCADE,
        related_name='participant',
        null=True, blank=True,
    )  # only for banned participant

    ### participantLeft (user_id, left_date, ?)
    left_date = models.BigIntegerField(null=True, blank=True, )

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
    event_date = models.BigIntegerField(null=True, blank=True, )
    is_previous = models.BooleanField(null=True, blank=True, )

    class Meta:
        ordering = ['-event_date', 'is_previous']

    def __str__(self):
        return f"participant {self.id} of type :{self.type}"
