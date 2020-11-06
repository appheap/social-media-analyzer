import typing
from pyrogram import Client
from pyrogram.handlers import MessageHandler, RawUpdateHandler, UserStatusHandler, DisconnectHandler
from pyrogram.raw.types import ChannelAdminLogEventsFilter
from pyrogram.types import User as User
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
from telegram.client.client_manager import *
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

#############################################

from django.core import exceptions
from django.db import DatabaseError, transaction

#############################################

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


class Worker(ConsumerProducerMixin):
    tg_exchange = tg_globals.tg_exchange
    info_queue = tg_globals.info_queue

    def __init__(self, connection, clients):
        self.connection = connection
        self.clients = clients
        from telegram import models
        self.tg_models = models

        from users import models
        self.users_models = models

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
        from telegram import models
        from users.models import CustomUser
        from utils.utils import prettify

        func = body['func']
        args = body['args']
        kwargs = body['kwargs']

        logger.info(f'Got task: {prettify(body)}')
        response = BaseResponse()

        if func == 'init_clients':
            response = self.acquire_clients(self.handle_init_clients, *args, **kwargs)

        elif func == 'get_me':
            response = self.acquire_clients(self.handle_get_me, *args, **kwargs)

        elif func == 'request_add_tg_channel':
            response = self.acquire_clients(self.handle_add_tg_channel, *args, **kwargs)

        elif func == 'iterate_dialogs':
            with clients_lock:
                if len(self.clients) != 0:
                    for client in self.clients:
                        client: Client = client

                        for dialog in client.iter_dialogs():
                            if dialog.chat.type == 'channel' and dialog.chat.username is not None:
                                logger.info(dialog.chat.title)
                                try:
                                    db_tg_admin_account = models.TelegramAccount.objects.filter(user_id=1)[0]
                                    admins = client.get_chat_members(chat_id=dialog.chat.id,
                                                                     filter=Filters.ADMINISTRATORS)
                                    tg_chat: Chat = client.get_chat(dialog.chat.id)
                                    tg_chat = models.Chat(
                                        chat_id=tg_chat.id,
                                        type=models.ChatTypes.CHANNEL,
                                        is_verified=tg_chat.is_verified,
                                        is_restricted=tg_chat.is_restricted,
                                        is_scam=tg_chat.is_scam,
                                        is_support=tg_chat.is_support,
                                        title=tg_chat.title,
                                        username=tg_chat.username,
                                        description=tg_chat.description,
                                        dc_id=tg_chat.dc_id,
                                        invite_link=tg_chat.invite_link,
                                    )
                                    tg_chat.save()
                                    logger.info(tg_chat)
                                    logger.info("\n" * 5)
                                    channel = models.TelegramChannel(
                                        channel_id=tg_chat.chat_id,
                                        is_account_creator=tg_chat.is_creator,
                                        is_account_admin=True,
                                        username=tg_chat.username,
                                        is_public=True,
                                        chat=tg_chat,
                                        telegram_account=db_tg_admin_account,
                                        custom_user=CustomUser.objects.filter(username='sigma')[0],
                                    )
                                    channel.save()
                                    for admin in admins:
                                        admin: ChatMember = admin
                                    time.sleep(5)
                                except Exception as e:
                                    logger.exception(e)
                                    pass

                    response.done()
                else:
                    response.fail()

        logger.info(prettify(response, include_class_name=False))

        from utils.utils import prettify
        self.producer.publish(
            body=prettify(response, include_class_name=False),
            exchange='', routing_key=message.properties['reply_to'],
            correlation_id=message.properties['correlation_id'],
            serializer='json',
            retry=True,
        )
        message.ack()

    def handle_get_me(self, *args, **kwargs):
        data = {}
        for client in clients:
            client: Client = client
            data.update({
                str(client.session_name): str(client.get_me())
            })
        return BaseResponse().done(data=data)

    def handle_init_clients(self, *args, **kwargs):
        for client in self.clients:
            client: Client = client
            custom_user = self.users_models.CustomUser.objects.get(username='sigma')
            me: User = client.get_me()
            try:
                db_tg_admin_account = self.tg_models.TelegramAccount.objects.get(user_id=me.id, is_deleted=False)
            except exceptions.ObjectDoesNotExist as e:
                logger.exception(e)
                self.save_new_account(client, custom_user, me)

        return BaseResponse().done(message='client init successful')

    def handle_add_tg_channel(self, *args, **kwargs):
        admin_userid = kwargs['admin_userid']
        channel_username = kwargs['channel_username']
        userid = kwargs['userid']
        response = BaseResponse()
        try:
            db_tg_admin_account = self.tg_models.TelegramAccount.objects.get(user_id=admin_userid, is_deleted=False)
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
                            response.fail('this channel is already added')
                        except exceptions.ObjectDoesNotExist as e:
                            logger.exception(e)
                            try:
                                tg_chat: Chat = client.get_chat(channel_username)
                                logger.info(tg_chat)

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
                                        logger.info(tg_full_chat)
                                    except tg_errors.RPCError as e:
                                        logger.exception(e)
                                        response.fail(TG_BAD_REQUEST)
                                    else:
                                        try:
                                            with transaction.atomic():
                                                if tg_full_chat.linked_chat:
                                                    linked_chat: Chat = client.get_chat(
                                                        tg_full_chat.linked_chat.id)
                                                    db_linked_chat = self.save_chat(linked_chat)
                                                    db_chat = self.save_chat(tg_full_chat, db_linked_chat)
                                                else:
                                                    db_chat = self.save_chat(tg_full_chat)

                                                db_tg_channel = self.save_tg_channel(
                                                    db_tg_admin_account,
                                                    db_chat,
                                                    tg_full_chat,
                                                    userid
                                                )

                                                db_add_request = self.update_add_channel_request_status(
                                                    admin_userid, channel_username, db_tg_channel, tg_full_chat)

                                                response.done('joined channel')

                                        except DatabaseError as e:
                                            logger.exception(e)
                                            response.fail('DB_ERROR')
                                else:
                                    response.fail('Only public channels can be added')



                    else:
                        response.fail('Sorry, that Admin account is not connected now.')
                    break
            else:
                response.fail('Sorry, that Admin account is not connected now.')
        except exceptions.ObjectDoesNotExist as e:
            logger.exception(e)
            response.fail('no such tg account')

        return response

    def save_new_account(self, client: Client, db_owner_user, tg_user: User):
        with transaction.atomic():
            db_tg_user = self.tg_models.User(
                user_id=tg_user.id,
                username=tg_user.username,
                first_name=tg_user.first_name,
                last_name=tg_user.last_name,
                is_bot=tg_user.is_bot,
                is_restricted=tg_user.is_restricted,
                is_scam=tg_user.is_scam,
                is_verified=tg_user.is_verified,
                is_deleted=tg_user.is_deleted,
                is_support=tg_user.is_support,
                phone_number=tg_user.phone_number,
                dc_id=tg_user.dc_id,
                language_code=tg_user.language_code,
            )
            db_tg_user.save()

            db_tg_admin_account = self.tg_models.TelegramAccount(
                user_id=tg_user.id,
                username=tg_user.username,
                first_name=tg_user.first_name,
                last_name=tg_user.last_name,
                is_bot=tg_user.is_bot,
                is_restricted=tg_user.is_restricted,
                is_scam=tg_user.is_scam,
                is_verified=tg_user.is_verified,
                is_deleted=tg_user.is_deleted,
                phone_number=tg_user.phone_number,
                dc_id=tg_user.dc_id,
                language_code=tg_user.language_code,
                api_id=client.api_id,
                api_hash=client.api_hash,
                session_name=client.session_name,
                custom_user=db_owner_user,
                telegram_user=db_tg_user,
            )
            db_tg_admin_account.save()

    def update_add_channel_request_status(self, db_admin_userid: int, channel_username: str, db_tg_channel,
                                          tg_full_chat: Chat):
        db_add_request = self.tg_models.AddChannelRequest.objects.get(
            done=False,
            channel_username=channel_username,
            telegram_account=db_admin_userid)
        db_add_request.status = self.tg_models.AddChannelRequestStatusTypes.CHANNEL_MEMBER
        db_add_request.telegram_channel = db_tg_channel
        db_add_request.channel_id = tg_full_chat.id
        db_add_request.save()

        logger.info(db_add_request)
        return db_add_request

    def save_tg_channel(self, db_admin_tg_account, db_chat, tg_full_chat, db_userid):
        db_channel = self.tg_models.TelegramChannel(
            channel_id=tg_full_chat.id,
            is_account_creator=tg_full_chat.is_creator,
            is_account_admin=False,
            username=tg_full_chat.username,
            is_public=True,
            custom_user=self.users_models.CustomUser.objects.get(pk=db_userid),
            telegram_account=db_admin_tg_account,
            chat=db_chat,
        )
        db_channel.save()

        logger.info(db_channel)
        return db_channel

    def save_chat(self, full_chat, db_linked_chat=None):
        db_chat = self.tg_models.Chat(
            chat_id=full_chat.id,
            is_verified=full_chat.is_verified,
            is_restricted=full_chat.is_restricted,
            is_scam=full_chat.is_scam,
            title=full_chat.title,
            username=full_chat.username,
            description=full_chat.description,
            dc_id=full_chat.dc_id,
            linked_chat=db_linked_chat,
            invite_link=full_chat.invite_link,
        )
        db_chat.save()

        logger.info(db_chat)
        return db_chat


