import arrow
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from pyrogram.types import MessageEntity, Message as PGMessage, ChatMember

from pyrogram.raw.types import (
    ChannelParticipant as PGChannelParticipant,
    ChannelParticipantCreator as PGChannelParticipantCreator,
    ChannelParticipantAdmin as PGChannelParticipantAdmin,
    ChannelParticipantSelf as PGChannelParticipantSelf,
    ChannelParticipantBanned as PGChannelParticipantBanned
)


# Create your models here.
class MyBaseModel(models.Model):
    created_at = models.BigIntegerField(null=False, blank=True, )
    modified_at = models.BigIntegerField(null=False, blank=True, )

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = arrow.utcnow().timestamp
        self.modified_at = arrow.utcnow().timestamp
        return super().save(*args, **kwargs)


class ChatTypes(models.TextChoices):
    channel = 'channel'
    supergroup = 'supergroup'
    group = 'group'
    private = 'private'
    bot = 'bot'
    undefined = 'undefined'

    @staticmethod
    def get_type(chat_type: str):
        for choice in ChatTypes.choices:
            if chat_type == choice[0]:
                return getattr(ChatTypes, str(choice[1]).lower())
        else:
            return ChatTypes.undefined


class AddChannelRequestStatusTypes(models.TextChoices):
    INIT = 'INIT'
    CHANNEL_MEMBER = 'CHANNEL_MEMBER'
    CHANNEL_ADMIN = 'CHANNEL_ADMIN'


################################################
# models used as proxy to control access,etc to the objects they refer to
class TelegramAccount(MyBaseModel):
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=32, null=True, blank=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    is_bot = models.BooleanField(default=False)
    is_restricted = models.BooleanField(default=False)
    is_scam = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    dc_id = models.IntegerField(null=True, blank=True)
    language_code = models.CharField(max_length=5, null=True, blank=True)

    # fields needed for telegram client api
    api_id = models.CharField(max_length=256, null=True, blank=True)
    api_hash = models.CharField(max_length=256, null=True, blank=True)
    session_name = models.CharField(max_length=256, null=True, blank=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.BigIntegerField(null=True, blank=True)

    # `telegram_channels` : telegram channels added by this account
    # `chats` : chats added by this account
    # `telegram_channel_add_requests` : requests for adding telegram channel this account is requested to be admin of
    # `admin_log_events` : admin log events logged by this account
    # `logged_messages` : messages logged by this account
    # `message_views` : message views logged by this account
    # `member_count_history` : member counts logged by this account
    # `shared_media_history` : shared media counts logged by this account
    # `admin_rights` : admin rights belonging to this account
    # `dialogs` : dialogs belonging to this account

    # User who is the owner of this telegram account
    custom_user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name='telegram_accounts',
        null=True, blank=True,
    )

    # Telegram User this account belongs to
    telegram_user = models.ForeignKey(
        'telegram.User',
        related_name='telegram_accounts',
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )

    # the blockage object
    blockage = models.OneToOneField(
        'users.Blockage',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='telegram_account',
    )

    def __str__(self):
        return str(self.username if self.username else "") + str(self.first_name if self.first_name else "") + str(
            self.last_name if self.last_name else "")


class AddChannelRequest(MyBaseModel):
    done = models.BooleanField(null=False, default=False, )
    status = models.CharField(
        AddChannelRequestStatusTypes.choices,
        max_length=20,
        null=True, blank=True,
        default=AddChannelRequestStatusTypes.INIT,
    )
    channel_username = models.CharField(
        null=False,
        verbose_name='channel username',
        max_length=32,
        validators=[MinLengthValidator(5)])

    channel_id = models.BigIntegerField(
        null=True,
        blank=True,
        verbose_name='channel id',
    )

    # User who added made this request
    custom_user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='Owner',
        related_name='telegram_channel_add_requests',
        null=False,
    )

    # telegram channel requested to be the admin of
    telegram_channel = models.ForeignKey(
        'telegram.TelegramChannel',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='add_requests',
    )

    # telegram account chosen to be the admin of the channel
    telegram_account = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        related_name='telegram_channel_add_requests',
        null=False,
        verbose_name='admin',
    )

    # def get_absolute_url(self):
    #     return reverse('dashboard/')
    def __str__(self):
        return str(
            f"{arrow.get(self.created_at)} : {self.custom_user} : @{self.channel_username} : {self.telegram_account}")


