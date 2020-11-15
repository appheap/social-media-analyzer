import typing
from timeit import timeit

from pyrogram import Client
from pyrogram.handlers import MessageHandler, RawUpdateHandler, UserStatusHandler, DisconnectHandler
from pyrogram.raw.types import ChannelAdminLogEventsFilter, InputMessagesFilterPhotos, InputMessagesFilterDocument, \
    InputMessagesFilterUrl, InputMessagesFilterRoundVideo, InputMessagesFilterGeo, InputMessagesFilterContacts, \
    InputMessagesFilterGif, InputMessagesFilterVoice, InputMessagesFilterMusic, InputMessagesFilterVideo, \
    ChannelParticipantsSearch
from pyrogram.raw.types.channels import AdminLogResults, ChannelParticipants, ChannelParticipantsNotModified
from pyrogram.types import User as User, Restriction as PGRestricion
from pyrogram.types import Dialog as Dialog
from pyrogram.types import Message as Message
from pyrogram.types import Chat as Chat
from pyrogram.types import Update as Update
from pyrogram.raw import functions, types
# from pyrogram.raw.types import *
import pyrogram.utils as utils
from pyrogram.errors import FloodWait
from pyrogram.methods.utilities.idle import idle
from pyrogram import errors as tg_errors
from pyrogram.methods.chats.get_chat_members import Filters
from pyrogram.types.user_and_chats.chat_member import ChatMember
#############################################################
import asyncio

#############################################
from datetime import datetime
import pytz
import time

#############################################
import json
import logging
from termcolor import colored
import re

#############################################

#############################################
from kombu import Connection, Exchange, Queue, Consumer, Producer
from kombu.mixins import ConsumerMixin, ConsumerProducerMixin

#############################################
from threading import Thread
from threading import RLock
import threading
from multiprocessing import Process
import multiprocessing as mp
#############################################
from social_media_analyzer.globals import logger
from telegram import globals as tg_globals
from telegram.client.client_manager import *
from telegram import tasks
#############################################

from django.core import exceptions
from django.db import DatabaseError, transaction
import arrow

#############################################
from utils.utils import prettify

TG_BAD_REQUEST = 'TG_BAD_REQUEST'
base_timezone = pytz.timezone('Asia/Tehran')

clients = []
clients_lock = RLock()


def get_class_name(object):
    return str(object.__class__.__name__)


class BaseResponse(object):
    def __init__(self):
        self.success = None
        self.message = None
        self.error_code = None
        self.data = None

    def done(self, message=None, data=None):
        self.success = True
        self.message = message
        self.data = data
        return self

    def fail(self, message: str = "No Telegram client is ready...", error_code: int = None):
        self.success = False
        self.message = message
        self.error_code = error_code
        return self


