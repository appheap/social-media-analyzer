from django.db import models
from ..base import BaseModel


class ChatMediaTypes(models.TextChoices):
    photo = 'photo'
    video = 'video'
    document = 'document'
    music = 'music'
    url = 'url'
    voice = 'voice'
    video_note = 'video_note'
    animation = 'animation'
    location = 'location'
    contact = 'contact'
    undefined = 'undefined'

    @staticmethod
    def get_type(message: "PGMessage"):
        for choice in ChatMediaTypes.choices:
            if hasattr(message, choice[0]):
                return getattr(ChatMediaTypes, str(choice[0]).lower())
        else:
            return ChatMediaTypes.undefined


class Message(BaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:message_id`

    message_id = models.BigIntegerField()
    date = models.BigIntegerField()
    # conversation the message belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        related_name='messages',
        null=True, blank=True,
    )
    # Sender, null for messages sent to channels or sender user got deleted
    from_user = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        related_name='messages',
        null=True, blank=True,
    )
    # For forwarded messages, sender of the original message
    forward_from = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        related_name='forwarded_messages',
        null=True, blank=True,
    )
    forward_sender_name = models.CharField(max_length=64, null=True, blank=True)
    # For messages forwarded from channels, original channel of the message.
    forward_from_chat = models.ForeignKey(
        'telegram.Chat',
        related_name='forwarded_messages',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    forward_from_message_id = models.IntegerField(null=True, blank=True)
    forward_signature = models.CharField(max_length=256, null=True, blank=True)
    forward_date = models.BigIntegerField(null=True, blank=True)
    # For replies, the original message.
    reply_to_message = models.ForeignKey(
        'self',
        related_name='replies',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    mentioned = models.BooleanField(null=True, blank=True)
    empty = models.BooleanField(default=False, null=False, )
    edit_date = models.BigIntegerField(null=True, blank=True)
    media_group_id = models.BigIntegerField(null=True, blank=True)
    author_signature = models.CharField(max_length=256, null=True, blank=True)
    text = models.TextField(max_length=4096, null=True, blank=True)
    caption = models.TextField(max_length=1024, null=True, blank=True)
    # The information of the bot that generated the message from an inline query of a user.
    via_bot = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='via_bot_messages',
    )
    outgoing = models.BooleanField(null=True, blank=True)

    delete_date = models.BigIntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=False, )

    has_media = models.BooleanField(default=False, null=False)
    media_type = models.CharField(
        ChatMediaTypes.choices,
        max_length=20,
        null=True, blank=True,
    )

    # `replies` : replies to this message
    # `entities` : entities belonging to this message
    # `entity_types` : entity types in this message
    # `message_views` : views of this message during time
    # `actions_update_pinned` : actions were this message was pinned
    # `actions_edit_message_prev` : actions were this message was prev message of the action
    # `actions_edit_message_new` : actions were this message was new message of the action
    # `action_delete_message` : action were this message was deleted
    # `actions_stop_poll` : actions were this poll message was stopped
    # `new_message` : the new edited message if this message id an edited one

    # whether this message is an old (original of edited msg)
    # is_old_message = models.BooleanField(null=False, default=False, )
    # old_message = models.ForeignKey(
    #     'telegram.Message',
    #     null=True, blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='new_message'
    # )

    # Telegram account who logged this message
    logged_by = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='logged_messages',
    )

    class Meta:
        ordering = ('-date', 'chat',)
        get_latest_by = ('-date', 'chat',)

    def __str__(self):
        return f"message {self.message_id} from {self.chat}"