class TelegramChannel(MyBaseModel):
    channel_id = models.BigIntegerField()
    is_account_creator = models.BooleanField(null=True, blank=True)
    is_account_admin = models.BooleanField(null=False, default=False, )
    is_active = models.BooleanField(null=False, default=False, )

    username = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name='username',
        validators=[MinLengthValidator(5)],
    )
    is_public = models.BooleanField(default=False, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.BigIntegerField(null=True, blank=True)

    # User who added this telegram channel
    user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name='telegram_channels',
        null=True, blank=True,
    )

    # telegram account which added this channel
    telegram_account = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        related_name='telegram_channels',
        null=False,
        verbose_name='admin',
    )

    # Chat this channel belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='telegram_channels',
    )

    # the blockage object
    blockage = models.OneToOneField(
        'users.Blockage',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='telegram_channel',
    )

    ################################################
    # `chat_member_analyzer_metadata` : chat member analyzer of this channel
    # `admin_log_analyzer_metadata` : admin log analyzer of this channel
    # `add_requests` : requests made for adding this channel to an user's accounts
    # `admin_rights`: admin rights belonging to this channel

    def __str__(self):
        return str(self.chat.title) if self.chat else str(self.username)

    def get_absolute_url(self):
        return reverse('dashboard:accounts')


################################################
# the models used to implement telegram functionality

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
    def get_type(message: PGMessage):
        for choice in ChatMediaTypes.choices:
            if hasattr(message, choice[0]):
                return getattr(ChatMediaTypes, str(choice[0]).lower())
        else:
            return ChatMediaTypes.undefined


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


class EntitySourceTypes(models.TextChoices):
    text = "text"
    caption = "caption"


class EntityTypes(models.TextChoices):
    mention = 'mention'
    hashtag = 'hashtag'
    cashtag = 'cashtag'
    bot_command = 'bot_command'
    url = 'url'
    email = 'email'
    phone_number = 'phone_number'
    bold = 'bold'
    italic = 'italic'
    code = 'code'
    pre = 'pre'
    text_link = 'text_link'
    text_mention = 'text_mention'
    undefined = 'undefined'

    @staticmethod
    def get_type(entity: MessageEntity):
        for choice in EntityTypes.choices:
            if choice[0] == entity.type:
                return getattr(EntityTypes, str(choice[0]).lower())
        else:
            return EntityTypes.undefined


class User(MyBaseModel):
    user_id = models.BigIntegerField(primary_key=True)
    is_deleted = models.BooleanField(null=True, blank=True)
    is_bot = models.BooleanField(null=True, blank=True)
    is_verified = models.BooleanField(null=True, blank=True)
    is_restricted = models.BooleanField(null=True, blank=True)
    is_scam = models.BooleanField(null=True, blank=True)
    is_support = models.BooleanField(null=True, blank=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    username = models.CharField(max_length=32, null=True, blank=True)
    language_code = models.CharField(max_length=20, null=True, blank=True)
    dc_id = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    ##############################################################
    deleted_at = models.BigIntegerField(null=True, blank=True)

    # `telegram_accounts` : telegram accounts connected to this user
    # `restrictions` : restrictions of this user if it's a bot
    # `admin_log_mentions` : admin logs this user is mentioned in
    # `admin_log_events` : admin logs this user has committed
    # `forwarded_messages` : forwarded messages from this user
    # `messages` : messages belonging to this user in a chat
    # `via_bot_messages` : messages (inline queries) that were generated by this bot in a chat
    # `mentioned_entities` : entities that this user is mentioned in
    # `chats` : chats this users is/was member of (including state; is current member or left the chat)
    # `promoted_participants` : channel participants promoted by this user
    # `demoted_participants` : channel participants demoted by this user
    # `invited_participants` : channel participants invited by this user
    # `kicked_participants` : channel participants kicked by this user

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        # return str(self.first_name if self.first_name else "") + str(self.last_name if self.last_name else "")
        return f"{self.first_name if self.first_name else self.last_name if self.last_name else ''} `@{self.username if self.username else self.user_id}`"


class Dialog(MyBaseModel):
    id = models.CharField(max_length=265, primary_key=True, )  # `user_id:chat_id`
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=False,
        related_name='dialogs',
    )

    account = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        null=False,
        related_name='dialogs',
    )

    is_member = models.BooleanField(default=True, blank=True, )
    left_at = models.BigIntegerField(null=True, blank=True, )

    def __str__(self):
        return f"{self.account} : {self.chat}"


