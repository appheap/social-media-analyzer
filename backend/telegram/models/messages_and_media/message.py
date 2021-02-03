from typing import Optional

from django.db import models, transaction
from ..base import BaseModel
from pyrogram import types
from db.models import SoftDeletableBaseModel
from db.models import SoftDeletableQS
from django.db import DatabaseError
from core.globals import logger
from ..chats import ChatUpdater
from ..users import UserUpdater
from .message_updater import MessageUpdater
from telegram import models as tg_models


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
    def get_type(raw_media_type: str):
        if raw_media_type is None:
            return ChatMediaTypes.undefined

        for choice in ChatMediaTypes.choices:
            if raw_media_type == choice[0]:
                return getattr(ChatMediaTypes, str(choice[0]).lower())
        else:
            return ChatMediaTypes.undefined


class MessageTypes(models.TextChoices):
    message = 'message'
    service = 'service'
    empty = 'empty'
    undefined = 'undefined'


class MessageQuerySet(SoftDeletableQS):
    def filter_by_message_id(self, *, message_id: int) -> "MessageQuerySet":
        return self.filter(message_id=message_id)

    def filter_by_date_ts(self, *, date_ts: int) -> "MessageQuerySet":
        return self.filter(date_ts__in=(date_ts - 1, date_ts, date_ts + 1))

    def scheduled(self) -> "MessageQuerySet":
        return self.filter(is_scheduled=True)

    def non_scheduled(self) -> "MessageQuerySet":
        return self.filter(is_scheduled=False)

    def filter_by_id(self, *, id: str) -> "MessageQuerySet":
        return self.filter(id=id)

    def filter_by_chat(self, *, db_chat: 'tg_models.Chat', ) -> "MessageQuerySet":
        return self.filter(chat=db_chat)

    def get_by_id(self, *, id: str) -> Optional["Message"]:
        try:
            return self.get(id=id)
        except Message.DoesNotExist:
            pass
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None

    def get_by_message_id(self, *, message_id: int) -> Optional["Message"]:
        try:
            return self.order_by().filter(message_id=message_id).order_by('-edit_date_ts')[0]
        except Message.DoesNotExist:
            pass
        except DatabaseError as e:
            logger.exception(e)
        except IndexError as e:
            pass
        except Exception as e:
            logger.exception(e)
        return None

    def update_or_create_message(self, *, defaults: dict, **kwargs) -> Optional["Message"]:
        try:
            return self.update_or_create(
                defaults=defaults,
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None

    def update_message(self, **kwargs) -> bool:
        try:
            return bool(
                self.update(
                    **kwargs
                )
            )
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return False


class MessageManager(models.Manager):
    def get_queryset(self) -> "MessageQuerySet":
        return MessageQuerySet(self.model, using=self._db)

    def get_message_from_raw(
            self,
            *,
            chat_id: int,
            raw_message: 'types.Message'
    ) -> Optional['types.Message']:
        if chat_id is None or raw_message is None:
            return None

        return self.get_queryset().get_by_id(
            id=self._get_id_from_raw_message(chat_id, raw_message)
        )

    def get_message_by_message_id(
            self,
            *,
            db_chat: 'tg_models.Chat',
            message_id: int,
    ) -> Optional['Message']:
        if db_chat is None or message_id is None:
            return None

        return self.get_queryset().filter_by_chat(db_chat=db_chat).get_by_message_id(
            message_id=message_id
        )

    @staticmethod
    def _get_id_from_raw_message(chat_id: int, raw_message: 'types.Message'):
        edit_date = getattr(raw_message.content, 'edit_date', 0)
        edit_date = edit_date if edit_date is not None else 0
        return f"{chat_id}:{int(raw_message.is_scheduled)}:{raw_message.message_id}:{edit_date}"

    def update_or_create_from_raw(
            self,
            *,
            db_chat: 'tg_models.Chat',
            raw_message: types.Message,
            logger_account: "tg_models.TelegramAccount"
    ) -> Optional["Message"]:

        if db_chat is None or raw_message is None or logger_account is None:
            return None
        parsed_msg = self._parse_normal(
            raw_message=raw_message
        )

        if parsed_msg and len(parsed_msg):
            with transaction.atomic():
                db_message = self.get_queryset().update_or_create_message(
                    id=self._get_id_from_raw_message(db_chat.chat_id, raw_message),
                    defaults={
                        **parsed_msg,
                        'chat': db_chat,
                        'logged_by': logger_account,
                    }
                )

                self._update_message_related_models(db_message, raw_message)

            return db_message

        return None

    def update_from_raw(
            self,
            *,
            chat_id: int,
            id: str,
            raw_message: types.Message,
            logger_account: "tg_models.TelegramAccount" = None
    ) -> bool:

        if chat_id is None or id is None or raw_message is None:
            return False

        parsed_msg = self._parse_normal(
            raw_message=raw_message
        )

        if parsed_msg and len(parsed_msg):
            if logger_account:
                parsed_msg['logged_by'] = logger_account

            _updated = False
            with transaction.atomic():
                db_message_qs = self.get_queryset().filter_by_id(id=id)
                _updated = db_message_qs.update_message(
                    **parsed_msg
                )
                if db_message_qs.exists():
                    self._update_message_related_models(db_message_qs[0], raw_message)

            return _updated

        return False

    def get_scheduled_message(
            self,
            db_chat: 'tg_models.Chat',
            date_ts: int
    ) -> Optional['Message']:
        if db_chat is None or date_ts is None:
            return None

        qs = self.get_queryset().scheduled().filter_by_chat(db_chat=db_chat).filter_by_date_ts(date_ts=date_ts)
        if qs.exists():
            return qs.first()

        return None

    def _update_message_related_models(self, db_message: 'Message', raw_message: types.Message):
        if db_message and raw_message:
            db_message.update_or_create_chat_from_raw(
                model=db_message,
                field_name='sender_chat',
                raw_chat=raw_message.content.sender_chat
            )
            db_message.update_or_create_user_from_raw(
                model=db_message,
                field_name='user',
                raw_user=raw_message.content.from_user
            )
            if raw_message.content.forward_header:
                db_message.update_or_create_chat_from_raw(
                    model=db_message,
                    field_name='forward_from_chat',
                    raw_chat=raw_message.content.forward_header.forward_from_chat
                )
                db_message.update_or_create_user_from_raw(
                    model=db_message,
                    field_name='forward_from_user',
                    raw_user=raw_message.content.forward_header.forward_from_user
                )

                # fixme: forward_from_message ?

                db_message.update_or_create_chat_from_raw(
                    model=db_message,
                    field_name='saved_from_chat',
                    raw_chat=raw_message.content.forward_header.saved_from_chat
                )
                db_message.update_or_create_user_from_raw(
                    model=db_message,
                    field_name='saved_from_user',
                    raw_user=raw_message.content.forward_header.saved_from_user
                )

            if raw_message.content.reply_header:
                # fixme: `reply_to_message` and `reply_to_top_message`?
                db_message.update_or_create_chat_from_raw(
                    model=db_message,
                    field_name='reply_to_chat',
                    raw_chat=raw_message.content.reply_header.reply_to_chat
                )
                db_message.update_or_create_user_from_raw(
                    model=db_message,
                    field_name='reply_to_user',
                    raw_user=raw_message.content.reply_header.reply_to_user
                )

            if raw_message.restrictions:
                MessageManager.create_restrictions(
                    raw_message=raw_message,
                    db_message=db_message,
                )

            if db_message.from_scheduled:
                db_scheduled_message = self.get_scheduled_message(
                    db_chat=db_message.chat,
                    date_ts=db_message.date_ts,
                )
                if db_scheduled_message:
                    db_scheduled_message.update_sent_status()
                    db_message.update_or_create_message_from_db_message(
                        model=db_message,
                        field_name='scheduled_message',
                        db_message=db_scheduled_message,
                    )
                    tg_models.Post.posts.update_post_status_from_message(
                        db_message=db_message
                    )

    @staticmethod
    def _parse_normal(*, raw_message: types.Message) -> dict:
        if not raw_message:
            return {}

        content = raw_message.content
        if not content or raw_message.type != 'message':
            return {}

        r = {
            'message_id': raw_message.message_id,
            'date_ts': raw_message.date,
            'type': MessageTypes.message,
            "edit_date_ts": content.edit_date,
            "is_outgoing": content.is_outgoing,
            "mentioned": content.mentioned,
            "is_silent": content.is_silent,
            "is_post": content.is_post,
            "post_author": content.post_author,
            "from_scheduled": content.from_scheduled,
            "is_scheduled": content.is_scheduled,
            "edit_hide": content.edit_hide,
            "media_group_id": content.media_group_id,
            "text": content.text,
            "media_type": ChatMediaTypes.get_type(content.media_type)
        }
        if content.forward_header:
            r.update(
                {
                    "forward_date_ts": content.forward_header.date,
                    "forward_sender_name": content.forward_header.forward_sender_name,
                    "forward_from_message_id_orig": content.forward_header.forward_from_message_id,
                    "forward_signature": content.forward_header.forward_signature,
                    "saved_from_message_id_orig": content.forward_header.saved_from_message_id,
                }
            )

        if content.reply_header:
            r.update(
                {
                    'reply_to_message_id_orig': content.reply_header.reply_to_message_id,
                    'reply_to_top_message_id_orig': content.reply_header.reply_to_top_id,
                }
            )
        return r

    @staticmethod
    def create_restrictions(raw_message: types.Message, db_message: "Message"):
        if db_message and raw_message.restrictions:
            tg_models.Restriction.objects.bulk_create_restrictions(
                raw_restrictions=raw_message.restrictions,
                db_message=db_message,
            )


class Message(BaseModel, SoftDeletableBaseModel, ChatUpdater, UserUpdater, MessageUpdater):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:is_scheduled{0|1}:message_id:edit_date_ts|0`

    message_id = models.BigIntegerField()
    date_ts = models.BigIntegerField(null=True, blank=True)
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
    edit_date_ts = models.BigIntegerField(null=True, blank=True)
    is_outgoing = models.BooleanField(null=True, blank=True)
    mentioned = models.BooleanField(null=True, blank=True)
    is_silent = models.BooleanField(null=True, blank=True)
    is_post = models.BooleanField(null=True, blank=True)
    post_author = models.CharField(max_length=256, null=True, blank=True)
    from_scheduled = models.BooleanField(null=True, blank=True)
    is_scheduled = models.BooleanField(null=True, blank=True)  # whether this is a scheduled message or not
    edit_hide = models.BooleanField(null=True, blank=True)
    media_group_id = models.BigIntegerField(null=True, blank=True)
    sender_chat = models.ForeignKey(
        'telegram.Chat',
        related_name='sent_messages',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    # Sender, null for messages sent to channels or sender user got deleted
    user = models.ForeignKey(
        'telegram.User',
        related_name='sent_messages',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    # info from forward_header
    forward_date_ts = models.BigIntegerField(null=True, blank=True)
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

    is_deleted = models.BooleanField(default=False, null=False, )

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
    # `sent_message` : the scheduled message is this post is published from
    # `post_from_sent_message` : the post this message is published from
    # `post_from_scheduled_message` : the post this message is created of

    # Telegram account who logged this message
    logged_by = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='logged_messages',
    )

    is_scheduled_message_sent = models.BooleanField(null=True, blank=True)
    scheduled_message = models.OneToOneField(
        'telegram.Message',
        on_delete=models.CASCADE,
        related_name='sent_message',
        null=True,
        blank=True
    )

    objects = MessageManager()

    def update_fields_from_raw(
            self,
            *,
            raw_message: types.Message,
            chat_id: int,
            logger_account: "tg_models.TelegramAccount" = None
    ) -> bool:
        return Message.objects.update_from_raw(
            chat_id=chat_id,
            id=self.id,
            raw_message=raw_message,
            logger_account=logger_account
        )

    def update_sent_status(self):
        self.is_scheduled_message_sent = True
        self.save()

    class Meta:
        ordering = ('-date_ts', 'chat',)
        get_latest_by = ('-date_ts', 'chat',)

    def __str__(self):
        return f"message {self.message_id} from {self.chat}"
