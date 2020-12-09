from django.db import models
from ..base import BaseModel


class AdminRights(BaseModel):
    change_info = models.BooleanField(null=True, blank=True)
    post_messages = models.BooleanField(null=True, blank=True)
    edit_messages = models.BooleanField(null=True, blank=True)
    delete_messages = models.BooleanField(null=True, blank=True)
    ban_users = models.BooleanField(null=True, blank=True)
    invite_users = models.BooleanField(null=True, blank=True)
    pin_messages = models.BooleanField(null=True, blank=True)
    add_admins = models.BooleanField(null=True, blank=True)

    # channel this rights belongs to
    telegram_channel = models.ForeignKey(
        'telegram.TelegramChannel',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='telegram channel',
        related_name='admin_rights',
    )

    # admin this rights belongs to
    admin = models.ForeignKey(
        'telegram.TelegramAccount',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='admin',
        related_name='admin_rights',
    )

    # whether this rights are the latest stored
    is_latest = models.BooleanField(null=False, default=False, )

    #################################################
    # `participant` : Participant this rights belongs to

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

    def __str__(self):
        return str(
            f"{self.admin if self.admin else ''} @ {self.telegram_channel if self.telegram_channel else ''}{' : current' if self.is_latest else ''}") if self.admin and self.telegram_channel else str(
            self.pk)
