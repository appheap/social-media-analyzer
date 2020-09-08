import arrow
from django.db import models
from users import models as users_models


# Create your models here.


################################################
# models used as proxy to control access,etc to the objects they refer to
class TelegramAccount(models.Model):
    user_id = models.BigIntegerField()
    username = models.CharField(max_length=32, null=True)
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    is_bot = models.BooleanField(default=False)
    is_restricted = models.BooleanField(default=False)
    is_scam = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=True)
    dc_id = models.IntegerField(null=True)
    language_code = models.CharField(max_length=5, null=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.BigIntegerField(null=True)
    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()

    # `telegram_channels` : telegram channels added by this account
    # `admin_logs` : admin logs logged by this account
    # `message_views` : message views logged by this account
    # `member_count_history` : member counts logged by this account
    # `shared_media_history` : shared media counts logged by this account

    # User who is the owner of this telegram account
    custom_user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name='telegram_accounts',
        null=True,
    )

    # Telegram User this account belongs to
    telegram_user = models.ForeignKey(
        'telegram.User',
        related_name='telegram_accounts',
        null=True,
        on_delete=models.SET_NULL,
    )

    # the blockage object
    blockage = models.OneToOneField(
        'users.Blockage',
        on_delete=models.SET_NULL,
        null=True,
        related_name='telegram_account',
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(TelegramAccount, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class TelegramChannel(models.Model):
    channel_id = models.BigIntegerField()
    is_account_creator = models.BooleanField(null=True)
    is_account_admin = models.BooleanField(null=True)

    is_public = models.BooleanField(default=False, null=True)
    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.BigIntegerField(null=True)

    # telegram account which added this channel
    telegram_account = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        related_name='telegram_channels',
        null=False,
    )
    # Telegram Chat this channel belongs to
    telegram_chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.SET_NULL,
        null=True,
        related_name='telegram_channels',
    )
    # the blockage object
    blockage = models.OneToOneField(
        'users.Blockage',
        on_delete=models.SET_NULL,
        null=True,
        related_name='telegram_channel',
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(TelegramChannel, self).save(*args, **kwargs)

    def __str__(self):
        return self.channel_id


################################################
# the models used to implement telegram functionality

class ChatMediaTypes(models.TextChoices):
    PHOTO = 'photo'
    VIDEO = 'video'
    DOCUMENT = 'document'
    MUSIC = 'music'
    URL = 'url',
    VOICE = 'voice',
    VIDEO_NOTE = 'video_note',
    ANIMATION = 'animation',
    LOCATION = 'location',
    CONTACT = 'contact',


class EntitySourceTypes(models.TextChoices):
    TEXT = "text"
    CAPTION = "caption"


class EntityTypes(models.TextChoices):
    MENTION = 'mention'
    HASHTAG = 'hashtag'
    CASHTAG = 'cashtag'
    BOT_COMMAND = 'bot_command'
    URL = 'url'
    EMAIL = 'email'
    PHONE_NUMBER = 'phone_number'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    PRE = 'pre'
    TEXT_LINK = 'text_link'
    TEXT_MENTION = 'text_mention'


class User(models.Model):
    user_id = models.BigIntegerField()
    is_deleted = models.BooleanField(null=True)
    is_bot = models.BooleanField(null=True)
    is_verified = models.BooleanField(null=True)
    is_restricted = models.BooleanField(null=True)
    is_spam = models.BooleanField(null=True)
    is_support = models.BooleanField(null=True)
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    username = models.CharField(max_length=32, null=True)
    language_code = models.CharField(max_length=20, null=True)
    dc_id = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=20, null=True)

    ##############################################################
    deleted_at = models.BigIntegerField(null=True)

    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()

    # `telegram_accounts` : telegram accounts connected to this user
    # `restrictions` : restrictions of this user if it's a bot
    # `admin_log_mentions` : admin logs this user is mentioned in
    # `forwarded_messages` : forwarded messages from this user
    # `messages` : messages belonging to this user in a chat
    # `via_bot_messages` : messages (inline queries) that were generated by this bot in a chat
    # `mentioned_entities` : entities that this user is mentioned in
    #

    # chat_ref = models.ManyToManyField(
    #     'telegram.Chat',
    #     related_name='users',
    # )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Chat(models.Model):
    chat_id = models.BigIntegerField()
    type = models.CharField(
        users_models.ChatTypes.choices,
        max_length=15,
        default=users_models.ChatTypes.CHANNEL)
    is_verified = models.BooleanField(null=True)
    is_restricted = models.BooleanField(null=True)
    is_scam = models.BooleanField(null=True)
    is_support = models.BooleanField(null=True)
    title = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=32, null=True)
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    description = models.CharField(max_length=255, null=True)
    dc_id = models.IntegerField(null=True)
    invite_link = models.CharField(max_length=255, null=True)
    # Default chat member permissions, for groups and supergroups.
    permissions = models.OneToOneField(
        'telegram.ChatPermissions',
        on_delete=models.SET_NULL,
        related_name='chat',
        null=True,
    )
    # the chat linked to the current chat
    linked_chat = models.ForeignKey(
        'self',
        null=True,
        related_name='linked_chats_reverse',
        on_delete=models.SET_NULL,
    )

    #################################################
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.BigIntegerField(null=True)
    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()

    #################################################
    # `restrictions` : restrictions of this chat
    # `telegram_channels` : telegram channels connected to this chat
    # `admin_log_mentions` : admin logs this chat is mentioned in
    # `admin_logs` : admin logs belonging to this chat
    # `linked_chats_reverse` : Chats this chat is linked to
    # `messages` : messages of this channel
    # `forwarded_messages` : forwarded messages from this channel
    # `member_count_history` : member count history of the chat
    # `shared_media_history` : shared media history of the chat
    # `message_views` : message views belonging to this chat
    #

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(Chat, self).save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else self.first_name