class Chat(MyBaseModel):
    chat_id = models.BigIntegerField(primary_key=True)
    type = models.CharField(
        ChatTypes.choices,
        max_length=15,
        default=ChatTypes.channel)
    is_verified = models.BooleanField(null=True, blank=True)
    is_restricted = models.BooleanField(null=True, blank=True)
    is_scam = models.BooleanField(null=True, blank=True)
    is_support = models.BooleanField(null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    username = models.CharField(max_length=32, null=True, blank=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(max_length=256, null=True, blank=True)
    dc_id = models.IntegerField(null=True, blank=True)
    invite_link = models.CharField(max_length=256, null=True, blank=True)
    # Default chat member permissions, for groups and supergroups.
    permissions = models.OneToOneField(
        'telegram.ChatPermissions',
        on_delete=models.SET_NULL,
        related_name='chat',
        null=True, blank=True,
    )
    # the chat linked to the current chat
    linked_chat = models.ForeignKey(
        'self',
        null=True, blank=True,
        related_name='linked_chats_reverse',
        on_delete=models.SET_NULL,
    )

    #################################################
    # telegram account which added this chat
    logger_account = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        related_name='chats',
        null=False,
        verbose_name='logger account',
    )

    shared_media_analyzer = models.OneToOneField(
        'telegram.SharedMediaAnalyzerMetaData',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='chat',
    )

    member_count_analyzer = models.OneToOneField(
        'telegram.ChatMemberCountAnalyzerMetaData',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='chat',
    )

    message_view_analyzer = models.OneToOneField(
        'telegram.ChatMessageViewsAnalyzerMetaData',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='chat',
    )

    members_analyzer = models.OneToOneField(
        'telegram.ChatMembersAnalyzerMetaData',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='chat',
    )

    admin_log_analyzer = models.OneToOneField(
        'telegram.AdminLogAnalyzerMetaData',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='chat',
    )

    # users who are/were member of this chat (including their state; currently member or left the chat)
    members = models.ManyToManyField(
        'telegram.User',
        related_name='chats',
        through='telegram.Membership',
        through_fields=('chat', 'user'),
    )

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.BigIntegerField(null=True, blank=True)

    is_public = models.BooleanField(default=False)

    #################################################
    # `restrictions` : restrictions of this chat
    # `telegram_channels` : telegram channels connected to this chat
    # `admin_log_mentions` : admin logs this chat is mentioned in
    # `admin_log_events` : admin log events belonging to this chat
    # `linked_chats_reverse` : Chats this chat is linked to
    # `messages` : messages of this channel
    # `forwarded_messages` : forwarded messages from this channel
    # `member_count_history` : member count history of the chat
    # `shared_media_history` : shared media history of the chat
    # `message_views` : message views belonging to this chat
    # `dialogs` : dialogs this chat belongs to

    def __str__(self):
        s = self.title if self.title else self.first_name if self.first_name else self.last_name
        r = s if s else str(self.chat_id)
        _type = '📢'
        if self.type == 'channel':
            _type = '📢'
        elif self.type == 'supergroup':
            _type = '👥*'
        elif self.type == 'group':
            _type = '👥'
        elif self.type == 'private':
            _type = '👤'
        elif self.type == 'bot':
            _type = '🤖'
        else:
            pass
        return f'{_type} {r}'


class Membership(MyBaseModel):
    # id = models.CharField(
    #     max_length=256,
    #     null=False,
    #     primary_key=True,
    # )  # `chat_id:user_id`

    user = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        related_name='+',
    )

    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        related_name='+',
    )

    class Meta:
        # order_with_respect_to = 'chat'
        unique_together = [
            ('chat', 'user'),
        ]
        ordering = ['chat', 'user']

    current_status = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='+'
    )
    previous_status = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='+'
    )

    status_change_date = models.BigIntegerField(null=True, blank=True)

    ######################################
    # `participant_history` : participants related to this membership

    def __str__(self):
        return f"{self.user} @ {self.chat} : {self.current_status.type if self.current_status else ''}"


class ChannelParticipant(MyBaseModel):
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
        'telegram.ChatBannedRight',
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


class Message(MyBaseModel):
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
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='logged_messages',
    )

    class Meta:
        ordering = ('-date', 'chat',)
        get_latest_by = ('-date', 'chat',)

    def __str__(self):
        return f"message {self.message_id} from {self.chat}"


