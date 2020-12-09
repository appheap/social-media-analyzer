from django.db import models

from ..base import BaseModel


# todo: relation with chat?
class ChatBannedRight(BaseModel):
    """
    Represents the rights of a normal user in a supergroup/channel/chat.
    In this case, the flags are inverted: if set, a flag does not allow a user to do X.
    """

    # If set, does not allow a user to view messages in a supergroup/channel/chat
    can_view_messages = models.BooleanField()
    # If set, does not allow a user to send messages in a supergroup/chat
    can_send_messages = models.BooleanField()
    # If set, does not allow a user to send any media in a supergroup/chat
    can_send_media = models.BooleanField()
    # If set, does not allow a user to send stickers in a supergroup/chat
    can_send_stickers = models.BooleanField()
    # If set, does not allow a user to send gifs in a supergroup/chat
    can_send_gifs = models.BooleanField()
    # If set, does not allow a user to send games in a supergroup/chat/chat
    can_send_games = models.BooleanField()
    # If set, does not allow a user to use inline bots_and_keyboards in a supergroup/chat
    can_send_inline = models.BooleanField()
    # If set, does not allow a user to embed links in the messages of a supergroup/chat
    can_embed_links = models.BooleanField()
    # If set, does not allow a user to send stickers in a supergroup/chat
    can_send_polls = models.BooleanField()
    # If set, does not allow any user to change the description of a supergroup/chat
    can_change_info = models.BooleanField()
    # If set, does not allow any user to invite users in a supergroup/chat
    can_invite_users = models.BooleanField()
    # If set, does not allow any user to pin messages in a supergroup/chat
    can_pin_messages = models.BooleanField()
    # "Validity of said permissions (0 = forever, forever = 2^31-1 for now)."
    until_date = models.BigIntegerField(default=0)

    #################################################
    # `action_banned_rights_prev` : Action this Rights is the previous banned rights of it
    # `action_banned_rights_new` : Action this Rights is the new banned rights of it
    # `participant` : Participant this rights belongs to