class DataBaseManager(object):
    tg_models = None
    tg_users = None

    _media_types = ['audio', 'document', 'photo', 'sticker', 'video', 'animation', 'voice', 'video_note', 'contact',
                    'location', 'venue']

    def __init__(self, clients: list):
        self.clients = clients
        from telegram import models
        self.tg_models = models

        from users import models
        self.users_models = models

    def disable_channel_analyzers_with_admin_required(self, db_chat, db_tg_channel):
        if db_tg_channel.is_active or db_tg_channel.is_account_admin:
            db_tg_channel.is_active = False
            db_tg_channel.is_account_admin = False
            db_tg_channel.save()

        if db_chat.admin_log_analyzer:
            db_chat.admin_log_analyzer.enabled = False
            db_chat.admin_log_analyzer.disabled_at = arrow.utcnow().timestamp
            db_chat.admin_log_analyzer.disable_reason = 'admin demoted'
            db_chat.admin_log_analyzer.save()

        if db_chat.members_analyzer:
            db_chat.members_analyzer.enabled = False
            db_chat.members_analyzer.disabled_at = arrow.utcnow().timestamp
            db_chat.members_analyzer.disable_reason = 'admin demoted'
            db_chat.members_analyzer.save()

    def create_db_admin_rights(self, chat_member: ChatMember, db_tg_admin_account=None, db_tg_channel=None):
        return self.tg_models.AdminRights.objects.create(
            is_latest=True,
            telegram_channel=db_tg_channel,
            admin=db_tg_admin_account,
            change_info=chat_member.can_change_info,
            post_messages=chat_member.can_post_messages,
            edit_messages=chat_member.can_edit_messages,
            delete_messages=chat_member.can_delete_messages,
            ban_users=chat_member.can_restrict_members,
            invite_users=chat_member.can_invite_users,
            pin_messages=chat_member.can_pin_messages,
            add_admins=chat_member.can_promote_members,
        )

    @staticmethod
    def update_membership_status(db_membership, db_participant):
        if not db_membership.current_status and not db_membership.previous_status:
            db_membership.current_status = db_participant
            db_membership.status_change_date = arrow.utcnow().timestamp
        elif (not db_membership.previous_status and db_membership.current_status) or \
                (db_membership.current_status and db_membership.previous_status):
            db_membership.previous_status = db_membership.current_status
            db_membership.current_status = db_participant
            db_membership.status_change_date = arrow.utcnow().timestamp
        db_membership.save()

    def create_channel_participant(self, chat_member: ChatMember, db_membership, client: Client):
        if not chat_member or not db_membership or not client:
            return
        _type = chat_member.status
        db_participant = self.tg_models.ChannelParticipant(
            user=self.get_or_create_db_tg_user(
                tg_user=chat_member.user,
                client=client,
            ),
            membership=db_membership,
        )
        if _type == 'member':
            db_participant.type = self.tg_models.ChannelParticipantTypes.member
            db_participant.user = self.get_or_create_db_tg_user(
                tg_user=chat_member.user,
                client=client,
            )
            db_participant.join_date = chat_member.joined_date

        elif _type == 'self':
            db_participant.type = self.tg_models.ChannelParticipantTypes.self
            db_participant.join_date = chat_member.joined_date
            db_participant.invited_by = self.get_or_create_db_tg_user(
                tg_user=chat_member.invited_by,
                client=client,
            )

        elif _type == 'creator':
            db_participant.type = self.tg_models.ChannelParticipantTypes.creator
            db_participant.rank = chat_member.title

        elif _type == 'administrator':
            db_participant.type = self.tg_models.ChannelParticipantTypes.administrator
            db_participant.join_date = chat_member.joined_date
            db_participant.invited_by = self.get_or_create_db_tg_user(
                tg_user=chat_member.invited_by,
                client=client,
            )
            db_participant.rank = chat_member.title
            db_participant.can_edit = chat_member.can_be_edited
            db_participant.promoted_by = self.get_or_create_db_tg_user(
                tg_user=chat_member.promoted_by,
                client=client,
            )
            db_participant.admin_rights = self.create_db_admin_rights(chat_member)

        elif _type == 'kicked':
            db_participant.type = self.tg_models.ChannelParticipantTypes.kicked
            db_participant.join_date = chat_member.joined_date
            db_participant.left = not chat_member.is_member
            db_participant.kicked_by = self.get_or_create_db_tg_user(
                tg_user=chat_member.restricted_by,
                client=client,
            )
            db_participant.banned_rights = self.create_chat_banned_rights(chat_member)

        elif _type == 'restricted':
            db_participant.type = self.tg_models.ChannelParticipantTypes.restricted
            db_participant.join_date = chat_member.joined_date
            db_participant.left = not chat_member.is_member
            db_participant.kicked_by = self.get_or_create_db_tg_user(
                tg_user=chat_member.restricted_by,
                client=client,
            )
            db_participant.banned_rights = self.create_chat_banned_rights(chat_member)

        db_participant.save()
        return db_participant

    def create_chat_banned_rights(self, chat_member: ChatMember):
        return self.tg_models.ChatBannedRight.objects.create(
            view_messages=chat_member.status == 'restricted',
            send_messages=chat_member.can_send_messages,
            send_media=chat_member.can_send_media_messages,
            send_stickers=chat_member.can_send_stickers,
            send_gifs=chat_member.can_send_animations,
            send_games=chat_member.can_send_games,
            send_inline=chat_member.can_use_inline_bots,
            embed_links=chat_member.can_add_web_page_previews,
            send_polls=chat_member.can_send_polls,
            change_info=chat_member.can_change_info,
            invite_users=chat_member.can_invite_users,
            pin_messages=chat_member.can_pin_messages,
            until_date=chat_member.until_date,
        )

    def get_or_create_membership(self, db_chat, db_user):
        if not db_chat or not db_user:
            return None
        try:
            membership = self.tg_models.Membership.objects.get(
                user=db_user,
                chat=db_chat,
            )
        except exceptions.ObjectDoesNotExist as e:
            membership = self.tg_models.Membership.objects.create(
                user=db_user,
                chat=db_chat,
            )
        except Exception as e:
            logger.exception(e)
            membership = None
        return membership

    def create_db_tg_account(self, client: Client, db_owner_user, tg_user: User):
        with transaction.atomic():
            db_tg_user = self.get_or_create_db_tg_user(tg_user, client)

            db_tg_admin_account = self.tg_models.TelegramAccount.objects.create(
                user_id=tg_user.id,
                username=tg_user.username.lower() if tg_user.username else None,
                first_name=getattr(tg_user, 'first_name', None),
                last_name=getattr(tg_user, 'first_name', None),
                is_bot=getattr(tg_user, 'is_bot', False),
                is_restricted=getattr(tg_user, 'is_restricted', False),
                is_scam=getattr(tg_user, 'is_scam', False),
                is_verified=getattr(tg_user, 'is_verified', False),
                is_deleted=getattr(tg_user, 'is_deleted', False),
                phone_number=getattr(tg_user, 'phone_number', None),
                dc_id=getattr(tg_user, 'dc_id', None),
                language_code=getattr(tg_user, 'language_code', False),
                api_id=client.api_id,
                api_hash=client.api_hash,
                session_name=client.session_name,
                custom_user=db_owner_user,
                telegram_user=db_tg_user,
            )

            return db_tg_admin_account

    def update_add_channel_request_status(self, db_admin, channel_username: str, db_tg_channel,
                                          tg_full_chat: Chat, db_request_owner):
        db_add_request = self.tg_models.AddChannelRequest.objects.create(
            done=False,
            custom_user=db_request_owner,
            channel_username=channel_username.lower(),
            telegram_account=db_admin,
            status=self.tg_models.AddChannelRequestStatusTypes.CHANNEL_MEMBER,
            telegram_channel=db_tg_channel,
            channel_id=tg_full_chat.id,
        )
        return db_add_request

    def get_or_create_db_tg_channel(self, db_admin_tg_account, db_chat, tg_full_chat, db_user):
        if not db_chat or not db_admin_tg_account or not tg_full_chat or not db_user:
            return None

        try:
            db_channel = self.tg_models.TelegramChannel.objects.get(
                channel_id=db_chat.chat_id,
                custom_user=db_user,
                telegram_account=db_admin_tg_account,
            )
        except exceptions.ObjectDoesNotExist as e:
            db_channel = self.tg_models.TelegramChannel.objects.create(
                channel_id=db_chat.chat_id,
                is_account_creator=tg_full_chat.is_creator,
                is_account_admin=False,
                username=db_chat.username.lower(),
                is_public=True,
                custom_user=db_user,
                telegram_account=db_admin_tg_account,
                chat=db_chat,
            )
        except Exception as e:
            logger.exception(e)
            db_channel = None

        return db_channel

    def create_entity_types(self, db_chat, db_message, message: Message):
        if not message:
            return None
        entities = message.entities if message.entities else message.caption_entities
        if not entities:
            return
        for entity in entities:
            _id = f"{db_chat.chat_id}:{db_message.message_id}:{entity.type}"
            try:
                db_entity_type = self.tg_models.EntityType.objects.get(id=_id)
            except exceptions.ObjectDoesNotExist as e:
                db_entity_type = self.tg_models.EntityType.objects.create(
                    id=_id,
                    type=self.tg_models.EntityTypes.get_type(entity),
                    message=db_message,
                )
            except Exception as e:
                logger.exception(e)

    def create_entities(self, client: Client, db_chat, db_message, message: Message):
        if not message:
            return None
        entities = message.entities if message.entities else message.caption_entities
        if not entities:
            return
        for entity in entities:
            _id = f"{db_chat.chat_id}:{db_message.message_id}:{entity.offset}"
            try:
                db_entity = self.tg_models.Entity.objects.get(id=_id)
            except exceptions.ObjectDoesNotExist as e:
                db_entity = self.tg_models.Entity.objects.create(
                    id=_id,
                    type=self.tg_models.EntityTypes.get_type(entity),
                    source=self.tg_models.EntitySourceTypes.text if message.entities else self.tg_models.EntitySourceTypes.caption,
                    offset=entity.offset,
                    length=entity.length,
                    message=db_message,
                    user=self.get_or_create_db_tg_user(entity.user, client, ),
                )
            except Exception as e:
                logger.exception(e)

    def fill_db_tg_user_attrs(self, db_tg_user, tg_user: User):
        db_tg_user.username = tg_user.username.lower() if tg_user.username else None
        db_tg_user.first_name = getattr(tg_user, 'first_name', None)
        db_tg_user.last_name = getattr(tg_user, 'last_name', None)
        db_tg_user.is_bot = getattr(tg_user, 'is_bot', False)
        db_tg_user.is_restricted = getattr(tg_user, 'is_restricted', False)
        db_tg_user.is_scam = getattr(tg_user, 'is_scam', False)
        db_tg_user.is_verified = getattr(tg_user, 'is_verified', False)
        db_tg_user.is_deleted = getattr(tg_user, 'is_deleted', False)
        db_tg_user.is_support = getattr(tg_user, 'is_support', False)
        db_tg_user.phone_number = getattr(tg_user, 'phone_number', None)
        db_tg_user.dc_id = getattr(tg_user, 'dc_id', None)
        db_tg_user.language_code = getattr(tg_user, 'language_code', None)

    def get_or_create_db_tg_user(self, tg_user: User, client: Client, update_current=False):
        if tg_user is None:
            return None
        try:
            db_tg_user = self.tg_models.User.objects.get(
                user_id=tg_user.id
            )
            if update_current:
                tg_user: User = client.get_users(tg_user.id)

                db_tg_user = self.tg_models.User.objects.get(user_id=tg_user.id)
                db_tg_user.user_id = tg_user.id
                self.fill_db_tg_user_attrs(db_tg_user, tg_user)
                db_tg_user.save()
                if db_tg_user.is_restricted:
                    self.create_db_restrictions(tg_user.restrictions, db_tg_user=db_tg_user)

        except exceptions.ObjectDoesNotExist as e:
            db_tg_user = self.tg_models.User.objects.create(
                user_id=tg_user.id,
            )
            self.fill_db_tg_user_attrs(db_tg_user, tg_user)
            db_tg_user.save()
            if db_tg_user.is_restricted:
                self.create_db_restrictions(tg_user.restrictions, db_tg_user=db_tg_user)
        except Exception as e:
            logger.exception(e)
            db_tg_user = None
        return db_tg_user

    def fill_db_tg_chat_attrs(self, db_tg_chat, tg_chat: Chat, db_creator_account, client: Client,
                              check_chat_type: bool):
        db_tg_chat.type = self.tg_models.ChatTypes.get_type(tg_chat.type)
        db_tg_chat.is_verified = getattr(tg_chat, 'is_verified', False)
        db_tg_chat.is_restricted = getattr(tg_chat, 'is_restricted', False)
        db_tg_chat.is_scam = getattr(tg_chat, 'is_scam', False)
        db_tg_chat.title = getattr(tg_chat, 'title', None)
        db_tg_chat.username = tg_chat.username.lower() if tg_chat.username else None
        db_tg_chat.description = getattr(tg_chat, 'description', None)
        db_tg_chat.dc_id = getattr(tg_chat, 'dc_id', None)
        if not check_chat_type:
            if tg_chat.linked_chat:
                db_tg_chat.linked_chat = self.get_or_create_db_tg_chat(
                    tg_chat.linked_chat,
                    db_creator_account,
                    client,
                    check_chat_type=True,
                )
            else:
                db_tg_chat.linked_chat = None

        db_tg_chat.invite_link = getattr(tg_chat, 'invite_link', None)
        db_tg_chat.creator_account = db_creator_account

    def get_or_create_db_tg_chat(self, tg_chat: Chat, db_creator_account, client: Client, update_current=False,
                                 is_tg_full_chat=False, check_chat_type=False):
        if tg_chat is None:
            return None
        _id = int(tg_chat.id)

        try:
            db_tg_chat = self.tg_models.Chat.objects.get(
                chat_id=_id
            )
            if update_current:
                if not is_tg_full_chat:
                    tg_chat: Chat = client.get_chat(tg_chat.id)
                db_tg_chat = self.tg_models.Chat.objects.get(chat_id=tg_chat.id)
                self.fill_db_tg_chat_attrs(db_tg_chat, tg_chat, db_creator_account, client, check_chat_type)
                db_tg_chat.save()
                if db_tg_chat.is_restricted:
                    self.create_db_restrictions(tg_chat.restrictions, db_tg_chat)

        except exceptions.ObjectDoesNotExist as e:
            if not is_tg_full_chat:
                # get the full chat info from telegram client
                tg_chat: Chat = client.get_chat(_id)
            try:
                db_tg_chat = self.tg_models.Chat.objects.create(
                    chat_id=_id,
                )
                self.fill_db_tg_chat_attrs(db_tg_chat, tg_chat, db_creator_account, client, check_chat_type)
                db_tg_chat.save()
                if db_tg_chat.is_restricted:
                    self.create_db_restrictions(tg_chat.restrictions, db_tg_chat)

            except Exception as e:
                logger.exception(e)
                db_tg_chat = None
        return db_tg_chat

    def get_message_media_type(self, message: Message):
        if getattr(message, 'media', False):
            for media_type in self._media_types:
                if hasattr(message, media_type):
                    return media_type
        else:
            return None

    @staticmethod
    def get_entity_types(message: Message):
        entity_types = set()
        if message.entities:
            for entity in message.entities:
                entity_types.add(entity.type)
        if message.caption_entities:
            for entity in message.caption_entities:
                entity_types.add(entity.type)
        return list(entity_types)

    def fill_db_tg_message_attrs(self, db_message, message, db_chat, client: Client, now: int):
        db_message.message_id = getattr(message, 'message_id', None)
        db_message.date = getattr(message, 'date', None)
        db_message.from_user = self.get_or_create_db_tg_user(getattr(message, 'from_user', None), client)
        db_message.forward_from = self.get_or_create_db_tg_user(getattr(message, 'forward_from', None), client)
        db_message.forward_sender_name = getattr(message, 'forward_sender_name', None)
        db_message.forward_from_chat = self.get_or_create_db_tg_chat(
            getattr(message, 'forward_from_chat', None),
            db_chat.creator_account,
            client,
        )
        db_message.forward_from_message_id = getattr(message, 'forward_from_message_id', None)
        db_message.forward_signature = getattr(message, 'forward_signature', None)
        db_message.forward_date = getattr(message, 'forward_date', None)
        db_message.reply_to_message = self.get_or_create_db_tg_message(
            getattr(message, 'reply_to_message', None), db_chat, client, now
        )
        db_message.mentioned = getattr(message, 'mentioned', False)
        db_message.empty = message.empty if message.empty else False
        db_message.emptied_at = now if db_message.empty else None
        db_message.edit_date = getattr(message, 'edit_date', None)
        db_message.media_group_id = getattr(message, 'media_group_id', None)
        db_message.author_signature = getattr(message, 'author_signature', None)
        db_message.text = getattr(message, 'text', None)
        db_message.caption = getattr(message, 'caption', None)
        db_message.via_bot = self.get_or_create_db_tg_user(getattr(message, 'via_bot', None), client)
        db_message.outgoing = getattr(message, 'outgoing', None)
        db_message.has_media = message.media if message.media else False
        db_message.media_type = self.get_message_media_type(message)
        db_message.chat = db_chat
        db_message.logged_by = db_chat.creator_account

    def get_or_create_db_tg_message(self, message: Message, db_chat, client: Client, now: int):
        if message is None:
            return None
        _id = f"{db_chat.chat_id}:{message.message_id}"

        try:
            db_message = self.tg_models.Message.objects.get(id=_id)
            if message.edit_date and getattr(message, 'edit_date', 0) > getattr(message, 'modified_at', 0):
                # message needs to be updated in the db
                self.fill_db_tg_message_attrs(db_message, message, db_chat, client, now)
                db_message.save()
        except exceptions.ObjectDoesNotExist as e:
            try:
                db_message = self.tg_models.Message(
                    id=_id,
                )
                self.fill_db_tg_message_attrs(db_message, message, db_chat, client, now)
                db_message.save()
            except Exception as e:
                logger.exception(e)
                db_message = None
        except Exception as e:
            logger.exception(e)
            db_message = None

        return db_message

    def create_db_restrictions(self, tg_restrictions, db_tg_chat=None, db_tg_user=None):
        now = arrow.utcnow().timestamp
        # delete previous restriction to add new ones
        self.tg_models.Restriction.objects.filter(chat=db_tg_chat, user=db_tg_user).update(
            is_deleted=True,
            deleted_at=now
        )

        for tg_restriction in tg_restrictions:
            tg_restriction: PGRestricion = tg_restriction
            _id = f"{'chat' if db_tg_chat else 'user'}:{db_tg_chat.chat_id if db_tg_chat else db_tg_user.user_id}"
            try:
                db_restriction = self.tg_models.Restriction.objects.get(
                    id=_id,
                    platform=tg_restriction.platform,
                    reason=tg_restriction.reason,
                    text=tg_restriction.text,
                    chat=db_tg_chat,
                    user=db_tg_user,
                )
                db_restriction.is_deleted = False
                db_restriction.deleted_at = None
                db_restriction.save()
            except exceptions.ObjectDoesNotExist as e:
                try:
                    db_restriction = self.tg_models.Restriction.objects.create(
                        id=_id,
                        platform=tg_restriction.platform,
                        reason=tg_restriction.reason,
                        text=tg_restriction.text,
                        chat=db_tg_chat,
                        user=db_tg_user,
                    )
                except Exception as e:
                    logger.exception(e)