class Message(models.Model):
    message_id = models.IntegerField()
    date = models.BigIntegerField()
    # conversation the message belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        related_name='messages',
        null=True,
    )
    # Sender, null for messages sent to channels or sender user got deleted
    from_user = models.ForeignKey(
        'telegram.User',
        on_delete=models.SET_NULL,
        related_name='messages',
        null=True,
    )
    # For forwarded messages, sender of the original message
    forward_from = models.ForeignKey(
        'telegram.User',
        on_delete=models.SET_NULL,
        related_name='forwarded_messages',
        null=True,
    )
    forward_sender_name = models.CharField(max_length=64, null=True)
    # For messages forwarded from channels, original channel of the message.
    forward_from_chat = models.ForeignKey(
        'telegram.Chat',
        related_name='forwarded_messages',
        null=True,
        on_delete=models.SET_NULL,
    )
    forward_from_message_id = models.IntegerField(null=True)
    forward_signature = models.CharField(max_length=255, null=True)
    forward_date = models.BigIntegerField(null=True)
    # For replies, the original message.
    reply_to_message = models.ForeignKey(
        'self',
        related_name='replies',
        null=True,
        on_delete=models.SET_NULL,
    )
    mentioned = models.BooleanField(null=True)
    empty = models.BooleanField()
    edit_date = models.BigIntegerField(null=True)
    media_group_id = models.BigIntegerField(null=True)
    author_signature = models.CharField(max_length=255, null=True)
    text = models.TextField(max_length=4096, null=True)
    caption = models.TextField(max_length=1024, null=True)
    # The information of the bot that generated the message from an inline query of a user.
    via_bot = models.ForeignKey(
        'telegram.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='via_bot_messages',
    )
    outgoing = models.BooleanField(null=True)

    emptied_at = models.BigIntegerField(null=True)
    has_media = models.BooleanField()
    media_type = models.CharField(
        ChatMediaTypes.choices,
        max_length=20,
        null=True,
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

    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(Message, self).save(*args, **kwargs)

    def __str__(self):
        return self.message_id


class MessageView(models.Model):
    views = models.IntegerField()
    date = models.BigIntegerField()

    # message this view belongs to
    message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.DO_NOTHING,
        null=False,
        related_name='message_views',
    )

    # TODO add more fields if necessary
    # Telegram account who logged this view
    telegram_account = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.SET_NULL,
        null=True,
        related_name='messages_views',
    )
    # Chat this view belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=True,
        related_name='message_views',
    )

    def __str__(self):
        return f"{self.views} at {self.date}"


