from django.db import models

from ...base import BaseModel


class AdminLogEventActionDefaultBannedRights(BaseModel):
    """
    The default banned rights were modified
    """
    # Previous global banned rights
    prev_banned_rights = models.OneToOneField(
        'telegram.ChatPermissions',
        on_delete=models.CASCADE,
        related_name='action_banned_rights_prev',
        null=True, blank=True,
    )

    # New global banned rights.
    new_banned_rights = models.OneToOneField(
        'telegram.ChatPermissions',
        on_delete=models.CASCADE,
        related_name='action_banned_rights_new',
        null=True, blank=True,
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (default banned rights)'