class Worker(ConsumerProducerMixin, DataBaseManager):
    tg_exchange = tg_globals.tg_exchange
    info_queue = tg_globals.info_queue

    _search_filter_count = [InputMessagesFilterPhotos(), InputMessagesFilterVideo(),
                            InputMessagesFilterDocument(), InputMessagesFilterMusic(),
                            InputMessagesFilterUrl(), InputMessagesFilterVoice(),
                            InputMessagesFilterRoundVideo(), InputMessagesFilterGif(),
                            InputMessagesFilterGeo(), InputMessagesFilterContacts(), ]
    _filter_names = {'InputMessagesFilterPhotos': 'photo', 'InputMessagesFilterVideo': 'video',
                     'InputMessagesFilterDocument': 'document', 'InputMessagesFilterMusic': 'music',
                     'InputMessagesFilterUrl': 'url', 'InputMessagesFilterVoice': 'voice',
                     'InputMessagesFilterRoundVideo': 'video_note', 'InputMessagesFilterGif': 'animation',
                     'InputMessagesFilterGeo': 'location', 'InputMessagesFilterContacts': 'contact'}

    def __init__(self, connection, clients):
        self.connection = connection
        super().__init__(clients)

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=[self.info_queue], callbacks=[self.on_task])]

    def acquire_clients(self, func, *args, **kwargs):
        response = BaseResponse()
        with clients_lock as lock:
            if len(self.clients) != 0:
                return func(*args, **kwargs) if callable(func) else response.fail()
            else:
                return response.fail()

    def on_task(self, body, message):
        from utils.utils import prettify

        func = body['func']
        args = body['args']
        kwargs = body['kwargs']

        # logger.info(f'Got task: {prettify(body)}')
        response = BaseResponse()

        if func == 'task_init_clients':
            response = self.acquire_clients(self.task_init_clients, *args, **kwargs)

        elif func == 'task_get_me':
            response = self.acquire_clients(self.task_get_me, *args, **kwargs)

        elif func == 'task_add_tg_channel':
            response = self.acquire_clients(self.task_add_tg_channel, *args, **kwargs)

        elif func == 'task_iterate_dialogs':
            response = self.acquire_clients(self.task_iterate_dialogs, *args, **kwargs)

        elif func == 'task_analyze_chat_shared_medias':
            response = self.acquire_clients(self.task_analyze_chat_shared_medias, *args, **kwargs)

        elif func == 'task_analyze_chat_member_count':
            response = self.acquire_clients(self.task_analyze_chat_member_count, *args, **kwargs)

        elif func == 'task_analyze_message_views':
            response = self.acquire_clients(self.task_analyze_message_views, *args, **kwargs)

        elif func == 'task_analyze_admin_logs':
            response = self.acquire_clients(self.task_analyze_admin_logs, *args, **kwargs)

        elif func == 'task_analyze_all_chat_members':
            response = self.acquire_clients(self.task_analyze_all_chat_members, *args, **kwargs)

        elif func == 'task_analyze_chat_members':
            response = self.acquire_clients(self.task_analyze_chat_members, *args, **kwargs)

        self.producer.publish(
            body=prettify(response, include_class_name=False),
            exchange='', routing_key=message.properties['reply_to'],
            correlation_id=message.properties['correlation_id'],
            serializer='json',
            retry=True,
        )
        message.ack()

    def task_get_me(self, *args, **kwargs):
        data = {}
        for client in clients:
            client: Client = client
            data.update({
                str(client.session_name): str(client.get_me())
            })
        return BaseResponse().done(data=data)

    def task_init_clients(self, *args, **kwargs):
        tg_accounts_to_be_iterated = []
        for client in self.clients:
            client: Client = client
            custom_user = self.users_models.CustomUser.objects.get(username='sigma')
            me: User = client.get_me()
            try:
                db_tg_admin_account = self.tg_models.TelegramAccount.objects.get(user_id=me.id, is_deleted=False)
            except exceptions.ObjectDoesNotExist as e:
                logger.exception(e)
                db_tg_admin_account = self.create_db_tg_account(client, custom_user, me)

            # update chats table for each account
            tg_accounts_to_be_iterated.append(db_tg_admin_account.user_id)
        tasks.iterate_dialogs.apply_async(
            kwargs={
                'tg_account_ids': tg_accounts_to_be_iterated,
            },
            countdown=0,
        )

        return BaseResponse().done(message='client init successful')

    def task_iterate_dialogs(self, *args, **kwargs):
        response = BaseResponse()
        ids = []
        try:
            tg_account_ids = kwargs['tg_account_ids']
            db_tg_accounts = self.tg_models.TelegramAccount.objects.filter(
                user_id__in=tg_account_ids,
                is_deleted=False,
            )
        except Exception as e:
            logger.exception(e)
            response.fail('missing `tg_account_ids` kwarg')
        else:
            if not db_tg_accounts or not len(db_tg_accounts):
                return response.fail('no telegram account is available now')

            session_names = [db_tg_account.session_name for db_tg_account in db_tg_accounts]
            for client in self.clients:
                client: Client = client
                if client.session_name in session_names:
                    db_tg_admin_account = self.tg_models.TelegramAccount.objects.get(
                        session_name=client.session_name,
                        is_deleted=False,
                    )
                    for dialog in client.get_dialogs():
                        if dialog.chat.type == 'channel' and dialog.chat.username is not None:
                            db_chat = self.get_or_create_db_tg_chat(
                                dialog.chat,
                                db_tg_admin_account,
                                client,
                                update_current=True,
                                is_tg_full_chat=False,
                            )
                            if db_chat:
                                db_tg_channel = self.get_or_create_db_tg_channel(
                                    db_tg_admin_account,
                                    db_chat,
                                    dialog.chat,
                                    self.users_models.CustomUser.objects.get(username='sigma', is_superuser=True),
                                )
                                try:
                                    admins = client.get_chat_members(db_chat.chat_id, filter=Filters.ADMINISTRATORS)
                                except tg_errors.ChatAdminRequired as e:
                                    # client is not admin of this channel, update telegram account related to this channel
                                    self.disable_channel_analyzers_with_admin_required(db_chat, db_tg_channel)
                                except Exception as e:
                                    logger.exception(e)
                                else:
                                    # update memberships for this channel
                                    ids.append(db_chat.chat_id)
        response.done()
        if len(ids):
            tasks.analyze_chat_members.apply_async(
                kwargs={
                    'only_admins': False,
                    'chat_ids': ids,
                },
                countdown=0,
            )
        return response

    def task_add_tg_channel(self, *args, **kwargs):
        db_tg_account_admin_id = kwargs['db_tg_account_admin_id']
        channel_username = str(kwargs['channel_username']).lower()
        db_userid = kwargs['db_userid']
        response = BaseResponse()
        try:
            db_request_owner = self.users_models.CustomUser.objects.get(pk=db_userid)
        except exceptions.ObjectDoesNotExist as e:
            logger.exception(e)
            response.fail('No such user')
        else:
            try:
                db_tg_admin_account = self.tg_models.TelegramAccount.objects.get(user_id=db_tg_account_admin_id,
                                                                                 is_deleted=False)
            except exceptions.ObjectDoesNotExist as e:
                logger.exception(e)
                response.fail('no such tg account')
            else:
                for client in clients:
                    if client.session_name == db_tg_admin_account.session_name:
                        client: Client = client
                        if client.is_connected:
                            try:
                                db_tg_channel = \
                                    self.tg_models.TelegramChannel.objects.get(
                                        username=channel_username,
                                        is_deleted=False
                                    )
                            except exceptions.ObjectDoesNotExist as e:
                                logger.exception(e)
                                try:
                                    tg_chat: Chat = client.get_chat(channel_username)

                                except tg_errors.BadRequest as e:
                                    logger.exception(e)
                                    if type(e) == tg_errors.ChannelsTooMuch:
                                        response.fail('Admin has joined too many channels or supergroups')
                                    else:
                                        response.fail(TG_BAD_REQUEST)
                                else:
                                    if tg_chat.type == 'channel' and tg_chat.username:
                                        try:
                                            tg_full_chat: Chat = client.get_chat(tg_chat.id)
                                            client.join_chat(channel_username)
                                        except tg_errors.RPCError as e:
                                            logger.exception(e)
                                            response.fail(TG_BAD_REQUEST)
                                        else:
                                            try:
                                                with transaction.atomic():
                                                    db_chat = self.get_or_create_db_tg_chat(tg_full_chat,
                                                                                            db_tg_admin_account,
                                                                                            client)
                                                    db_tg_channel = self.get_or_create_db_tg_channel(
                                                        db_tg_admin_account,
                                                        db_chat,
                                                        tg_full_chat,
                                                        db_request_owner,
                                                    )

                                                    db_add_request = self.update_add_channel_request_status(
                                                        db_tg_admin_account, channel_username, db_tg_channel,
                                                        tg_full_chat,
                                                        db_request_owner)

                                                    response.done('joined channel')

                                            except DatabaseError as e:
                                                logger.exception(e)
                                                response.fail('DB_ERROR')
                                    else:
                                        response.fail('Only public channels can be added')
                            else:
                                response.fail('this channel is already added')


                        else:
                            response.fail('Sorry, that Admin account is not connected now.')
                        break
                else:
                    response.fail('Sorry, that Admin account is not connected now.')

        return response

    ########################################

    def task_analyze_message_views(self, *args, **kwargs):
        response = BaseResponse()

        chats = self.tg_models.Chat.objects.filter(message_view_analyzer__isnull=False,
                                                   message_view_analyzer__enabled=True)
        for db_chat in chats:
            analyzer = db_chat.message_view_analyzer
            now = arrow.utcnow().timestamp

            for client in clients:
                if client.session_name == db_chat.creator_account.session_name:
                    client: Client = client
                    if client.is_connected:
                        try:
                            for message in client.iter_history(db_chat.chat_id):
                                message: Message = message
                                if not message.service:
                                    try:
                                        now = arrow.utcnow().timestamp
                                        with transaction.atomic():
                                            db_message = self.get_or_create_db_tg_message(message, db_chat, client, now)
                                            db_message_view = self.tg_models.MessageView.objects.create(
                                                id=f"{db_chat.chat_id}:{message.message_id}:{now}",
                                                date=now,
                                                views=message.views,
                                                message=db_message,
                                                logged_by=db_chat.creator_account,
                                                chat=db_chat,
                                            )
                                            self.create_entities(client, db_chat, db_message, message)
                                            self.create_entity_types(db_chat, db_message, message)

                                    except Exception as e:
                                        logger.exception(e)
                                    else:
                                        pass

                        except Exception as e:
                            logger.exception(e)
                            response.fail('TG_ERROR')
                        else:
                            response.done('logged message views')
                    else:
                        response.fail('client is not connected now')
                    break
            else:
                response.fail('no client is ready')
                break

            if response.success:
                if not analyzer.first_analyzed_at:
                    analyzer.first_analyzed_at = now
                analyzer.last_analyzed_at = now
                analyzer.save()
        return response

    def task_analyze_chat_member_count(self, *args, **kwargs):
        response = BaseResponse()

        chats = self.tg_models.Chat.objects.filter(member_count_analyzer__isnull=False,
                                                   member_count_analyzer__enabled=True)
        for db_chat in chats:
            analyzer = db_chat.member_count_analyzer
            now = arrow.utcnow().timestamp
            for client in clients:
                if client.session_name == db_chat.creator_account.session_name:
                    client: Client = client
                    if client.is_connected:
                        try:
                            tg_chat: Chat = client.get_chat(chat_id=db_chat.chat_id)
                        except Exception as e:
                            response.fail('TG_ERROR')
                            logger.exception(e)
                        else:
                            try:
                                now = arrow.utcnow().timestamp
                                self.tg_models.ChatMemberCount.objects.create(
                                    id=f"{db_chat.chat_id}:{db_chat.creator_account.user_id}:{now}",
                                    count=tg_chat.members_count,
                                    date=now,
                                    chat=db_chat,
                                    logged_by=db_chat.creator_account,
                                )
                            except Exception as e:
                                logger.exception(e)
                                response.fail('DB_ERROR')
                            else:
                                response.done('logged chat member count')
                    else:
                        response.fail('client is not connected now')
                    break
            else:
                response.fail('no client is ready')
                break

            if response.success:
                if not analyzer.first_analyzed_at:
                    analyzer.first_analyzed_at = now
                analyzer.last_analyzed_at = now
                analyzer.save()

        return response

    def task_analyze_chat_shared_medias(self, *args, **kwargs):
        response = BaseResponse()

        chats = self.tg_models.Chat.objects.filter(shared_media_analyzer__isnull=False,
                                                   shared_media_analyzer__enabled=True)
        for db_chat in chats:
            analyzer = db_chat.shared_media_analyzer
            now = arrow.utcnow().timestamp
            for client in clients:
                if client.session_name == db_chat.creator_account.session_name:
                    client: Client = client
                    if client.is_connected:
                        res = client.send(
                            functions.messages.GetSearchCounters(peer=client.resolve_peer(db_chat.chat_id),
                                                                 filters=self._search_filter_count)
                        )
                        if res:
                            count_dict = {}
                            for counter in res:
                                count_dict[self._filter_names[counter.filter.__class__.__name__]] = counter.count
                            if count_dict:
                                try:
                                    now = arrow.utcnow().timestamp
                                    self.tg_models.ChatSharedMedia.objects.create(
                                        id=f"{db_chat.chat_id}:{db_chat.creator_account.user_id}:{now}",
                                        date=now,
                                        photo=count_dict['photo'],
                                        video=count_dict['video'],
                                        document=count_dict['document'],
                                        music=count_dict['music'],
                                        url=count_dict['url'],
                                        voice=count_dict['voice'],
                                        video_note=count_dict['video_note'],
                                        animation=count_dict['animation'],
                                        location=count_dict['location'],
                                        contact=count_dict['contact'],
                                        chat=db_chat,
                                        logged_by=db_chat.creator_account,
                                    )
                                except Exception as e:
                                    logger.exception(e)
                                    response.fail('DB_ERROR')
                                else:
                                    response.done('logged shared media counts')
                    else:
                        response.fail('client is not connected now')
                    break
            else:
                response.fail('no client is ready')
                break

            if response.success:
                if not analyzer.first_analyzed_at:
                    analyzer.first_analyzed_at = now
                analyzer.last_analyzed_at = now
                analyzer.save()

        return response

    def task_analyze_chat_members(self, *args, **kwargs):
        response = BaseResponse()
        only_admins = kwargs.get('only_admins', False)
        chat_ids = kwargs.get('chat_ids', None)
        if chat_ids:
            for chat_id in chat_ids:
                try:
                    db_chat = self.tg_models.Chat.objects.get(
                        chat_id=chat_id,
                    )
                except exceptions.ObjectDoesNotExist as e:
                    response.fail(f"Chat with `chat_id`:{chat_id} does not exists")
                except Exception as e:
                    logger.exception(e)
                    response.fail('UNKNOWN_ERROR')
                else:
                    if db_chat.members_analyzer and db_chat.members_analyzer.enabled:
                        for client in clients:
                            if client.session_name == db_chat.creator_account.session_name:
                                client: Client = client
                                if client.is_connected:
                                    response = self.analyze_chat_members(
                                        client,
                                        db_chat,
                                        response,
                                        Filters.ADMINISTRATORS if only_admins else None,
                                    )
                                else:
                                    response.fail('client is not connected now')
                                break
                        else:
                            response.fail('no client is ready')
                    else:
                        response.fail(f'Chat with `chat_id`:{chat_id} does not have an enabled `member_analyzer`')
        else:
            response.fail('KeyError: No `chat_ids` in kwargs')

        return response

    def task_analyze_all_chat_members(self, *args, **kwargs):
        response = BaseResponse()
        chats = self.tg_models.Chat.objects.filter(members_analyzer__isnull=False,
                                                   members_analyzer__enabled=True)
        for db_chat in chats:
            analyzer = db_chat.members_analyzer
            now = arrow.utcnow().timestamp
            for client in clients:
                if client.session_name == db_chat.creator_account.session_name:
                    client: Client = client
                    if client.is_connected:
                        response = self.analyze_chat_members(client, db_chat, response)
                    else:
                        response.fail('client is not connected now')
                    break
            else:
                response.fail('no client is ready')
                break

            if response.success:
                if not analyzer.first_analyzed_at:
                    analyzer.first_analyzed_at = now
                analyzer.last_analyzed_at = now
                analyzer.save()

        return response

    def task_analyze_admin_logs(self, *args, **kwargs):
        response = BaseResponse()

        return response

    def analyze_chat_members(self, client: Client, db_chat, response: BaseResponse, _filter=None):
        try:
            for chat_member in client.iter_chat_members(db_chat.chat_id, filter=_filter if _filter else Filters.ALL):
                chat_member: ChatMember = chat_member
                new_status = chat_member.status
                try:
                    db_user = self.tg_models.User.objects.get(
                        user_id=chat_member.user.id
                    )
                except exceptions.ObjectDoesNotExist as e:
                    # user and membership does not exist, create them
                    tg_user = chat_member.user
                    db_user = self.get_or_create_db_tg_user(tg_user, client)
                    db_membership = self.get_or_create_membership(db_chat, db_user)
                    db_participant = self.create_channel_participant(
                        chat_member,
                        db_membership,
                        client,
                    )
                    self.update_membership_status(db_membership, db_participant)
                    response.done()
                else:
                    try:
                        db_membership = self.tg_models.Membership.objects.get(
                            user=db_user,
                            chat=db_chat,
                        )
                    except exceptions.ObjectDoesNotExist as e:
                        # membership does not exists, create it
                        db_membership = self.get_or_create_membership(db_chat, db_user)
                        db_participant = self.create_channel_participant(
                            chat_member,
                            db_membership,
                            client,
                        )
                        self.update_membership_status(db_membership, db_participant)
                        response.done()
                    else:
                        # logger.info(f"{db_membership} : {db_membership.current_status.type}, {new_status}")
                        if db_membership.current_status and db_membership.current_status.type != new_status:
                            db_participant = self.create_channel_participant(
                                chat_member,
                                db_membership,
                                client,
                            )
                            self.update_membership_status(db_membership, db_participant)

                        response.done()
        except tg_errors.RPCError as e:
            logger.exception(e)
            response.fail('TG_ERROR')
        except Exception as e:
            logger.exception(e)
            response.fail('UNKNOWN_ERROR')

        return response

    ########################################