class Entity(models.Model):
    type = models.CharField(
        EntityTypes.choices,
        max_length=20,
        null=False,
    )
    source = models.CharField(
        EntitySourceTypes.choices,
        max_length=20,
        null=False,
    )
    offset = models.IntegerField()
    length = models.IntegerField()

    # entities, both from `text` and `caption`
    message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        null=False,
        related_name='entities',
    )

    # For `text_mention` only, the mentioned user.
    user = models.ForeignKey(
        'telegram.User',
        related_name='mentioned_entities',
        null=True,
        on_delete=models.SET_NULL,
    )


class EntityType(models.Model):
    """

    """

    # Type of the entity
    type = models.CharField(
        EntityTypes.choices,
        max_length=20,
        null=False,
    )

    # Message this entity belongs to
    message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        null=False,
        related_name='entity_types',
    )


class ChatMemberCount(models.Model):
    count = models.IntegerField()
    date = models.BigIntegerField()

    # Chat this object belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=False,
        related_name='member_count_history',
    )

    ############################
    # TODO add more fields if you can
    # Telegram account who logged this member count
    telegram_account = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.SET_NULL,
        null=True,
        related_name='member_count_history',
    )

    def __str__(self):
        return f"{self.count} at {self.date}"


class ChatSharedMedia(models.Model):
    # date of getting this query
    date = models.BigIntegerField()

    photo = models.IntegerField(default=0)
    video = models.IntegerField(default=0)
    document = models.IntegerField(default=0)
    music = models.IntegerField(default=0)
    url = models.IntegerField(default=0)
    voice = models.IntegerField(default=0)
    video_note = models.IntegerField(default=0)
    animation = models.IntegerField(default=0)
    location = models.IntegerField(default=0)
    contact = models.IntegerField(default=0)

    # Chat this shared media belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=False,
        related_name='shared_media_history',
    )

    ############################
    # TODO add more fields if you can
    # Telegram account who logged this member count
    telegram_account = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.SET_NULL,
        null=True,
        related_name='shared_media_history',
    )


class Restriction(models.Model):
    """
    The reason why this chat/bot might be unavailable to some users. This field is available only in case is_restricted of `chat` or `bot` is True.
    """
    platform = models.CharField(max_length=255, null=True)
    reason = models.CharField(max_length=255, null=True)
    text = models.CharField(max_length=255, null=True)

    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=True,
        related_name='restrictions',
    )

    user = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        null=True,
        related_name='restrictions',
    )
    ##############################################
    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()
    is_deleted = models.BooleanField(default=False, null=False)
    deleted_at = models.BigIntegerField(null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(Restriction, self).save(*args, **kwargs)

    def __str__(self):
        return self.reason


class AdminLog(models.Model):
    # Chats mentioned in events
    chats = models.ManyToManyField(
        'telegram.Chat',
        related_name='admin_log_mentions',
    )

    # Users mentioned in events
    users = models.ManyToManyField(
        'telegram.User',
        related_name='admin_log_mentions',
    )

    ##################################
    query_date = models.BigIntegerField()

    # Chat this AdminLog belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        null=True,
        on_delete=models.CASCADE,
        related_name='admin_logs',
    )

    # Telegram account this AdminLog belongs to
    telegram_account = models.ForeignKey(
        'telegram.TelegramAccount',
        null=False,
        on_delete=models.CASCADE,
        related_name="admin_logs",
    )

    ####################################
    # `events` : events of this admin log

    def __str__(self):
        return f"{self.query_date}"