class TelegramConsumerManager(Thread):
    def __init__(self, clients):
        threading.Thread.__init__(self)
        self.clients = clients
        self.daemon = True
        self.name = 'Telegram_Consumer_Manager_Thread'

    def run(self) -> None:
        Worker(connection=Connection('amqp://localhost'), clients=clients).run()
        logger.info(f"Telegram Consumer started ....")


class TelegramClientManager(Thread):
    tg_models = None

    def __init__(self, clients: list):
        threading.Thread.__init__(self)
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

    def handle_channel_update(self, client, update):
        channel_raw_id = '-100' + str(update.channel_id)
        try:
            admin_logs = client.send(
                functions.channels.GetAdminLog(
                    channel=client.resolve_peer(peer_id=channel_raw_id),
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
            try:
                tg_admin = self.tg_models.TelegramAccount.objects.get(
                    session_name=client.session_name,
                    is_deleted=False,
                )
            except exceptions.ObjectDoesNotExist as e:
                logger.exception(e)
            else:
                tg_channels = self.tg_models.TelegramChannel.objects.filter(
                    channel_id=channel_raw_id,
                    is_deleted=False,
                    telegram_account=tg_admin,
                )
                for tg_channel in tg_channels:
                    tg_channel.is_account_admin = False
                    tg_channel.is_active = False  # TODO what's the goal of having this ?
                    tg_channel.save()
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
                    logger.exception(e)
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
                                    requests = self.tg_models.AddChannelRequest.objects.filter(
                                        done=False,
                                        channel_id=channel_raw_id,
                                        telegram_account=tg_admin,
                                    )
                                    tg_channel = self.tg_models.TelegramChannel.objects.get(
                                        channel_id=channel_raw_id,
                                        is_deleted=False,
                                        telegram_account=tg_admin,
                                    )
                                    admin_rights = action.new_participant.admin_rights

                                    with transaction.atomic():
                                        for request in requests:
                                            request.status = self.tg_models.AddChannelRequestStatusTypes.CHANNEL_ADMIN
                                            request.done = True
                                            request.save()

                                        tg_channel.is_account_admin = True
                                        tg_channel.is_active = True  # TODO what's the goal of having this ?
                                        tg_channel.save()

                                        self.save_admin_rights(admin_rights, tg_admin, tg_channel)

                                elif get_class_name(action.new_participant) in self.names and get_class_name(
                                        action.prev_participant) == "ChannelParticipantAdmin":
                                    # this tg_account was demoted to participant;
                                    pass
                                elif get_class_name(
                                        action.new_participant) == "ChannelParticipantAdmin" and get_class_name(
                                    action.prev_participant) == "ChannelParticipantAdmin":
                                    # this tg_account's admin rights was changed

                                    admin_rights = action.new_participant.admin_rights
                                    try:
                                        tg_channel = self.tg_models.TelegramChannel.objects.get(
                                            channel_id=channel_raw_id,
                                            is_deleted=False,
                                            telegram_account=tg_admin,
                                        )
                                    except exceptions.ObjectDoesNotExist as e:
                                        logger.exception(e)
                                    else:
                                        with transaction.atomic():
                                            self.update_old_admin_rights(tg_admin, tg_channel)
                                            self.save_admin_rights(admin_rights, tg_admin, tg_channel)

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