class TelegramConsumerManager(Thread):
    def __init__(self, clients):
        Thread.__init__(self)
        self.clients = clients
        self.daemon = True
        self.name = 'Telegram_Consumer_Manager_Thread'

    def run(self) -> None:
        Worker(connection=Connection('amqp://localhost'), clients=clients).run()
        logger.info(f"Telegram Consumer started ....")


class TelegramClientManager():
    tg_models = None

    def __init__(self, clients: list):
        # threading.Thread.__init__(self)
        self.clients = clients
        self.name = 'telegram_client_thread'
        self.names = [
            "ChannelParticipantSelf",
            "ChannelParticipant",
        ]
        from telegram import models
        self.tg_models = models

    def on_disconnect(self, client: Client):
        import arrow
        logger.info(f"client {client.session_name} disconnected @ {arrow.utcnow()}")

    def on_message(self, client: Client, message: Message):
        # logger.info('on_message:: %s : %s' % (mp.current_process().name, threading.current_thread().name))
        logger.info(f"in on_message : {threading.current_thread()}")
        logger.info(message)

    def on_raw_update(self, client: Client, update, users, chats):
        logger.info(f"in on_raw_update : {threading.current_thread()}")
        # if 'message' not in update_name and 'status' not in update_name:
        # if 'updateNewMessage' in update_name and 'MessageService' in str(type(update.message)):

        # logger.info(f"{type(update), type(update.message) if hasattr(update, 'message') else 'empty'}")
        # logger.info(str(type(update.message)))

        # if hasattr(update, 'message') and update.message.__class__.__name__ == 'MessageService':
        logger.info("\n")
        logger.info("*" * 30)
        logger.info(update)
        logger.info("\n")
        if get_class_name(update) == 'UpdateChannel':
            self.handle_channel_update(client, update)
        else:
            pass
        logger.info("*" * 30)

    # noinspection PyTypeChecker
    def handle_channel_update(self, client: Client, update):
        channel_id = int('-100' + str(update.channel_id))
        try:
            admin_logs: AdminLogResults = client.send(
                functions.channels.GetAdminLog(
                    channel=client.resolve_peer(peer_id=channel_id),
                    q="",
                    min_id=0,
                    max_id=0,
                    events_filter=ChannelAdminLogEventsFilter(promote=True, demote=True),
                    admins=None,
                    limit=1
                )
            )
            logger.info(admin_logs)
        except tg_errors.RPCError as e:
            logger.exception(e)
            # this tg_account was demoted to participant;
            self.disable_tg_channel(channel_id, client)
        else:
            from pyrogram.raw.types import User as PGuser
            from pyrogram.raw.types import \
                ChannelAdminLogEventActionParticipantToggleAdmin as PGaction_toggle_admin
            for user in admin_logs.users:
                user: PGuser = user
                try:
                    tg_admin: TelegramClientManager.tg_models.TelegramAccount = self.tg_models.TelegramAccount.objects.get(
                        user_id=user.id,
                        is_deleted=False,
                        session_name=client.session_name
                    )
                except exceptions.ObjectDoesNotExist as e:
                    pass
                else:
                    for admin_log_event in admin_logs.events:
                        action = admin_log_event.action
                        action_class_name = get_class_name(action)
                        logger.info(action_class_name)
                        if action_class_name == "ChannelAdminLogEventActionParticipantToggleAdmin":
                            action: PGaction_toggle_admin = admin_log_event.action
                            if action.prev_participant.user_id == tg_admin.user_id and action.new_participant.user_id == tg_admin.user_id:
                                if get_class_name(action.prev_participant) in self.names and get_class_name(
                                        action.new_participant) == "ChannelParticipantAdmin":
                                    # this tg_account was promoted to admin;
                                    self.handle_tg_account_promotion(action, channel_id, tg_admin)

                                elif get_class_name(action.new_participant) in self.names and get_class_name(
                                        action.prev_participant) == "ChannelParticipantAdmin":
                                    # this tg_account was demoted to participant;
                                    pass
                                elif get_class_name(
                                        action.new_participant) == "ChannelParticipantAdmin" and get_class_name(
                                    action.prev_participant) == "ChannelParticipantAdmin":
                                    # this tg_account's admin rights was changed
                                    self.handle_admin_rights_update(action, channel_id, tg_admin)

    def handle_admin_rights_update(self, action, channel_id: int, tg_admin):
        admin_rights = action.new_participant.admin_rights
        try:
            tg_channel = self.tg_models.TelegramChannel.objects.get(
                channel_id=channel_id,
                is_deleted=False,
                telegram_account=tg_admin,
            )
        except exceptions.ObjectDoesNotExist as e:
            logger.exception(e)
        else:
            with transaction.atomic():
                self.update_old_admin_rights(tg_admin, tg_channel)
                self.save_admin_rights(admin_rights, tg_admin, tg_channel)

    def handle_tg_account_promotion(self, action, channel_id: int, tg_admin):
        admin_rights = action.new_participant.admin_rights
        with transaction.atomic():
            self.complete_add_channel_request_status(channel_id, tg_admin)
            tg_channel = self.enable_tg_channel(channel_id, tg_admin)
            self.save_admin_rights(admin_rights, tg_admin, tg_channel)

    def enable_tg_channel(self, channel_id: int, tg_admin):
        tg_channel = self.tg_models.TelegramChannel.objects.get(
            channel_id=channel_id,
            is_deleted=False,
            telegram_account=tg_admin,
        )
        tg_channel.is_account_admin = True
        tg_channel.is_active = True  # TODO what's the goal of having this ?
        tg_channel.save()
        return tg_channel

    def complete_add_channel_request_status(self, channel_id: int, tg_admin):
        requests = self.tg_models.AddChannelRequest.objects.filter(
            done=False,
            channel_id=channel_id,
            telegram_account=tg_admin,
        )
        for request in requests:
            request.status = self.tg_models.AddChannelRequestStatusTypes.CHANNEL_ADMIN
            request.done = True
            request.save()

    def disable_tg_channel(self, channel_id: int, client: Client):
        """
        Disable all channels related to this client because client was demoted to normal participant.

        :param channel_id: ID of the telegram channel
        :param client: Client that was admin of this channel
        :return:
        """
        try:
            tg_admin = self.tg_models.TelegramAccount.objects.get(
                session_name=client.session_name,
                is_deleted=False,
            )
        except exceptions.ObjectDoesNotExist as e:
            logger.exception(e)
        else:
            tg_channels = self.tg_models.TelegramChannel.objects.filter(
                channel_id=channel_id,
                is_deleted=False,
                telegram_account=tg_admin,
            )
            for tg_channel in tg_channels:
                tg_channel.is_account_admin = False
                tg_channel.is_active = False  # TODO what's the goal of having this ?
                tg_channel.save()

    def save_admin_rights(self, admin_rights, tg_admin, tg_channel, is_latest=True):
        tg_admin_rights_new = self.tg_models.AdminRights(
            change_info=admin_rights.change_info,
            post_messages=admin_rights.change_info,
            edit_messages=admin_rights.edit_messages,
            delete_messages=admin_rights.delete_messages,
            ban_users=admin_rights.ban_users,
            invite_users=admin_rights.invite_users,
            pin_messages=admin_rights.pin_messages,
            add_admins=admin_rights.add_admins,
            is_latest=is_latest,
            admin=tg_admin,
            telegram_channel=tg_channel
        )
        tg_admin_rights_new.save()

    def update_old_admin_rights(self, tg_admin, tg_channel):
        old_admin_rights = self.tg_models.AdminRights.objects.filter(
            admin=tg_admin,
            telegram_channel=tg_channel,
            is_latest=True,
        )
        for old_rights in old_admin_rights:
            old_rights.is_latest = False
            old_rights.save()

    def run(self) -> None:
        logger.info(mp.current_process().name)
        logger.info(threading.current_thread())

        for client in map(get_client, client_names, [False] * len(client_names)):
            client.start()
            with clients_lock:
                self.clients.append(client)
            me = str(client.get_me())
            logger.info(me)
            client.add_handler(DisconnectHandler(self.on_disconnect))
            client.add_handler(MessageHandler(self.on_message))
            client.add_handler(RawUpdateHandler(self.on_raw_update))

        idle()
        with clients_lock:
            for client in clients:
                client.stop()


def init_consumer():
    global clients
    TelegramConsumerManager(clients).start()

    TelegramClientManager(clients).run()
