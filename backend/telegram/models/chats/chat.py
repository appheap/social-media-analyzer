from django.db import models
from ..base import BaseModel


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


class Chat(BaseModel):
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
