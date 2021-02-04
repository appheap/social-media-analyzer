from typing import Optional

from django.db import DatabaseError
from django.db import models
from django.db.models import QuerySet
from django.utils.functional import cached_property

from core.globals import logger
from db.models import SoftDeletableBaseModel, SoftDeletableQS
from pyrogram import types
from telegram import models as tg_models
from ..analyzers import AdminLogAnalyzerMetaDataUpdater
from ..analyzers import ChatMemberCountAnalyzerMetaDataUpdater
from ..analyzers import ChatMembersAnalyzerMetaDataUpdater
from ..analyzers import ChatSharedMediaAnalyzerMetaDataUpdater
from ..analyzers import MessageViewsAnalyzerMetaDataUpdater
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


class ChatQuerySet(SoftDeletableQS):
    def get_chat_by_id(self, *, chat_id: int) -> Optional["Chat"]:
        try:
            return self.get(chat_id=chat_id)
        except Chat.DoesNotExist as e:
            pass
        except Chat.MultipleObjectsReturned as e:
            logger.exception(e)
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None

    def get_chat_by_username(self, *, username: str) -> Optional["Chat"]:
        try:
            return self.get(username=username)  # fixme: `username` is not field of the class
        except DatabaseError as e:
            logger.exception(e)
        except Chat.MultipleObjectsReturned as e:
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

    def update_or_create_chat(self, *, defaults: dict, **kwargs) -> Optional["Chat"]:
        try:
            return self.update_or_create(defaults=defaults, **kwargs)[0]
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

    def update_or_create_from_raw(
            self,
            *,
            raw_chat: types.Chat,
            creator: "tg_models.User" = None,

            db_message_view: 'tg_models.MessageView' = None
    ) -> Optional["Chat"]:
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
                    defaults={
                        'type': ChatTypes.channel if raw_chat.type == 'channel' else ChatTypes.supergroup,
                        'channel': db_channel,

                        'message_view': db_message_view,
                    }
                )
        elif raw_chat.type == 'group':
            db_group = tg_models.Group.objects.update_or_create_group_from_raw(
                full_group=raw_chat.full_group,
                group=raw_chat.group,
                creator=creator
            )

            if db_group:
                db_chat = self.get_queryset().update_or_create_chat(
                    chat_id=raw_chat.id,
                    defaults={
                        'type': ChatTypes.group,
                        'group': db_group,

                        'message_view': db_message_view,
                    }
                )
        else:
            pass

        BaseChatManager.create_restrictions(
            raw_chat=raw_chat,
            db_chat=db_chat
        )

        return db_chat

    def get_chat_by_id(self, *, chat_id: int) -> Optional['Chat']:
        return self.get_queryset().get_chat_by_id(chat_id=chat_id)

    def get_chat_by_username(self, *, username: str) -> Optional['Chat']:
        return self.get_queryset().get_chat_by_username(username=username)

    def get_chats_filter_by_analyzer(
            self,
            *,
            admin_log_analyzer: bool = None,
            members_analyzer: bool = None,
            shared_media_analyzer: bool = None,
            member_count_analyzer: bool = None,
            message_view_analyzer: bool = None,
    ) -> 'QuerySet[tg_models.Chat]':

        if admin_log_analyzer is None and members_analyzer is None and shared_media_analyzer is None \
                and member_count_analyzer is None and message_view_analyzer is None:
            return self.get_queryset().none()

        _filter_obj = {}
        if admin_log_analyzer is not None:
            _filter_obj['admin_log_analyzer__enabled'] = admin_log_analyzer
        if members_analyzer is not None:
            _filter_obj['members_analyzer__enabled'] = members_analyzer
        if message_view_analyzer is not None:
            _filter_obj['message_view_analyzer__enabled'] = message_view_analyzer
        if member_count_analyzer is not None:
            _filter_obj['member_count_analyzer__enabled'] = member_count_analyzer
        if shared_media_analyzer is not None:
            _filter_obj['shared_media_analyzer__enabled'] = shared_media_analyzer

        return self.get_queryset().complex_filter(
            _filter_obj
        )

    @staticmethod
    def create_restrictions(
            raw_chat: types.Chat,
            db_chat: "Chat"
    ):
        if db_chat and raw_chat.restrictions:
            tg_models.Restriction.objects.bulk_create_restrictions(
                raw_restrictions=raw_chat.restrictions,
                db_chat=db_chat,
            )


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
    MessageViewsAnalyzerMetaDataUpdater,
    ChatMemberCountAnalyzerMetaDataUpdater,
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

    chats = BaseChatManager()
    channels = ChannelsManager()
    supergroups = SupergroupsManger()
    groups = GroupsManager()
    objects = chats

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

    message_view = models.ForeignKey(
        'telegram.MessageView',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='recent_chat_repliers',
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
    # `profile_photos` : profile photos of this chat

    @property
    def manager(self) -> BaseChatManager:
        return self._manager(self)

    @staticmethod
    def _manager(self):
        if self.type == ChatTypes.channel:
            return Chat.channels
        elif self.type == ChatTypes.supergroup:
            return Chat.supergroups
        elif self.type == ChatTypes.group:
            return Chat.groups
        else:
            return Chat.chats

    @cached_property
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

    @cached_property
    def about(self):
        if self.type in ('channel', 'supergroup'):
            return self.channel.about
        elif self.type == 'group':
            return self.group.about
        elif self.type in ('private', 'bot'):
            return self.user.about
        else:
            return ''

    @cached_property
    def username(self):
        if self.type in ('channel', 'supergroup'):
            return self.channel.username
        elif self.type == 'group':
            return None
        elif self.type in ('private', 'bot'):
            return self.user.username
        else:
            return None

    @cached_property
    def members_count(self):
        if self.type in ('channel', 'supergroup'):
            return self.channel.members_count
        elif self.type == 'group':
            return self.group.members_count
        elif self.type in ('private', 'bot'):
            return 2
        else:
            return None

    class Meta:
        indexes = [
            models.Index(fields=('type',)),
            models.Index(fields=('group',)),
            models.Index(fields=('channel',)),
            models.Index(fields=('user',)),
        ]

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
        Chat._manager(self).update_chat_from_raw(chat_id=self.chat_id, raw_chat=raw_chat)
