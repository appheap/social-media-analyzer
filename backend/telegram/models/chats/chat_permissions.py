from django.db import models

from ..base import BaseModel


class ChatPermissions(BaseModel):
    id = models.CharField(max_length=256, primary_key=True, )  # `chat_id`

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

    ###########################################
    # `chat` : chat this permissions belongs to
    # `adminships` : adminship object this permissions belongs to
    # `action_banned_rights_prev` : Action this Rights is the previous banned rights of it
    # `action_banned_rights_new` : Action this Rights is the new banned rights of it
    # `participant` : Participant this rights belongs to

    class Meta:
        verbose_name_plural = 'Chat permissions'
        ordering = ('-modified_at', '-created_at')
        get_latest_by = ('-modified_at', '-created_at')