class AdminLogEvent(models.Model):
    event_id = models.BigIntegerField()
    date = models.BigIntegerField()
    user_id = models.BigIntegerField()

    # AdminLog this event belongs to
    admin_log = models.ForeignKey(
        'telegram.AdminLog',
        null=False,
        related_name='events',
        on_delete=models.CASCADE,
    )

    # Channel/supergroup title was changed
    action_change_title = models.OneToOneField(
        'telegram.AdminLogEventActionChangeTitle',
        on_delete=models.SET_NULL,
        related_name='admin_log_event',
        null=True,
    )

    # The description was changed
    action_change_about = models.OneToOneField(
        'telegram.AdminLogEventActionChangeAbout',
        on_delete=models.SET_NULL,
        related_name='admin_log_event',
        null=True,
    )
    # Channel/supergroup username was changed
    action_change_username = models.OneToOneField(
        'telegram.AdminLogEventActionChangeUsername',
        on_delete=models.SET_NULL,
        related_name='admin_log_event',
        null=True,
    )

    # The channel/supergroup's picture was changed
    action_change_photo = models.OneToOneField(
        'telegram.AdminLogEventActionChangePhoto',
        on_delete=models.SET_NULL,
        related_name='admin_log_event',
        null=True,
    )

    # Invites were enabled/disabled
    action_toggle_invites = models.OneToOneField(
        'telegram.AdminLogEventActionToggleInvites',
        on_delete=models.SET_NULL,
        related_name='admin_log_event',
        null=True,
    )

    # Channel signatures were enabled/disabled
    action_toggle_signatures = models.OneToOneField(
        'telegram.AdminLogEventActionToggleSignatures',
        on_delete=models.SET_NULL,
        related_name='admin_log_event',
        null=True,
    )

    # A message was pinned
    action_update_pinned = models.OneToOneField(
        'telegram.AdminLogEventActionUpdatePinned',
        on_delete=models.SET_NULL,
        related_name='admin_log_event',
        null=True,
    )

    # A message was deleted
    action_edit_message = models.OneToOneField(
        'telegram.AdminLogEventActionEditMessage',
        on_delete=models.SET_NULL,
        related_name='admin_log_event',
        null=True,
    )

    # A message was deleted
    action_delete_message = models.OneToOneField(
        'telegram.AdminLogEventActionDeleteMessage',
        on_delete=models.SET_NULL,
        related_name='admin_log_event',
        null=True,
    )

    # A user has joined the group (in the case of big groups, info of the user that has joined isn't shown)
    action_participant_join = models.OneToOneField(
        'telegram.AdminLogEventActionParticipantJoin',
        on_delete=models.SET_NULL,
        related_name='admin_log_event',
        null=True,
    )

    # A user left the channel/supergroup (in the case of big groups, info of the user that has joined isn't shown)
    action_participant_leave = models.OneToOneField(
        'telegram.AdminLogEventActionParticipantLeave',
        on_delete=models.SET_NULL,
        related_name='admin_log_event',
        null=True,
    )

    # A user was invited to the group
    action_participant_invite = models.OneToOneField(
        'telegram.AdminLogEventActionParticipantInvite',
        on_delete=models.SET_NULL,
        related_name='admin_log_event',
        null=True,
    )

    #############################################
    # user = models.ForeignKey(
    #     'telegram.User',
    #     null=True,
    #     on_delete=models.SET_NULL,
    #     related_name='admin_log_events',
    #     verbose_name='User this event is about'
    # )

    # chat = models.ForeignKey(
    #     'telegram.Chat',
    #     on_delete=models.DO_NOTHING,
    #     related_name='admin_log_events',
    #     null=False,
    # )
    #############################################

    def __str__(self):
        return f"{self.user_id} at {self.date}"


