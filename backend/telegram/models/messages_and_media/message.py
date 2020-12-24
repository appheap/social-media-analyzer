from typing import Optional

from django.db import models
from ..base import BaseModel
from pyrogram import types
from db.models import SoftDeletableBaseModel
from db.models import SoftDeletableQS
from django.db import DatabaseError
from telegram.globals import logger
from ..chats import ChatUpdater
from ..users import UserUpdater
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

    def filter_by_id(self, *, id: str) -> "MessageQuerySet":
        return self.filter(id=id)

    def update_or_create_message(self, **kwargs) -> Optional["Message"]:
        try:
            return self.update_or_create(
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

    def update_or_create_from_raw(
            self,
            *,
            chat_id: int,
            raw_message: types.Message,
            logger_account: "tg_models.TelegramAccount"
    ) -> Optional["Message"]:

        if chat_id is None or not raw_message or not logger_account:
            return None
        parsed_msg = self._parse_normal(
            chat_id=chat_id,
            raw_message=raw_message
        )

        if parsed_msg and len(parsed_msg):
            db_message = self.get_queryset().update_or_create_message(
                **{
                    **parsed_msg,
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
            chat_id=chat_id,
            raw_message=raw_message
        )

        if parsed_msg and len(parsed_msg):
            del parsed_msg['id']
            if logger_account:
                parsed_msg['logged_by'] = logger_account

            db_message = self.get_queryset().filter_by_id(id=id).update_message(
                **parsed_msg
            )

            self._update_message_related_models(db_message, raw_message)
            return db_message

        return False

    @staticmethod
    def _update_message_related_models(db_message, raw_message):
        if db_message and raw_message:
            db_message.update_or_create_chat_from_raw(
                model=db_message,
                field_name='from_chat',
                raw_chat=raw_message.content.from_chat
            )
            db_message.update_or_create_user_from_raw(
                model=db_message,
                field_name='from_user',
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

    @staticmethod
    def _parse_normal(*, chat_id, raw_message: types.Message) -> dict:
        if not raw_message:
            return {}

        content = raw_message.content
        if not content or raw_message.type != 'message':
            return {}

        r = {
            'id': f"{chat_id}:{raw_message.id}:{getattr(raw_message.content, 'edit_date', 0)}",
            'message_id': raw_message.id,
            'date_ts': raw_message.date,
            'type': MessageTypes.message,
            "edit_date_ts": content.edit_date,
            "is_outgoing": content.is_outgoing,
            "mentioned": content.mentioned,
            "is_silent": content.is_silent,
            "is_post": content.is_post,
            "post_author": content.post_author,
            "from_scheduled": content.from_scheduled,
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
        return


class Message(BaseModel, SoftDeletableBaseModel, ChatUpdater, UserUpdater):
    id = models.CharField(max_length=256, primary_key=True)  # `chat_id:message_id:edit_date_ts|0`

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

    # Telegram account who logged this message
    logged_by = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='logged_messages',
    )

    objects = MessageManager()

    def update_fields_from_raw(
            self,
            *,
            raw_message: types.Message,
            chat_id: int,
            logger_account: "tg_models.TelegramAccount" = None
    ) -> bool:
        return self.objects.update_from_raw(
            chat_id=chat_id,
            id=self.id,
            raw_message=raw_message,
            logger_account=logger_account
        )

    class Meta:
        ordering = ('-date_ts', 'chat',)
        get_latest_by = ('-date_ts', 'chat',)

    def __str__(self):
        return f"message {self.message_id} from {self.chat}"
