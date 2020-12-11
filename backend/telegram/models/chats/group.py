from django.db import models
from ..base import BaseModel


class Group(BaseModel):
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

    ########################################################
    # `chat` : chat this channel belongs to
