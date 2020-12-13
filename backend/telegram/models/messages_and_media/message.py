from django.db import models
from ..base import BaseModel
from pyrogram import types


class ChatMediaTypes(models.TextChoices):
    photo = 'photo'
    video = 'video'
    document = 'document'
    music = 'music'
    url = 'url'
    voice = 'voice'
    webpage = 'webpage'
    game = 'game'
    invoice = 'invoice'
    video_note = 'video_note'
    animation = 'animation'
    poll = 'poll'
    dice = 'dice'
    sticker = 'sticker'
    location = 'location'
    live_location = 'live_location'
    contact = 'contact'
    undefined = 'undefined'

    @staticmethod
    def get_type(message: "types.Message"):
        if message.media_type is None:
            return ChatMediaTypes.undefined

        for choice in ChatMediaTypes.choices:
            if message.media_type == choice[0]:
                return getattr(ChatMediaTypes, str(choice[0]).lower())
        else:
            return ChatMediaTypes.undefined


class MessageTypes(models.TextChoices):
    message = 'message'
    service = 'service'
    empty = 'empty'
    undefined = 'undefined'


class Message(BaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:message_id`

    message_id = models.BigIntegerField()
    date = models.BigIntegerField()
    type = models.CharField(
        MessageTypes.choices,
        max_length=20,
        null=True, blank=True,
    )

    # conversation the message belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        related_name='messages',
        null=True, blank=True,
    )

    # info from message_normal
    edit_date = models.BigIntegerField(null=True, blank=True)
    is_outgoing = models.BooleanField(null=True, blank=True)
    mentioned = models.BooleanField(null=True, blank=True)
    is_silent = models.BooleanField(null=True, blank=True)
    is_post = models.BooleanField(null=True, blank=True)
    post_author = models.CharField(max_length=256, null=True, blank=True)
    from_scheduled = models.BooleanField(null=True, blank=True)
    edit_hide = models.BooleanField(null=True, blank=True)
    media_group_id = models.BigIntegerField(null=True, blank=True)
    from_chat = models.ForeignKey(
        'telegram.Chat',
        related_name='sent_messages',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    # Sender, null for messages sent to channels or sender user got deleted
    from_user = models.ForeignKey(
        'telegram.User',
        related_name='sent_messages',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    # info from forward_header
    forward_date = models.BigIntegerField(null=True, blank=True)
    # For messages forwarded from channels, original channel of the message.
    forward_from_chat = models.ForeignKey(
        'telegram.Chat',
        related_name='forwarded_messages',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    # For forwarded messages, sender of the original message
    forward_from_user = models.ForeignKey(
        'telegram.User',
        related_name='forwarded_messages',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    forward_sender_name = models.CharField(max_length=64, null=True, blank=True)
    forward_from_message_id_orig = models.BigIntegerField(null=True, blank=True)
    forward_from_message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        related_name='forwards',
        null=True,
        blank=True
    )
    forward_signature = models.CharField(max_length=256, null=True, blank=True)
    saved_from_chat = models.ForeignKey(
        'telegram.Chat',
        related_name='saved_messages',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    # For forwarded messages, sender of the original message
    saved_from_user = models.ForeignKey(
        'telegram.User',
        related_name='saved_messages',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    saved_from_message_id_orig = models.BigIntegerField(null=True, blank=True)
    # end of info from forward_header
    # The information of the bot that generated the message from an inline query of a user.
    via_bot = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='via_bot_messages',
    )
    text = models.TextField(max_length=4096, null=True, blank=True)
    media_type = models.CharField(
        ChatMediaTypes.choices,
        max_length=20,
        null=True, blank=True,
    )
    # info from reply_header
    reply_to_message_id_orig = models.BigIntegerField(null=True, blank=True)
    reply_to_message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        related_name='replies',
        null=True,
        blank=True
    )
    reply_to_user = models.ForeignKey(
        'telegram.User',
        related_name='message_replies',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    reply_to_chat = models.ForeignKey(
        'telegram.Chat',
        related_name='message_replies',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    reply_to_top_message_id_orig = models.BigIntegerField(null=True, blank=True)
    reply_to_top_message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        related_name='all_replies',
        null=True,
        blank=True
    )
    # end of info from reply_header

    delete_date = models.BigIntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=False, )

    has_media = models.BooleanField(default=False, null=False)

    ##########################################################
    # `all_replies` : replies to this message (whole thread)
    # `replies` : replies to this message
    # `forwards` : forwards of this message
    # `entities` : entities belonging to this message
    # `entity_types` : entity types in this message
    # `message_views` : views of this message during time
    # `actions_update_pinned` : actions were this message was pinned
    # `actions_edit_message_prev` : actions were this message was prev message of the action
    # `actions_edit_message_new` : actions were this message was new message of the action
    # `action_delete_message` : action were this message was deleted
    # `actions_stop_poll` : actions were this poll message was stopped
    # `new_message` : the new edited message if this message id an edited one
    # `restrictions` : restrictions of this message

    # Telegram account who logged this message
    logged_by = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='logged_messages',
    )

    class Meta:
        ordering = ('-date', 'chat',)
        get_latest_by = ('-date', 'chat',)

    def __str__(self):
        return f"message {self.message_id} from {self.chat}"