class AdminLogEventActionChangeTitle(models.Model):
    """
    Channel/supergroup title was changed
    """
    prev_value = models.CharField(max_length=255, null=True)
    new_value = models.CharField(max_length=255, null=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionChangeAbout(models.Model):
    """
    The description was changed
    """
    prev_value = models.CharField(max_length=255, null=True)
    new_value = models.CharField(max_length=255, null=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionChangeUsername(models.Model):
    """
    Channel/supergroup username was changed
    """
    prev_value = models.CharField(max_length=32, null=True)
    new_value = models.CharField(max_length=32, null=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionChangePhoto(models.Model):
    """
    The channel/supergroup's picture was changed
    """

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to
    pass


class AdminLogEventActionToggleInvites(models.Model):
    """
    Invites were enabled/disabled
    """
    new_value = models.BooleanField()

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionToggleSignatures(models.Model):
    """
    Channel signatures were enabled/disabled
    """
    new_value = models.BooleanField()

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionUpdatePinned(models.Model):
    """
    A message was pinned
    """

    # The message that was pinned
    message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.SET_NULL,
        related_name='actions_update_pinned',
        null=True,
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionEditMessage(models.Model):
    """
    A message was edited
    """

    # old message
    prev_message = models.ForeignKey(
        'telegram.Message',
        null=True,
        on_delete=models.SET_NULL,
        related_name='actions_edit_message_prev',
    )

    # new message
    new_message = models.ForeignKey(
        'telegram.Message',
        null=True,
        on_delete=models.SET_NULL,
        related_name='actions_edit_message_new',
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionDeleteMessage(models.Model):
    """
    A message was deleted
    """

    # The message that was deleted
    message = models.OneToOneField(
        'telegram.Message',
        null=True,
        on_delete=models.SET_NULL,
        related_name='action_delete_message',
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionParticipantJoin(models.Model):
    """
    A user has joined the group (in the case of big groups, info of the user that has joined isn't shown)
    """
    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionParticipantLeave(models.Model):
    """
    A user left the channel/supergroup (in the case of big groups, info of the user that has joined isn't shown)
    """
    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionParticipantInvite(models.Model):
    """
    A user was invited to the group
    """

    # The user that was invited
    participant = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_participant_invite",
    )

    # The user that was invited
    participant_self = models.OneToOneField(
        'telegram.ChannelParticipantSelf',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_participant_invite",
    )

    # The user that was invited
    participant_creator = models.OneToOneField(
        'telegram.ChannelParticipantCreator',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_participant_invite",
    )

    # The user that was invited
    participant_admin = models.OneToOneField(
        'telegram.ChannelParticipantAdmin',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_participant_invite",
    )

    # The user that was invited
    participant_banned = models.OneToOneField(
        'telegram.ChannelParticipantBanned',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_participant_invite",
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionToggleBan(models.Model):
    """
    The banned rights of a user were changed
    """

    prev_participant = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_ban_prev",
    )
    prev_participant_self = models.OneToOneField(
        'telegram.ChannelParticipantSelf',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_ban_prev",
    )
    prev_participant_creator = models.OneToOneField(
        'telegram.ChannelParticipantCreator',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_ban_prev",
    )
    prev_participant_admin = models.OneToOneField(
        'telegram.ChannelParticipantAdmin',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_ban_prev",
    )
    prev_participant_banned = models.OneToOneField(
        'telegram.ChannelParticipantBanned',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_ban_prev",
    )

    new_participant = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_ban_new",
    )
    new_participant_self = models.OneToOneField(
        'telegram.ChannelParticipantSelf',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_ban_new",
    )
    new_participant_creator = models.OneToOneField(
        'telegram.ChannelParticipantCreator',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_ban_new",
    )
    new_participant_admin = models.OneToOneField(
        'telegram.ChannelParticipantAdmin',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_ban_new",
    )
    new_participant_banned = models.OneToOneField(
        'telegram.ChannelParticipantBanned',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_ban_new",
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionToggleAdmin(models.Model):
    """
    The admin rights of a user were changed
    """
    prev_participant = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_admin_prev",
    )
    prev_participant_self = models.OneToOneField(
        'telegram.ChannelParticipantSelf',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_admin_prev",
    )
    prev_participant_creator = models.OneToOneField(
        'telegram.ChannelParticipantCreator',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_admin_prev",
    )
    prev_participant_admin = models.OneToOneField(
        'telegram.ChannelParticipantAdmin',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_admin_prev",
    )
    prev_participant_banned = models.OneToOneField(
        'telegram.ChannelParticipantBanned',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_admin_prev",
    )

    new_participant = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_admin_new",
    )
    new_participant_self = models.OneToOneField(
        'telegram.ChannelParticipantSelf',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_admin_new",
    )
    new_participant_creator = models.OneToOneField(
        'telegram.ChannelParticipantCreator',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_admin_new",
    )
    new_participant_admin = models.OneToOneField(
        'telegram.ChannelParticipantAdmin',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_admin_new",
    )
    new_participant_banned = models.OneToOneField(
        'telegram.ChannelParticipantBanned',
        on_delete=models.SET_NULL,
        null=True,
        related_name="action_toggle_admin_new",
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionChangeStickerSet(models.Model):
    """
    The supergroup's stickerset was changed
    """
    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionTogglePreHistoryHidden(models.Model):
    """
    The hidden prehistory setting was changed
    """
    new_value = models.BooleanField()

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionDefaultBannedRights(models.Model):
    """
    The default banned rights were modified
    """
    # Previous global banned rights
    prev_banned_rights = models.OneToOneField(
        'telegram.ChatBannedRight',
        on_delete=models.SET_NULL,
        related_name='action_banned_rights_prev',
        null=True,
    )

    # New global banned rights.
    new_banned_rights = models.OneToOneField(
        'telegram.ChatBannedRight',
        on_delete=models.SET_NULL,
        related_name='action_banned_rights_new',
        null=True,
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionStopPoll(models.Model):
    """
    A poll was stopped
    """

    # The poll that was stopped
    message = models.ForeignKey(
        'telegram.Message',
        null=True,
        on_delete=models.SET_NULL,
        related_name='actions_stop_poll',
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionChangeLinkedChat(models.Model):
    """
    The linked chat was changed
    """

    # Previous linked chat
    prev_value = models.IntegerField(null=True, )
    # New linked chat
    new_value = models.IntegerField(null=True, )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionChangeLocation(models.Model):
    """
    The geogroup location was changed
    """

    prev_address = models.CharField(max_length=255, null=True)
    prev_lat = models.FloatField(null=True)
    prev_long = models.FloatField(null=True)
    prev_access_hash = models.BigIntegerField(null=True)

    new_address = models.CharField(max_length=255, null=True)
    new_lat = models.FloatField(null=True)
    new_long = models.FloatField(null=True)
    new_access_hash = models.BigIntegerField(null=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


class AdminLogEventActionToggleSlowMode(models.Model):
    """
    Slow mode setting for supergroups was changed
    """

    # Previous slow mode value
    prev_value = models.IntegerField(null=True, )
    # New slow mode value
    new_value = models.IntegerField(null=True, )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to


# class ParticipantsLog(models.Model):
#     query_date = models.BigIntegerField()
#
#     channel_ref = models.ForeignKey(
#         'users.TelegramChannel',
#         null=True,
#         related_name='participants_log',
#         on_delete=models.CASCADE,
#     )
#
#     chat_ref = models.ForeignKey(
#         'telegram.Chat',v
#         null=True,
#         related_name='participants_log',
#         on_delete=models.CASCADE,
#     )


class ChannelParticipant(models.Model):
    """
    Channel/supergroup participant
    """

    # Participant user ID
    user_id = models.BigIntegerField()
    # Date joined
    date = models.BigIntegerField()

    # participants_log_ref = models.ForeignKey(
    #     'telegram.ParticipantsLog',
    #     null=True,
    #     on_delete=models.DO_NOTHING,
    #     related_name='participants'
    # )

    #################################################
    # `action_participant_invite` : Action that this participant is the invited participant
    # `action_toggle_ban_prev' : Action that this participant is the prev participant of the action
    # `action_toggle_ban_prev' : Action that this participant is the new participant of the action
    # `action_toggle_admin_prev` : Action that this participant was the the prev participant
    # `action_toggle_admin_new` : Action that this participant was the the new participant
    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(ChannelParticipant, self).save(*args, **kwargs)


class ChannelParticipantSelf(models.Model):
    """
    Myself
    """

    # User ID
    user_id = models.BigIntegerField()
    # User that invited me to the channel/supergroup
    inviter_id = models.BigIntegerField()
    # When did I join the channel/supergroup
    date = models.BigIntegerField()

    # participants_log_ref = models.ForeignKey(
    #     'telegram.ParticipantsLog',
    #     null=True,
    #     on_delete=models.DO_NOTHING,
    #     related_name='self_participant'
    # )

    #################################################
    # `action_participant_invite` : Action that this participant is the invited participant
    # `action_toggle_ban_prev' : Action that this participant is the prev participant of the action
    # `action_toggle_ban_prev' : Action that this participant is the new participant of the action
    # `action_toggle_admin_prev` : Action that this participant was the the prev participant
    # `action_toggle_admin_new` : Action that this participant was the the new participant
    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(ChannelParticipantSelf, self).save(*args, **kwargs)


class ChannelParticipantCreator(models.Model):
    """
    Channel/supergroup creator
    """

    # User id
    user_id = models.BigIntegerField()
    # The role (rank) of the group creator in the group: just an arbitrary string, admin by default
    rank = models.CharField(
        max_length=255,
        null=True,
        default='admin',
    )

    # participants_log_ref = models.ForeignKey(
    #     'telegram.ParticipantsLog',
    #     null=True,
    #     on_delete=models.DO_NOTHING,
    #     related_name='creator_participants'
    # )

    #################################################
    # `action_participant_invite` : Action that this participant is the invited participant
    # `action_toggle_ban_prev' : Action that this participant is the prev participant of the action
    # `action_toggle_ban_prev' : Action that this participant is the new participant of the action
    # `action_toggle_admin_prev` : Action that this participant was the the prev participant
    # `action_toggle_admin_new` : Action that this participant was the the new participant
    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(ChannelParticipantCreator, self).save(*args, **kwargs)


class ChannelParticipantAdmin(models.Model):
    """
    Admin
    """

    # Can this admin promote other admins with the same permissions?
    can_edit = models.BooleanField()
    # Is this the current user
    is_self = models.BooleanField()
    # Admin user ID
    user_id = models.BigIntegerField()
    # User that invited the admin to the channel/group
    inviter_id = models.BigIntegerField()
    # User that promoted the user to admin
    promoted_by = models.BigIntegerField()
    # When did the user join
    date = models.BigIntegerField()
    # The role (rank) of the admin in the group: just an arbitrary string, admin by default
    rank = models.CharField(max_length=255, null=True, default='admin', )
    admin_rights = models.OneToOneField(
        'telegram.AdminRights',
        on_delete=models.SET_NULL,
        null=True,
        related_name='participant',
    )
    # participants_log_ref = models.ForeignKey(
    #     'telegram.ParticipantsLog',
    #     null=True,
    #     on_delete=models.DO_NOTHING,
    #     related_name='admin_participants',
    # )

    #################################################
    # `action_participant_invite` : Action that this participant is the invited participant
    # `action_toggle_ban_prev' : Action that this participant is the prev participant of the action
    # `action_toggle_ban_prev' : Action that this participant is the new participant of the action
    # `action_toggle_admin_prev` : Action that this participant was the the prev participant
    # `action_toggle_admin_new` : Action that this participant was the the new participant
    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(ChannelParticipantAdmin, self).save(*args, **kwargs)


class ChannelParticipantBanned(models.Model):
    """
    Banned/kicked user
    """

    # Whether the user has left the group
    left = models.BooleanField()
    # User id
    user_id = models.BigIntegerField()
    # User was kicked by the specified admin
    kicked_by = models.BigIntegerField()
    # When did the user join the group
    date = models.BigIntegerField()
    # Banned rights
    banned_rights = models.OneToOneField(
        'telegram.ChatBannedRight',
        on_delete=models.SET_NULL,
        related_name='participant',
        null=True,
    )

    # participants_log_ref = models.ForeignKey(
    #     'telegram.ParticipantsLog',
    #     null=True,
    #     on_delete=models.DO_NOTHING,
    #     related_name='banned_participants',
    # )

    #################################################
    # `action_participant_invite` : Action that this participant is the invited participant
    # `action_toggle_ban_prev' : Action that this participant is the prev participant of the action
    # `action_toggle_ban_prev' : Action that this participant is the new participant of the action
    # `action_toggle_admin_prev` : Action that this participant was the the prev participant
    # `action_toggle_admin_new` : Action that this participant was the the new participant
    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(ChannelParticipantBanned, self).save(*args, **kwargs)


class ChatBannedRight(models.Model):
    """
    Represents the rights of a normal user in a supergroup/channel/chat.
    In this case, the flags are inverted: if set, a flag does not allow a user to do X.
    """

    # If set, does not allow a user to view messages in a supergroup/channel/chat
    view_messages = models.BooleanField()
    # If set, does not allow a user to send messages in a supergroup/chat
    send_messages = models.BooleanField()
    # If set, does not allow a user to send any media in a supergroup/chat
    send_media = models.BooleanField()
    # If set, does not allow a user to send stickers in a supergroup/chat
    send_stickers = models.BooleanField()
    # If set, does not allow a user to send gifs in a supergroup/chat
    send_gifs = models.BooleanField()
    # If set, does not allow a user to send games in a supergroup/chat/chat
    send_games = models.BooleanField()
    # If set, does not allow a user to use inline bots in a supergroup/chat
    send_inline = models.BooleanField()
    # If set, does not allow a user to embed links in the messages of a supergroup/chat
    embed_links = models.BooleanField()
    # If set, does not allow a user to send stickers in a supergroup/chat
    send_polls = models.BooleanField()
    # If set, does not allow any user to change the description of a supergroup/chat
    change_info = models.BooleanField()
    # If set, does not allow any user to invite users in a supergroup/chat
    invite_users = models.BooleanField()
    # If set, does not allow any user to pin messages in a supergroup/chat
    pin_messages = models.BooleanField()
    # "Validity of said permissions (0 = forever, forever = 2^31-1 for now)."
    until_date = models.BigIntegerField(default=0)

    #################################################
    # `action_banned_rights_prev` : Action this Rights is the previous banned rights of it
    # `action_banned_rights_new` : Action this Rights is the new banned rights of it
    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(ChatBannedRight, self).save(*args, **kwargs)


class ChatPermissions(models.Model):
    # True, if the user is allowed to send text messages, contacts, locations and venues.
    can_send_messages = models.BooleanField(null=True, )
    # True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages.
    can_send_media_messages = models.BooleanField(null=True, )
    # True, if the user is allowed to send stickers, implies can_send_media_messages.
    can_send_stickers = models.BooleanField(null=True, )
    # True, if the user is allowed to send animations (GIFs), implies can_send_media_messages.
    can_send_animations = models.BooleanField(null=True, )
    # True, if the user is allowed to send games, implies can_send_media_messages.
    can_send_games = models.BooleanField(null=True, )
    # True, if the user is allowed to use inline bots, implies can_send_media_messages.
    can_use_inline_bots = models.BooleanField(null=True, )
    # True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages.
    can_add_web_page_previews = models.BooleanField(null=True, )
    # True, if the user is allowed to send polls, implies can_send_messages.
    can_send_polls = models.BooleanField(null=True, )
    # True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups.
    can_change_info = models.BooleanField(null=True, )
    # True, if the user is allowed to invite new users to the chat.
    can_invite_users = models.BooleanField(null=True, )
    # True, if the user is allowed to pin messages. Ignored in public supergroups.
    can_pin_messages = models.BooleanField(null=True, )

    ###########################################
    # `chat` : chat this permissions belongs to

    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(ChatPermissions, self).save(*args, **kwargs)


class AdminRights(models.Model):
    change_info = models.BooleanField(null=True)
    post_messages = models.BooleanField(null=True)
    edit_messages = models.BooleanField(null=True)
    delete_messages = models.BooleanField(null=True)
    ban_users = models.BooleanField(null=True)
    pin_messages = models.BooleanField(null=True)
    add_admins = models.BooleanField(null=True)

    #################################################
    # `participant` : Participant this rights belongs to
    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super(AdminRights, self).save(*args, **kwargs)

##########################################################################
# Analyzer tables