class MessageView(MyBaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:message_id:date`

    views = models.BigIntegerField()
    date = models.BigIntegerField()

    # message this view belongs to
    message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        null=False,
        related_name='message_views',
    )

    # TODO add more fields if necessary
    # Telegram account who logged this view
    logged_by = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='messages_views',
    )
    # Chat this view belongs to
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='message_views',
    )

    class Meta:
        ordering = ['-date', 'message', ]
        get_latest_by = ['-date', 'message', ]

    def __str__(self):
        return f"{self.views} @ ({arrow.get(self.date, tzinfo='utc').format('YYYY-MM-DD HH:mm:ss')}) of {self.message}"


class Entity(MyBaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:message_id:offset`

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
        null=True, blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'Entities'
        ordering = ('message',)

    def __str__(self):
        return f"{self.type} of type {self.source} in {self.message}"


class EntityType(MyBaseModel):
    """

    """
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:message_id:type`

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

    class Meta:
        verbose_name_plural = 'Entity Types'

    def __str__(self):
        return f"{self.type} in {self.message}"


class ChatMemberCount(MyBaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:logged_by_id:date`

    count = models.BigIntegerField()
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
    logged_by = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='member_count_history',
    )

    class Meta:
        ordering = ('-date',)
        get_latest_by = ('-date',)

    def __str__(self):
        return f"{self.chat} : {self.count} @ {arrow.get(self.date)}"


