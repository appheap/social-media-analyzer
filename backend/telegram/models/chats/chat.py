from django.db import models
from ..base import BaseModel
from typing import Optional
from db.models import SoftDeletableBaseModel, SoftDeletableQS
from django.db import DatabaseError
from telegram.globals import logger
from telegram import models as tg_models
from pyrogram import types
from ..analyzers import AdminLogAnalyzerMetaDataUpdater
from ..analyzers import ChatMembersAnalyzerMetaDataUpdater
from ..analyzers import ChatSharedMediaAnalyzerMetaDataUpdater


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


class ChatQuerySet(SoftDeletableQS):
    def get_chat_by_id(self, *, chat_id: int) -> "Chat":
        try:
            return self.get(chat_id=chat_id)
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None

    def filter_by_id(self, *, chat_id: int) -> "ChatQuerySet":
        return self.filter(chat_id=chat_id)

    def chat_exists(self, *, chat_id: int) -> bool:
        return self.filter(chat_id=chat_id).exists()

    def channels(self) -> "ChatQuerySet":
        return self.filter(type=ChatTypes.channel)

    def supergroups(self) -> "ChatQuerySet":
        return self.filter(type=ChatTypes.supergroup)

    def groups(self) -> "ChatQuerySet":
        return self.filter(type=ChatTypes.group)

    def update_or_create_chat(self, **kwargs) -> Optional["Chat"]:
        try:
            return self.update_or_create(**kwargs)[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None


class BaseChatManager(models.Manager):
    def get_queryset(self) -> ChatQuerySet:
        return ChatQuerySet(self.model, using=self._db)

    def update_chat_from_raw(self, *, chat_id: int, raw_chat: types.Chat) -> bool:
        logger.info(f'running the base method in {self}')
        return False

    def update_or_create_from_raw(self, *, raw_chat: types.Chat, creator: "tg_models.User" = None) -> Optional["Chat"]:
        if raw_chat is None:
            return None
        db_chat = None
        if raw_chat.type in ('channel', 'supergroup'):
            db_channel = tg_models.Channel.objects.update_or_create_from_raw(
                full_channel=raw_chat.full_channel,
                channel=raw_chat.channel,
                creator=creator
            )
            if db_channel:
                db_chat = self.get_queryset().update_or_create_chat(
                    chat_id=raw_chat.id,
                    type=ChatTypes.channel if raw_chat.type == 'channel' else ChatTypes.supergroup,
                    channel=db_channel,
                )
            else:
                db_chat = None

        elif raw_chat.type == 'group':
            db_group = tg_models.Group.objects.update_or_create_group_from_raw(
                full_group=raw_chat.full_group,
                group=raw_chat.group,
                creator=creator
            )

            if db_group:
                db_chat = self.get_queryset().update_or_create_chat(
                    chat_id=raw_chat.id,
                    type=ChatTypes.group,
                    group=db_group,
                )
        else:
            pass
        return db_chat


class ChannelsManager(BaseChatManager):
    def get_queryset(self):
        return super().get_queryset().channels()

    def update_chat_from_raw(self, *, chat_id: int, raw_chat: types.Chat) -> bool:
        if not chat_id or not raw_chat:
            return False

        chat: Chat = self.get_queryset().get_chat_by_id(chat_id=chat_id)
        if chat:
            return chat.channel.update_fields_from_raw_chat(
                raw_chat=raw_chat
            )

        return False


class GroupsManager(BaseChatManager):
    def get_queryset(self):
        return super().get_queryset().groups()

    def update_chat_from_raw(self, *, chat_id: int, raw_chat: types.Chat) -> bool:
        if not chat_id or not raw_chat:
            return False

        chat: Chat = self.get_queryset().get_chat_by_id(chat_id=chat_id)
        if chat:
            return chat.group.update_fields_from_raw_chat(
                raw_chat=raw_chat
            )

        return False


class SupergroupsManger(BaseChatManager):
    def get_queryset(self):
        return super().get_queryset().supergroups()

    def update_chat_from_raw(self, *, chat_id: int, raw_chat: types.Chat) -> bool:
        if not chat_id or not raw_chat:
            return False

        chat: Chat = self.get_queryset().get_chat_by_id(chat_id=chat_id)
        if chat:
            return chat.channel.update_fields_from_raw_chat(
                raw_chat=raw_chat
            )

        return False


class Chat(
    BaseModel,
    SoftDeletableBaseModel,
    AdminLogAnalyzerMetaDataUpdater,
    ChatMembersAnalyzerMetaDataUpdater,
    ChatSharedMediaAnalyzerMetaDataUpdater,
):
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

    channels = ChannelsManager()
    supergroups = SupergroupsManger()
    groups = GroupsManager()
    chats = BaseChatManager()

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
    # `migrated_to` : supergroup this group chat migrated to

    @property
    def manager(self) -> BaseChatManager:
        if self.type == ChatTypes.channel:
            return self.channels
        elif self.type == ChatTypes.supergroup:
            return self.supergroups
        elif self.type == ChatTypes.group:
            return self.groups
        else:
            return BaseChatManager()

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

    def update_fields_from_raw(self, *, raw_chat: types.Chat):
        self.manager.update_chat_from_raw(chat_id=self.chat_id, raw_chat=raw_chat)
