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
    chat_id = models.BigIntegerField(primary_key=True)  # fixme: what about private/bot chats?
    type = models.CharField(
        ChatTypes.choices,
        max_length=15,
        default=ChatTypes.channel)

    channel = models.OneToOneField(
        'telegram.Channel',
        models.CASCADE,
        related_name='chat',
        null=True,
        blank=True,
    )

    group = models.OneToOneField(
        'telegram.Group',
        models.CASCADE,
        related_name='chat',
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        'telegram.User',
        models.CASCADE,
        related_name='chat_peers',  # fixme: maybe a better name?
        null=True,
        blank=True,
    )

    #################################################
    # telegram accounts which are peers of this chat
    logger_accounts = models.ManyToManyField(
        'telegram.TelegramAccount',
        related_name='chats',
        through='telegram.AdminShip',
        through_fields=('chat', 'account'),
        verbose_name='logger accounts',
    )

    # users who are/were member of this chat (including their state; currently member or left the chat)
    members = models.ManyToManyField(
        'telegram.User',
        related_name='chats',
        through='telegram.Membership',
        through_fields=('chat', 'user'),
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

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.BigIntegerField(null=True, blank=True)

    #################################################
    # `restrictions` : restrictions of this chat
    # `telegram_channels` : telegram channels connected to this chat
    # `admin_log_mentions` : admin logs this chat is mentioned in
    # `admin_log_events` : admin log events belonging to this chat
    # `linked_chats_reverse` : Chats this chat is linked to
    # `messages` : messages of this channel
    # `forwarded_messages` : forwarded messages from this chat
    # `saved_messages` : saved messages from this chat
    # `sent_messages` : sent messages from this chat
    # `message_replies` : replies to this chat
    # `member_count_history` : member count history of the chat
    # `shared_media_history` : shared media history of the chat
    # `message_views` : message views belonging to this chat
    # `dialogs` : dialogs this chat belongs to
    # `migrated_to` : chat this group chat migrated to

    @property
    def title(self):
        if self.type in ('channel', 'supergroup'):
            return self.channel.title
        elif self.type == 'group':
            return self.group.title
        elif self.type in ('private', 'bot'):
            s = f"{self.user.first_name}" if self.user.first_name else ""
            s += " : " if len(s) else ""
            s += f"{self.user.last_name}" if self.user.last_name else ""
            return s
        else:
            return str(self.chat_id)

    def __str__(self):
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
        return f'{_type} {self.title}'