class ChatSharedMedia(MyBaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:logged_by_id:date`

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
    logged_by = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='shared_media_history',
    )

    class Meta:
        ordering = ('-date',)
        get_latest_by = ('-date',)

    def __str__(self):
        return f"{self.chat} @ {arrow.get(self.date)}"


class Restriction(MyBaseModel):
    """
    The reason why this chat/bot might be unavailable to some users. This field is available only in case is_restricted of `chat` or `bot` is True.
    """

    id = models.CharField(max_length=256, primary_key=True, )  # `chat|user:_id`

    platform = models.CharField(max_length=256, null=True, blank=True)
    reason = models.CharField(max_length=256, null=True, blank=True)
    text = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        unique_together = [('id', 'platform', 'reason', 'text'), ]

    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='restrictions',
    )

    user = models.ForeignKey(
        'telegram.User',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='restrictions',
    )
    ##############################################
    is_deleted = models.BooleanField(default=False, null=False)
    deleted_at = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.reason


class AdminLogEvent(MyBaseModel):
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


class AdminLogEventActionChangeTitle(MyBaseModel):
    """
    Channel/supergroup title was changed
    """
    prev_value = models.CharField(max_length=256, null=True, blank=True)
    new_value = models.CharField(max_length=256, null=True, blank=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (change title)'


class AdminLogEventActionChangeAbout(MyBaseModel):
    """
    The description was changed
    """
    prev_value = models.CharField(max_length=256, null=True, blank=True)
    new_value = models.CharField(max_length=256, null=True, blank=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (change about)'


class AdminLogEventActionChangeUsername(MyBaseModel):
    """
    Channel/supergroup username was changed
    """
    prev_value = models.CharField(max_length=32, null=True, blank=True)
    new_value = models.CharField(max_length=32, null=True, blank=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (change username)'


class AdminLogEventActionChangePhoto(MyBaseModel):
    """
    The channel/supergroup's picture was changed
    """

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (change photo)'


class AdminLogEventActionToggleInvites(MyBaseModel):
    """
    Invites were enabled/disabled
    """
    new_value = models.BooleanField()

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (toggle invites)'


class AdminLogEventActionToggleSignatures(MyBaseModel):
    """
    Channel signatures were enabled/disabled
    """
    new_value = models.BooleanField()

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (toggle signatures)'


class AdminLogEventActionUpdatePinned(MyBaseModel):
    """
    A message was pinned
    """

    # The message that was pinned
    message = models.ForeignKey(
        'telegram.Message',
        on_delete=models.CASCADE,
        related_name='actions_update_pinned',
        null=True, blank=True,
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (message pinned)'


class AdminLogEventActionEditMessage(MyBaseModel):
    """
    A message was edited
    """

    # old message
    prev_message = models.ForeignKey(
        'telegram.Message',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='actions_edit_message_prev',
    )

    # new message
    new_message = models.ForeignKey(
        'telegram.Message',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='actions_edit_message_new',
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (message edit)'


class AdminLogEventActionDeleteMessage(MyBaseModel):
    """
    A message was deleted
    """

    # The message that was deleted
    message = models.OneToOneField(
        'telegram.Message',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='action_delete_message',
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (message deletion)'


class AdminLogEventActionParticipantJoin(MyBaseModel):
    """
    A user has joined the group (in the case of big groups, info of the user that has joined isn't shown)
    """

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (participant join)'


class AdminLogEventActionParticipantLeave(MyBaseModel):
    """
    A user left the channel/supergroup (in the case of big groups, info of the user that has joined isn't shown)
    """

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to
    class Meta:
        verbose_name_plural = 'Events (participant leave)'


class AdminLogEventActionParticipantInvite(MyBaseModel):
    """
    A user was invited to the group
    """

    # The user that was invited
    participant = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="action_participant_invite",
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to
    class Meta:
        verbose_name_plural = 'Events (participant invite)'


class AdminLogEventActionToggleBan(MyBaseModel):
    """
    The banned rights of a user were changed
    """

    prev_participant = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="action_toggle_ban_prev",
    )

    new_participant = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="action_toggle_ban_new",
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (toggle ban)'


class AdminLogEventActionToggleAdmin(MyBaseModel):
    """
    The admin rights of a user were changed
    """
    prev_participant = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="action_toggle_admin_prev",
    )

    new_participant = models.OneToOneField(
        'telegram.ChannelParticipant',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="action_toggle_admin_new",
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (toggle admin)'


class AdminLogEventActionChangeStickerSet(MyBaseModel):
    """
    The supergroup's stickerset was changed
    """

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (change sticker set)'


class AdminLogEventActionTogglePreHistoryHidden(MyBaseModel):
    """
    The hidden prehistory setting was changed
    """
    new_value = models.BooleanField()

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (prehistory hidden)'


class AdminLogEventActionDefaultBannedRights(MyBaseModel):
    """
    The default banned rights were modified
    """
    # Previous global banned rights
    prev_banned_rights = models.OneToOneField(
        'telegram.ChatBannedRight',
        on_delete=models.CASCADE,
        related_name='action_banned_rights_prev',
        null=True, blank=True,
    )

    # New global banned rights.
    new_banned_rights = models.OneToOneField(
        'telegram.ChatBannedRight',
        on_delete=models.CASCADE,
        related_name='action_banned_rights_new',
        null=True, blank=True,
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (default banned rights)'


class AdminLogEventActionStopPoll(MyBaseModel):
    """
    A poll was stopped
    """

    # The poll that was stopped
    message = models.ForeignKey(
        'telegram.Message',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='actions_stop_poll',
    )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (stop poll)'


class AdminLogEventActionChangeLinkedChat(MyBaseModel):
    """
    The linked chat was changed
    """

    # Previous linked chat
    prev_value = models.IntegerField(null=True, blank=True, )
    # New linked chat
    new_value = models.IntegerField(null=True, blank=True, )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (change linked chat)'


class AdminLogEventActionChangeLocation(MyBaseModel):
    """
    The geogroup location was changed
    """

    prev_address = models.CharField(max_length=256, null=True, blank=True)
    prev_lat = models.FloatField(null=True, blank=True)
    prev_long = models.FloatField(null=True, blank=True)
    prev_access_hash = models.BigIntegerField(null=True, blank=True)

    new_address = models.CharField(max_length=256, null=True, blank=True)
    new_lat = models.FloatField(null=True, blank=True)
    new_long = models.FloatField(null=True, blank=True)
    new_access_hash = models.BigIntegerField(null=True, blank=True)

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (change location)'


class AdminLogEventActionToggleSlowMode(MyBaseModel):
    """
    Slow mode setting for supergroups was changed
    """

    # Previous slow mode value
    prev_value = models.IntegerField(null=True, blank=True, )
    # New slow mode value
    new_value = models.IntegerField(null=True, blank=True, )

    ###########################################
    # `admin_log_event` : AdminLogEvent this action belongs to

    class Meta:
        verbose_name_plural = 'Events (toggle slow mode)'


# todo: relation with chat?
class ChatBannedRight(MyBaseModel):
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
    # `participant` : Participant this rights belongs to


# for supergroups
class ChatPermissions(MyBaseModel):
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
    # True, if the user is allowed to use inline bots, implies can_send_media_messages.
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

    ###########################################
    # `chat` : chat this permissions belongs to

    class Meta:
        verbose_name_plural = 'Chat permissions'


class AdminRights(MyBaseModel):
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

    def has_changed(self, chat_member: ChatMember):
        if not chat_member:
            return True

        if self.change_info != chat_member.can_change_info or \
                self.post_messages != chat_member.can_post_messages or \
                self.edit_messages != chat_member.can_edit_messages or \
                self.delete_messages != chat_member.can_delete_messages or \
                self.ban_users != chat_member.can_restrict_members or \
                self.invite_users != chat_member.can_invite_users or \
                self.pin_messages != chat_member.can_pin_messages or \
                self.add_admins != chat_member.can_promote_members:
            return True
        return False

    def __str__(self):
        return str(
            f"{self.admin if self.admin else ''} @ {self.telegram_channel if self.telegram_channel else ''}{' : current' if self.is_latest else ''}") if self.admin and self.telegram_channel else str(
            self.pk)


##########################################################################
# Analyzer tables

class SharedMediaAnalyzerMetaData(MyBaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:created_at`

    enabled = models.BooleanField()
    first_analyzed_at = models.BigIntegerField(null=True, blank=True)
    last_analyzed_at = models.BigIntegerField(null=True, blank=True)
    disabled_at = models.BigIntegerField(null=True, blank=True)
    disable_reason = models.CharField(max_length=256, null=True, blank=True, )

    ######################################

    ######################################
    # `chat` : chat this analyzer metadata belongs to

    class Meta:
        verbose_name_plural = 'Analyzers (chat shared medias)'

    def __str__(self):
        return str(f" {self.id} : {self.enabled}")


class AdminLogAnalyzerMetaData(MyBaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:created_at`

    enabled = models.BooleanField()
    first_analyzed_at = models.BigIntegerField(null=True, blank=True)
    last_analyzed_at = models.BigIntegerField(null=True, blank=True)
    disabled_at = models.BigIntegerField(null=True, blank=True)
    disable_reason = models.CharField(max_length=256, null=True, blank=True, )

    ######################################

    # current active telegram channel
    telegram_channel = models.OneToOneField(
        'telegram.TelegramChannel',
        on_delete=models.CASCADE,
        related_name='admin_log_analyzer_metadata',
        null=True, blank=True,
    )

    ######################################
    # `chat` : chat this analyzer metadata belongs to

    class Meta:
        verbose_name_plural = 'Analyzers (chat admin logs)'

    def __str__(self):
        return f"{self.id} : {self.enabled}"


class ChatMemberCountAnalyzerMetaData(MyBaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:created_at`

    enabled = models.BooleanField()
    first_analyzed_at = models.BigIntegerField(null=True, blank=True)
    last_analyzed_at = models.BigIntegerField(null=True, blank=True)
    disabled_at = models.BigIntegerField(null=True, blank=True)
    disable_reason = models.CharField(max_length=256, null=True, blank=True, )

    ######################################
    # `chat` : chat this analyzer metadata belongs to

    class Meta:
        verbose_name_plural = 'Analyzers (chat member count)'

    def __str__(self):
        return f"{self.id} : {self.enabled}"


class ChatMembersAnalyzerMetaData(MyBaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:created_at`

    enabled = models.BooleanField()
    first_analyzed_at = models.BigIntegerField(null=True, blank=True)
    last_analyzed_at = models.BigIntegerField(null=True, blank=True)
    disabled_at = models.BigIntegerField(null=True, blank=True)
    disable_reason = models.CharField(max_length=256, null=True, blank=True, )

    ######################################
    # current active telegram channel
    telegram_channel = models.OneToOneField(
        'telegram.TelegramChannel',
        on_delete=models.SET_NULL,
        related_name='chat_member_analyzer_metadata',
        null=True, blank=True,
    )

    ######################################
    # `chat` : chat this analyzer metadata belongs to

    class Meta:
        verbose_name_plural = 'Analyzers (chat members)'

    def __str__(self):
        return f"{self.id} : {self.enabled}"


class ChatMessageViewsAnalyzerMetaData(MyBaseModel):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:created_at`

    enabled = models.BooleanField()
    first_analyzed_at = models.BigIntegerField(null=True, blank=True)
    last_analyzed_at = models.BigIntegerField(null=True, blank=True)
    disabled_at = models.BigIntegerField(null=True, blank=True)
    disable_reason = models.CharField(max_length=256, null=True, blank=True, )

    ######################################
    # `chat` : chat this analyzer metadata belongs to

    class Meta:
        verbose_name_plural = 'Analyzers (message view)'

    def __str__(self):
        return f"{self.id} : {self.enabled}"
