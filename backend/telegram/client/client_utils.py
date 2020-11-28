import typing
from timeit import timeit

from pyrogram import Client
from pyrogram.handlers import MessageHandler, RawUpdateHandler, UserStatusHandler, DisconnectHandler
from pyrogram.raw.base import ChannelAdminLogEventAction
from pyrogram.raw.types import ChannelAdminLogEventsFilter, InputMessagesFilterPhotos, InputMessagesFilterDocument, \
    InputMessagesFilterUrl, InputMessagesFilterRoundVideo, InputMessagesFilterGeo, InputMessagesFilterContacts, \
    InputMessagesFilterGif, InputMessagesFilterVoice, InputMessagesFilterMusic, InputMessagesFilterVideo, \
    ChannelParticipantsSearch, ChannelAdminLogEvent, ChatBannedRights, UpdateDeleteChannelMessages, UpdateChannel
from pyrogram.raw.types.channels import AdminLogResults, ChannelParticipants, ChannelParticipantsNotModified
from pyrogram.types import User as User, Restriction as PGRestricion
from pyrogram.types import Dialog as Dialog
from pyrogram.types import Message as Message
from pyrogram.types import Chat as Chat
from pyrogram.types import Update as Update
from pyrogram.raw import types
from pyrogram import raw
# from pyrogram.raw.types import *
import pyrogram.utils as utils
from pyrogram.errors import FloodWait
from pyrogram.methods.utilities.idle import idle
from pyrogram import errors as tg_errors
from pyrogram.methods.chats.get_chat_members import Filters
from pyrogram.types.user_and_chats.chat_member import ChatMember

from pyrogram.raw.types import (
    ChannelAdminLogEventActionChangeAbout, ChannelAdminLogEventActionChangeLinkedChat,
    ChannelAdminLogEventActionChangeLocation, ChannelAdminLogEventActionChangePhoto,
    ChannelAdminLogEventActionChangeStickerSet, ChannelAdminLogEventActionChangeTitle,
    ChannelAdminLogEventActionChangeUsername, ChannelAdminLogEventActionDefaultBannedRights,
    ChannelAdminLogEventActionDeleteMessage, ChannelAdminLogEventActionEditMessage,
    ChannelAdminLogEventActionParticipantInvite, ChannelAdminLogEventActionParticipantJoin,
    ChannelAdminLogEventActionParticipantLeave, ChannelAdminLogEventActionParticipantToggleAdmin,
    ChannelAdminLogEventActionParticipantToggleBan, ChannelAdminLogEventActionStopPoll,
    ChannelAdminLogEventActionToggleInvites, ChannelAdminLogEventActionTogglePreHistoryHidden,
    ChannelAdminLogEventActionToggleSignatures, ChannelAdminLogEventActionToggleSlowMode,
    ChannelAdminLogEventActionUpdatePinned
)
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
import trio

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
from core.globals import logger
from telegram import globals as tg_globals
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

from telegram.client.client_manager import *


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

    def get_app_user(self, db_userid):
        try:
            db_site_user = self.users_models.CustomUser.objects.get(pk=db_userid)
        except exceptions.ObjectDoesNotExist as e:
            db_site_user = None
        except Exception as e:
            logger.exception(e)
            db_site_user = None
        return db_site_user

    def disable_channel_analyzers_with_admin_required(self, db_chat):
        if not db_chat:
            return

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

    def enable_or_create_channel_analyzers_with_admin_required(self, db_chat, db_tg_channel):
        if db_tg_channel:
            db_tg_channel.is_active = True
            db_tg_channel.is_account_admin = True
            db_tg_channel.save()

        if not db_chat.admin_log_analyzer:
            db_chat.admin_log_analyzer = self.tg_models.AdminLogAnalyzerMetaData.objects.create(
                id=str(db_chat.chat_id),
                telegram_channel=db_tg_channel,
                enabled=True,
            )
        if not db_chat.admin_log_analyzer.enabled:
            db_chat.admin_log_analyzer.enabled = True
            db_chat.admin_log_analyzer.save()

        if not db_chat.members_analyzer:
            db_chat.members_analyzer = self.tg_models.ChatMembersAnalyzerMetaData.objects.create(
                id=str(db_chat.chat_id),
                telegram_channel=db_tg_channel,
                enabled=True,
            )
        if not db_chat.members_analyzer.enabled:
            db_chat.members_analyzer.enabled = True
            db_chat.members_analyzer.save()

        db_chat.save()

    def create_general_channel_analyzers(self, db_chat):
        if not db_chat.shared_media_analyzer:
            db_chat.shared_media_analyzer = self.tg_models.SharedMediaAnalyzerMetaData.objects.create(
                id=str(db_chat.chat_id),
                enabled=True,
            )

        if not db_chat.member_count_analyzer:
            db_chat.member_count_analyzer = self.tg_models.ChatMemberCountAnalyzerMetaData.objects.create(
                id=str(db_chat.chat_id),
                enabled=True,
            )

        if not db_chat.message_view_analyzer:
            db_chat.message_view_analyzer = self.tg_models.ChatMessageViewsAnalyzerMetaData.objects.create(
                id=str(db_chat.chat_id),
                enabled=True,
            )
        db_chat.save()

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

    def promote_account(self, channel_id: int, tg_admin):
        with transaction.atomic():
            self.complete_add_channel_request_status(channel_id, tg_admin)
            self.enable_tg_channel(channel_id, tg_admin)
            # the rights is already added

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

    def create_channel_participant_from_chat_member(
            self,
            *,
            chat_member: ChatMember,
            db_membership,
            client: Client,
            event_date: int,
            is_previous_participant: bool = None,

            db_tg_channel=None,
            db_tg_admin_account=None
    ):
        if not chat_member or not db_membership or not client or not event_date:
            return None
        _type = chat_member.status
        db_participant = self.tg_models.ChannelParticipant(
            user=self.get_or_create_db_tg_user(
                tg_user=chat_member.user,
                client=client,
            ),
            membership=db_membership,
            invited_by=self.get_or_create_db_tg_user(
                tg_user=chat_member.invited_by,
                client=client,
            ) if chat_member.invited_by else None,
            event_date=event_date,
            is_previous=is_previous_participant,
        )

        if _type == 'user':
            db_participant.type = self.tg_models.ChannelParticipantTypes.user
            db_participant.join_date = chat_member.joined_date

        elif _type == 'member':
            db_participant.type = self.tg_models.ChannelParticipantTypes.member
            # db_participant.user = self.get_or_create_db_tg_user(
            #     tg_user=chat_member.user,
            #     client=client,
            # )
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
            db_participant.admin_rights = self.create_db_admin_rights(chat_member, db_tg_admin_account, db_tg_channel)

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

    def update_membership_status(
            self,
            *,
            db_participant=None,

            db_membership=None,

            chat_member: ChatMember = None,
            client: Client = None,

            event_date: int,
    ):
        def is_same_type():
            # return db_membership.current_status and db_membership.current_status.type == chat_member.status and db_membership.current_status.join_date and chat_member.joined_date and db_membership.current_status.join_date == chat_member.joined_date
            return db_membership.current_status and db_membership.current_status.type == chat_member.status

        if chat_member and client and event_date and db_membership:  # the data comes from `get_members` so it's up to date
            if not is_same_type():
                # create participant and update membership
                db_participant = self.create_channel_participant_from_chat_member(
                    chat_member=chat_member,
                    db_membership=db_membership,
                    client=client,
                    event_date=event_date,
                )
                db_membership.previous_status, db_membership.current_status = db_membership.current_status, db_participant
                db_membership.status_change_date = event_date
                db_membership.save()

        elif event_date and db_membership and db_participant:
            if not db_membership.current_status and not db_membership.previous_status:
                db_membership.current_status = db_participant
                db_membership.status_change_date = event_date
                db_membership.save()

            elif not db_membership.previous_status and db_membership.current_status:
                if event_date < db_membership.status_change_date:
                    db_membership.previous_status = db_participant
                    db_membership.save()
                elif event_date > db_membership.status_change_date:
                    db_membership.previous_status, db_membership.current_status = db_membership.current_status, db_participant
                    db_membership.status_change_date = event_date
                    db_membership.save()
                elif event_date == db_membership.status_change_date:
                    if not db_participant.is_previous and db_membership.current_status.is_previous:
                        db_membership.previous_status, db_membership.current_status = db_membership.current_status, db_participant
                        db_membership.save()
                    elif db_participant.is_previous and not db_membership.current_status.is_previous:
                        db_membership.previous_status = db_participant
                        db_membership.save()
                    else:
                        raise Exception("Oops!, why?")

            elif db_membership.current_status and db_membership.previous_status:
                if event_date < db_membership.status_change_date:
                    if event_date < db_membership.previous_status.event_date:
                        pass
                    elif event_date > db_membership.previous_status.event_date:
                        db_membership.previous_status = db_participant
                        db_membership.save()
                    elif event_date == db_membership.previous_status.event_date:
                        if not db_participant.is_previous and db_membership.previous_status.is_previous:
                            db_membership.previous_status = db_participant
                            db_membership.save()
                        elif db_participant.is_previous and not db_membership.previous_status.is_previous:
                            pass
                        else:
                            raise Exception("Oops!, why?")
                elif event_date > db_membership.status_change_date:
                    db_membership.previous_status, db_membership.current_status = db_membership.current_status, db_participant
                    db_membership.status_change_date = event_date
                    db_membership.save()
                elif event_date == db_membership.status_change_date:
                    if not db_participant.is_previous and db_membership.current_status.is_previous:
                        db_membership.previous_status, db_membership.current_status = db_membership.current_status, db_participant
                        db_membership.save()
                    elif db_participant.is_previous and not db_membership.current_status.is_previous:
                        db_membership.previous_status = db_participant
                        db_membership.save()
                    else:
                        raise Exception("Oops!, why?")

    def create_chat_banned_rights(self, chat_member: ChatMember):
        return self.tg_models.ChatBannedRight.objects.create(
            can_view_messages=chat_member.status == 'restricted',
            can_send_messages=chat_member.can_send_messages,
            can_send_media=chat_member.can_send_media_messages,
            can_send_stickers=chat_member.can_send_stickers,
            can_send_gifs=chat_member.can_send_animations,
            can_send_games=chat_member.can_send_games,
            can_send_inline=chat_member.can_use_inline_bots,
            can_embed_links=chat_member.can_add_web_page_previews,
            can_send_polls=chat_member.can_send_polls,
            can_change_info=chat_member.can_change_info,
            can_invite_users=chat_member.can_invite_users,
            can_pin_messages=chat_member.can_pin_messages,
            until_date=chat_member.until_date,
        )

    def create_chat_banned_rights_from_raw_rights(self, banned_rights: ChatBannedRights):
        return self.tg_models.ChatBannedRight.objects.create(
            can_view_messages=not banned_rights.view_messages,
            can_send_messages=not banned_rights.send_messages,
            can_send_media=not banned_rights.send_media,
            can_send_stickers=not banned_rights.send_stickers,
            can_send_gifs=not banned_rights.send_gifs,
            can_send_games=not banned_rights.send_games,
            can_send_inline=not banned_rights.send_inline,
            can_embed_links=not banned_rights.embed_links,
            can_send_polls=not banned_rights.send_polls,
            can_change_info=not banned_rights.change_info,
            can_invite_users=not banned_rights.invite_users,
            can_pin_messages=not banned_rights.pin_messages,
            until_date=banned_rights.until_date,
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

    def get_or_create_participant_by_event(
            self,
            *,
            client: Client,
            db_membership,
            event_type,
            event_date,
            by=None,
            is_previous_participant: bool = None,
            tg_raw_users: dict = None,
            tg_raw_participant=None,
            # db_participant1=None,
            # db_participant2=None

            db_tg_channel=None,
            db_tg_admin_account=None,
    ):
        db_participant = None
        if event_type == 'join':
            try:
                db_participant = db_membership.participant_history.get(
                    event_date=event_date,
                    type__in=(
                        [self.tg_models.ChannelParticipantTypes.member,
                         self.tg_models.ChannelParticipantTypes.self, ]
                    )
                )
            except exceptions.ObjectDoesNotExist as e:
                db_participant = self.tg_models.ChannelParticipant.objects.create(
                    user=db_membership.user,
                    membership=db_membership,
                    type=self.tg_models.ChannelParticipantTypes.member,
                    join_date=event_date,
                    event_date=event_date,
                )
            except Exception as e:
                logger.exception(e)

        elif event_type == 'left':
            try:
                db_participant = db_membership.participant_history.get(
                    event_date=event_date,
                    type__in=(
                        [self.tg_models.ChannelParticipantTypes.left, ]
                    )
                )
            except exceptions.ObjectDoesNotExist as e:
                db_participant = self.tg_models.ChannelParticipant.objects.create(
                    user=db_membership.user,
                    membership=db_membership,
                    type=self.tg_models.ChannelParticipantTypes.left,
                    left_date=event_date,
                    event_date=event_date,
                    left=True,
                )
            except Exception as e:
                logger.exception(e)

        elif event_type == 'invite':
            try:
                db_participant = db_membership.participant_history.get(
                    event_date=event_date,
                    type__in=(
                        [self.tg_models.ChannelParticipantTypes.member,
                         self.tg_models.ChannelParticipantTypes.self, ]
                    ),
                )
            except exceptions.ObjectDoesNotExist as e:
                chat_member = ChatMember._parse(client, tg_raw_participant, tg_raw_users)
                if by:
                    chat_member.invited_by = User._parse(client, tg_raw_users[by.user_id])
                db_participant = self.create_channel_participant_from_chat_member(
                    chat_member=chat_member,
                    db_membership=db_membership,
                    client=client,
                    event_date=event_date,
                )
            except Exception as e:
                logger.exception(e)

        elif event_type == 'toggle_ban':
            try:
                db_participant = db_membership.participant_history.get(
                    event_date=event_date,
                    is_previous=is_previous_participant,
                )
            except exceptions.ObjectDoesNotExist as e:
                chat_member = ChatMember._parse(client, tg_raw_participant, tg_raw_users)
                if by:
                    chat_member.invited_by = User._parse(client, tg_raw_users[by.user_id])
                if chat_member.joined_date == 0:
                    chat_member.status = 'user'
                db_participant = self.create_channel_participant_from_chat_member(
                    chat_member=chat_member,
                    db_membership=db_membership,
                    client=client,
                    event_date=event_date,
                    is_previous_participant=is_previous_participant,
                )
            except Exception as e:
                logger.exception(e)

        elif event_type == 'toggle_admin':
            try:
                db_participant = db_membership.participant_history.get(
                    event_date=event_date,
                    is_previous=is_previous_participant,
                )
            except exceptions.ObjectDoesNotExist as e:
                chat_member = ChatMember._parse(client, tg_raw_participant, tg_raw_users)
                if by:
                    chat_member.invited_by = User._parse(client, tg_raw_users[by.user_id])
                if chat_member.joined_date == 0:
                    chat_member.status = 'user'
                db_participant = self.create_channel_participant_from_chat_member(
                    chat_member=chat_member,
                    db_membership=db_membership,
                    client=client,
                    event_date=event_date,
                    is_previous_participant=is_previous_participant,

                    db_tg_channel=db_tg_channel,
                    db_tg_admin_account=db_tg_admin_account
                )
            except Exception as e:
                logger.exception(e)

        return db_participant

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

    def get_db_telegram_account(self, user_id: int):
        try:
            tg_admin: TelegramClientManager.tg_models.TelegramAccount = self.tg_models.TelegramAccount.objects.get(
                is_deleted=False,
                user_id=user_id,
            )
        except exceptions.ObjectDoesNotExist as e:
            tg_admin = None
        except Exception as e:
            tg_admin = None
            logger.exception(e)

        return tg_admin

    def get_db_telegram_account_by_client(self, client: Client):
        try:
            tg_admin: TelegramClientManager.tg_models.TelegramAccount = self.tg_models.TelegramAccount.objects.get(
                is_deleted=False,
                session_name=client.session_name,
                api_id=client.api_id,
            )
        except exceptions.ObjectDoesNotExist as e:
            tg_admin = None
        except Exception as e:
            tg_admin = None
            logger.exception(e)

        return tg_admin

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
                user=db_user,
                telegram_account=db_admin_tg_account,
            )
        except exceptions.ObjectDoesNotExist as e:
            db_channel = self.tg_models.TelegramChannel.objects.create(
                channel_id=db_chat.chat_id,
                is_account_creator=tg_full_chat.is_creator,
                is_account_admin=False,
                username=db_chat.username.lower(),
                is_public=db_chat.is_public,
                user=db_user,
                telegram_account=db_admin_tg_account,
                chat=db_chat,
            )
        except Exception as e:
            logger.exception(e)
            db_channel = None

        return db_channel

    def get_db_chat(self, db_tg_admin: "TelegramAccount", chat_id: int):
        try:
            db_chat = self.tg_models.Chat.objects.get(
                chat_id=chat_id,
                is_deleted=False,
                logger_account=db_tg_admin,
            )
        except exceptions.ObjectDoesNotExist as e:
            db_chat = None
        except Exception as e:
            db_chat = None
            logger.exception(e)

        return db_chat

    def get_db_tg_channel(self, db_tg_admin: "TelegramAccount", channel_id: int):
        try:
            db_tg_channel = self.tg_models.TelegramChannel.objects.get(
                channel_id=channel_id,
                is_deleted=False,
                telegram_account=db_tg_admin,
            )
        except exceptions.ObjectDoesNotExist as e:
            db_tg_channel = None
            logger.exception(e)
        except Exception as e:
            db_tg_channel = None
            logger.exception(e)

        return db_tg_channel

    def get_db_tg_channel_by_username(self, channel_username):
        try:
            db_tg_channel = self.tg_models.TelegramChannel.objects.get(
                username=channel_username,
                is_deleted=False
            )
        except exceptions.ObjectDoesNotExist as e:
            db_tg_channel = None
        except Exception as e:
            logger.exception(e)
            db_tg_channel = None
        return db_tg_channel

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
        db_tg_chat.first_name = getattr(tg_chat, 'first_name', None)
        db_tg_chat.last_name = getattr(tg_chat, 'last_name', None)
        db_tg_chat.description = getattr(tg_chat, 'description', None)
        db_tg_chat.dc_id = getattr(tg_chat, 'dc_id', None)
        db_tg_chat.permissions = self.create_or_update_chat_permissions(tg_chat)
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
        db_tg_chat.logger_account = db_creator_account

    def get_or_create_db_tg_chat(self, tg_chat: Chat, db_creator_account, client: Client, update_current=False,
                                 is_tg_full_chat=False, check_chat_type=False):
        if tg_chat is None or not db_creator_account or not client:
            return None
        _id = int(tg_chat.id)
        db_tg_chat = None

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
            is_public = True
            if not is_tg_full_chat:
                # get the full chat info from telegram client
                try:
                    temp: Chat = client.get_chat(_id)
                except tg_errors.ChannelPrivate as e:
                    logger.info(f"channel {tg_chat} is private")
                    is_public = False
                except tg_errors.RPCError as e:
                    logger.exception(e)
                else:
                    tg_chat: Chat = temp
                    is_public = True
            try:
                db_tg_chat = self.tg_models.Chat(
                    chat_id=_id,
                    is_public=True if tg_chat.username else is_public,
                )
                self.fill_db_tg_chat_attrs(db_tg_chat, tg_chat, db_creator_account, client, check_chat_type)
                db_tg_chat.save()
                if db_tg_chat.is_restricted:
                    self.create_db_restrictions(tg_chat.restrictions, db_tg_chat)
            except Exception as e:
                logger.exception(e)
                db_tg_chat = None
        except Exception as e:
            logger.exception(e)
            db_tg_chat = None

        return db_tg_chat

    def create_or_update_dialog(self, db_chat, db_tg_admin_account):
        if not db_chat or not db_tg_admin_account:
            return None
        return self.tg_models.Dialog.objects.update_or_create(
            id=f"{db_tg_admin_account.user_id}:{db_chat.chat_id}",
            chat=db_chat,
            account=db_tg_admin_account,
            is_member=True,
        )

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
            db_chat.logger_account,
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
        db_message.delete_date = now if db_message.empty else None
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
        db_message.logged_by = db_chat.logger_account

    def get_message_by_message_id(self, db_chat, message_id: int):
        if not db_chat and not message_id:
            return None
        _id = f"{db_chat.chat_id}:{message_id}:"
        try:
            db_message = self.tg_models.Message.objects.filter(
                chat__chat_id=db_chat.chat_id,
                message_id=message_id
            ).order_by('-created_at').first()
        except Exception as e:
            logger.exception(e)
            db_message = None
        return db_message

    def mark_message_as_deleted(self, db_chat, db_message, deletion_date: int = None):
        if not db_chat or not db_message or not deletion_date:
            return
        if not db_message.is_deleted:
            db_message.is_deleted = True
            db_message.delete_date = deletion_date
            db_message.save()

    def get_or_create_db_tg_message(self, message: Message, db_chat, client: Client, now: int, deletion_date: int = 0):
        if message is None or not db_chat or not client:
            return None
        _id = f"{db_chat.chat_id}:{message.message_id}:{message.edit_date if message.edit_date else 0}"
        _id_prefix = f"{db_chat.chat_id}:{message.message_id}:"  # todo: delete?

        try:
            db_message = self.tg_models.Message.objects.get(id=_id)
        except exceptions.ObjectDoesNotExist as e:
            try:
                if not message.empty:
                    db_message = self.tg_models.Message(
                        id=_id,
                    )
                    self.fill_db_tg_message_attrs(db_message, message, db_chat, client, now)
                    db_message.save()
                else:
                    db_message = None
            except Exception as e:
                logger.exception(e)
                db_message = None
            else:
                pass
        except Exception as e:
            logger.exception(e)
            db_message = None
        else:
            if message and message.edit_date and message.edit_date > db_message.modified_at:
                # message needs to be updated in the db
                self.fill_db_tg_message_attrs(db_message, message, db_chat, client, now)
                db_message.save()
            if deletion_date:
                db_message.is_deleted = True
                db_message.delete_date = deletion_date
                db_message.save()

        return db_message

    def update_db_message_to_deleted(self, client: Client, update: UpdateDeleteChannelMessages):
        now = arrow.utcnow().timestamp
        _id = int(f"-100{update.channel_id}")
        db_chat = self.get_db_chat(self.get_db_telegram_account_by_client(client), _id)
        if db_chat:
            self.tg_models.Message.objects.filter(
                message_id__in=update.messages,
                chat=db_chat,
            ).update(
                is_deleted=True,
                delete_date=now
            )

    def create_db_message_view_without_message(self, db_chat, db_message, message_id: int, views: int, now: int):
        return self.tg_models.MessageView.objects.create(
            id=f"{db_chat.chat_id}:{message_id}:{now}",
            date=now,
            views=views,
            message=db_message,
            logged_by=db_chat.logger_account,
            chat=db_chat,
        )

    def create_db_message_view(self, db_chat, db_message, message: Message, now):
        return self.tg_models.MessageView.objects.update_or_create(
            id=f"{db_chat.chat_id}:{message.message_id}:{now}",
            date=now,
            views=message.views,
            message=db_message,
            logged_by=db_chat.logger_account,
            chat=db_chat,
        )

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

    def enable_tg_channel(self, channel_id: int, db_tg_admin):
        tg_channel = self.get_db_tg_channel(db_tg_admin, channel_id)
        if tg_channel:
            tg_channel.is_account_admin = True
            tg_channel.is_active = True  # TODO what's the goal of having this ?
            tg_channel.save()
        return tg_channel

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
        except Exception as e:
            logger.exception(e)
        else:
            tg_channels = self.tg_models.TelegramChannel.objects.filter(
                channel_id=channel_id,
                is_deleted=False,
                telegram_account=tg_admin,
            )
            for tg_channel in tg_channels:
                tg_channel.is_account_admin = False
                tg_channel.save()

    def disable_channel_with_analyzers(self, client, db_tg_admin, channel_id: int):
        # this tg_account was demoted to participant;
        self.disable_tg_channel(channel_id, client)
        self.disable_channel_analyzers_with_admin_required(self.get_db_chat(db_tg_admin, channel_id))

    def update_or_create_chat_member_count(self, db_chat, tg_chat, response: BaseResponse):
        now = arrow.utcnow().timestamp
        try:
            self.tg_models.ChatMemberCount.objects.update_or_create(
                id=f"{db_chat.chat_id}:{db_chat.logger_account.user_id}:{now}",
                count=tg_chat.members_count,
                date=now,
                chat=db_chat,
                logged_by=db_chat.logger_account,
            )
        except Exception as e:
            logger.exception(e)
            response.fail('DB_ERROR')
        else:
            response.done('logged chat member count')
        return response

    def create_or_update_chat_permissions(self, tg_chat: Chat):
        if tg_chat.permissions:
            try:
                db_chat_permissions = self.tg_models.ChatPermissions.objects.update_or_create(
                    id=str(tg_chat.id),
                    can_send_messages=tg_chat.permissions.can_send_messages,
                    can_send_media_messages=tg_chat.permissions.can_send_media_messages,
                    can_send_stickers=tg_chat.permissions.can_send_stickers,
                    can_send_animations=tg_chat.permissions.can_send_animations,
                    can_send_games=tg_chat.permissions.can_send_games,
                    can_use_inline_bots=tg_chat.permissions.can_use_inline_bots,
                    can_add_web_page_previews=tg_chat.permissions.can_add_web_page_previews,
                    can_send_polls=tg_chat.permissions.can_send_polls,
                    can_change_info=tg_chat.permissions.can_change_info,
                    can_invite_users=tg_chat.permissions.can_invite_users,
                    can_pin_messages=tg_chat.permissions.can_pin_messages,
                )
            except DatabaseError as e:
                logger.exception(e)
                db_chat_permissions = None
            except Exception as e:
                logger.exception(e)
                db_chat_permissions = None

            return db_chat_permissions
        else:
            return None


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
    _names = [
        "ChannelParticipantSelf",
        "ChannelParticipant",
    ]

    def __init__(self, connection, clients, index: int):
        self.connection = connection
        self.index = index
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

        func = body['func']
        args = body['args']
        kwargs = body['kwargs']

        logger.info(f'on consumer {self.index} Got task: {prettify(body)}')
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

        elif func == 'task_iterate_chat_history':
            response = self.acquire_clients(self.task_iterate_chat_history, *args, **kwargs)

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
                    db_tg_admin_account = self.get_db_telegram_account_by_client(client)
                    if db_tg_admin_account:
                        from collections import defaultdict
                        start = time.perf_counter()
                        dialogs = self.get_all_dialogs(client)
                        print(f"after : {time.perf_counter() - start}")
                        if dialogs and len(dialogs):
                            # fixme: remove this?
                            types = defaultdict(int)
                            for dialog in dialogs:
                                types[dialog.chat.type] += 1
                            logger.info(prettify(types))

                            for dialog in dialogs:
                                if dialog.chat.type not in ('private', 'bot'):
                                    db_chat = self.get_or_create_db_tg_chat(
                                        dialog.chat,
                                        db_tg_admin_account,
                                        client,
                                        update_current=False,  # fixme: how to avoid floodWait when this is enabled?
                                        is_tg_full_chat=False,  # fixme: speedup the first fetch
                                    )
                                    if db_chat:
                                        self.create_or_update_dialog(db_chat, db_tg_admin_account)

                                        if dialog.chat.type == 'channel' and dialog.chat.username is not None:
                                            db_tg_channel = self.get_or_create_db_tg_channel(
                                                db_tg_admin_account,
                                                db_chat,
                                                dialog.chat,
                                                self.users_models.CustomUser.objects.get(username='sigma',
                                                                                         is_superuser=True),
                                            )

                                            # create general channel analyzers
                                            self.create_general_channel_analyzers(db_chat)

                                            try:
                                                admins = client.get_chat_members(db_chat.chat_id,
                                                                                 filter=Filters.ADMINISTRATORS)
                                            except tg_errors.ChatAdminRequired as e:
                                                # client is not admin of this channel, update telegram account related to this channel
                                                self.disable_tg_channel(db_chat.chat_id, client)
                                                self.disable_channel_analyzers_with_admin_required(db_chat)
                                            except Exception as e:
                                                logger.exception(e)
                                            else:
                                                # enable/create admin required analyzers for this channel
                                                self.enable_or_create_channel_analyzers_with_admin_required(db_chat,
                                                                                                            db_tg_channel)
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

        db_request_owner = self.get_app_user(db_userid)
        if db_request_owner:
            db_tg_admin_account = self.get_db_telegram_account(db_tg_account_admin_id)
            if db_tg_admin_account:
                for client in clients:
                    if client.session_name == db_tg_admin_account.session_name:
                        client: Client = client
                        if client.is_connected:
                            db_tg_channel = self.get_db_tg_channel_by_username(channel_username)
                            if db_tg_channel:
                                response.fail('this channel is already added')
                            else:
                                try:
                                    tg_chat: Chat = client.get_chat(channel_username)
                                except tg_errors.BadRequest as e:
                                    if type(e) == tg_errors.ChannelsTooMuch:
                                        # fixme: what now?
                                        response.fail('Admin has joined too many channels or supergroups')
                                    else:
                                        response.fail(TG_BAD_REQUEST)
                                except Exception as e:
                                    logger.exception(e)
                                else:
                                    # check to see whether the chat is the type of channel and it's public
                                    if tg_chat.type == 'channel' and tg_chat.username:
                                        try:
                                            client.join_chat(channel_username)
                                        except tg_errors.RPCError as e:
                                            logger.exception(e)
                                            response.fail(TG_BAD_REQUEST)
                                        else:
                                            try:
                                                with transaction.atomic():
                                                    db_chat = self.get_or_create_db_tg_chat(
                                                        tg_chat,
                                                        db_tg_admin_account,
                                                        client,
                                                    )
                                                    db_tg_channel = self.get_or_create_db_tg_channel(
                                                        db_tg_admin_account,
                                                        db_chat,
                                                        tg_chat,
                                                        db_request_owner,
                                                    )

                                                    db_add_request = self.update_add_channel_request_status(
                                                        db_tg_admin_account, channel_username, db_tg_channel,
                                                        tg_chat,
                                                        db_request_owner,
                                                    )
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
            else:
                response.fail('no such tg account')
        else:
            response.fail('No such user')

        return response

    ########################################
    async def update_db(self, view_chunks: dict, db_chat, client: Client):
        message_ids_to_fetch = []
        for k in view_chunks:
            views = view_chunks[k]
            if not len(views):
                continue
            for i, view in enumerate(views):
                message_id = k + i
                db_message = self.get_message_by_message_id(
                    db_chat,
                    message_id=message_id,
                )

                if view == 0:
                    # message no longer exists and it's deleted
                    self.mark_message_as_deleted(db_chat, db_message)
                else:
                    try:
                        now = arrow.utcnow().timestamp
                        with transaction.atomic():
                            if db_message:
                                db_message_view = self.create_db_message_view_without_message(
                                    db_chat,
                                    db_message,
                                    message_id,
                                    view,
                                    now,
                                )
                            else:
                                # message is not in the db
                                message_ids_to_fetch.append(message_id)

                    except Exception as e:
                        logger.exception(e)
                    else:
                        pass

        if len(message_ids_to_fetch):
            length = len(message_ids_to_fetch)
            index = 0
            increment = 100
            while index < length:
                if index > 0:
                    await trio.sleep(1)
                for message in client.get_messages(
                        chat_id=db_chat.chat_id,
                        message_ids=message_ids_to_fetch[index:index + increment]
                ):
                    try:
                        now = arrow.utcnow().timestamp
                        with transaction.atomic():
                            db_message = self.get_or_create_db_tg_message(
                                message,
                                db_chat,
                                client,
                                now,
                                now if message.empty else None
                            )
                            if db_message:
                                db_message_view = self.create_db_message_view(
                                    db_chat,
                                    db_message,
                                    message,
                                    now,
                                )
                                self.create_entities(client, db_chat, db_message, message)
                                self.create_entity_types(db_chat, db_message, message)

                    except Exception as e:
                        logger.exception(e)
                    else:
                        pass
                index += increment

    async def tg_get_message_views(self, client: Client, chat_id, ids: list):
        return client.send(
            raw.functions.messages.GetMessagesViews(peer=client.resolve_peer(chat_id), id=ids, increment=True)
        )

    async def get_views_chunk(self, client: Client, db_chat, i: int, all_views: dict):
        started = time.perf_counter()
        try:
            views = await self.tg_get_message_views(client, db_chat.chat_id, list(range(i, i + 100)))
        except tg_errors.RPCError as e:
            logger.exception(e)  # todo: other exceptions?
        except Exception as e:
            logger.exception(e)
        else:
            all_views[i] = views
        logger.info(f"{db_chat} messages {i} - {i + 100}: {time.perf_counter() - started:.3f}s")

    async def update_message_views(self, client: Client, db_chat):
        message = self.get_last_valid_message(client, db_chat)
        total_views = {}
        if message:
            last_message_id = message.message_id
            async with trio.open_nursery() as nursery:
                start = int((last_message_id - 10000) / 100)
                if start < 0:
                    start = 0
                for i in range(start, int(last_message_id / 100) + 1):
                    nursery.start_soon(self.get_views_chunk, client, db_chat, i * 100, total_views)
        return total_views

    def task_analyze_message_views(self, *args, **kwargs):
        response = BaseResponse()

        chats = self.tg_models.Chat.objects.filter(message_view_analyzer__isnull=False,
                                                   message_view_analyzer__enabled=True)
        update_db_dict = {}
        for db_chat in chats:
            analyzer = db_chat.message_view_analyzer
            now = arrow.utcnow().timestamp

            for client in clients:
                if client.session_name == db_chat.logger_account.session_name:
                    client: Client = client
                    if client.is_connected:
                        try:
                            started = time.perf_counter()
                            total_views = trio.run(self.update_message_views, client, db_chat)
                            logger.info(
                                f"finished fetch views in: {time.perf_counter() - started:.3f}s for chat: {db_chat}")
                            if len(total_views):
                                update_db_dict[db_chat.chat_id] = (total_views, db_chat, client)
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

        if len(update_db_dict):  # todo: put the db update in another task?
            for key, value in update_db_dict.items():
                total_views, db_chat, client = value
                started = time.perf_counter()
                trio.run(self.update_db, total_views, db_chat, client)
                logger.info(
                    f"finished db update views in: {time.perf_counter() - started:.3f}s for chat :{db_chat}")

        return response

    def get_last_valid_message(self, client, db_chat, limit: int = 20, is_first=True):
        if not client or not db_chat:
            return None
        messages = client.get_history(db_chat.chat_id, limit=limit)
        message = None
        if not messages:
            return None
        for msg in messages:
            if not msg.service:
                message = msg
        if is_first and not message:
            return self.get_last_valid_message(client, db_chat, limit=100, is_first=False)
        return message

    def task_iterate_chat_history(self, *args, **kwargs):
        response = BaseResponse()

        chats = self.tg_models.Chat.objects.filter(message_view_analyzer__isnull=False,
                                                   message_view_analyzer__enabled=True)
        for db_chat in chats:
            analyzer = db_chat.message_view_analyzer
            now = arrow.utcnow().timestamp

            for client in clients:
                if client.session_name == db_chat.logger_account.session_name:
                    client: Client = client
                    if client.is_connected:
                        try:
                            started = time.perf_counter()
                            message = self.get_last_valid_message(
                                client,
                                db_chat,
                            )
                            if not message:
                                break
                            offset_id = message.message_id
                            row = 0
                            sleep_counter = 0
                            sleep_time = 1
                            total_msgs = 0
                            while True:
                                if not row % 5:
                                    sleep_counter += 1
                                    time.sleep(sleep_time)
                                messages = client.get_history(db_chat.chat_id, offset=-1, offset_id=offset_id)
                                if not messages:
                                    break
                                row += 1
                                total_msgs += len(messages)
                                logger.info(
                                    f"got {total_msgs} messages in {time.perf_counter() - started - sleep_counter * sleep_time:.3f} of chat: {db_chat}")
                                for message in messages:
                                    message: Message = message
                                    offset_id = message.message_id
                                    if not message.service:
                                        try:
                                            now = arrow.utcnow().timestamp
                                            with transaction.atomic():
                                                db_message = self.get_or_create_db_tg_message(
                                                    message,
                                                    db_chat,
                                                    client,
                                                    now,
                                                    now if message.empty else None,
                                                )
                                                if db_message:
                                                    db_message_view = self.create_db_message_view(
                                                        db_chat,
                                                        db_message,
                                                        message,
                                                        now,
                                                    )
                                                    self.create_entities(client, db_chat, db_message, message)
                                                    self.create_entity_types(db_chat, db_message, message)

                                        except Exception as e:
                                            logger.exception(e)
                                        else:
                                            pass

                            logger.info(
                                f"finished iterate history in {time.perf_counter() - started - sleep_counter * sleep_time:.3f} of chat: {db_chat}")
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
        made_request = False
        for db_chat in chats:
            analyzer = db_chat.member_count_analyzer
            last = arrow.utcnow().timestamp
            for client in clients:
                if client.session_name == db_chat.logger_account.session_name:
                    client: Client = client
                    if client.is_connected:
                        try:
                            if made_request:
                                time.sleep(0.7)
                            # todo: a better way to get member_count?
                            tg_chat: Chat = client.get_chat(chat_id=db_chat.chat_id)
                        except tg_errors.RPCError as e:
                            response.fail('TG_ERROR')
                            made_request = False
                        except Exception as e:
                            response.fail('UNKNOWN')
                            logger.exception(e)
                            made_request = False
                        else:
                            response = self.update_or_create_chat_member_count(db_chat, tg_chat, response)
                            made_request = True
                    else:
                        # fixme: update the response to support multiErrors
                        response.fail('client is not connected now')
                    break
            else:
                response.fail('no client is ready')
                break

            if response.success:
                if not analyzer.first_analyzed_at:
                    analyzer.first_analyzed_at = last
                analyzer.last_analyzed_at = last
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
                if client.session_name == db_chat.logger_account.session_name:
                    client: Client = client
                    if client.is_connected:
                        res = client.send(
                            raw.functions.messages.GetSearchCounters(peer=client.resolve_peer(db_chat.chat_id),
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
                                        id=f"{db_chat.chat_id}:{db_chat.logger_account.user_id}:{now}",
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
                                        logged_by=db_chat.logger_account,
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
                            if client.session_name == db_chat.logger_account.session_name:
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
                if client.session_name == db_chat.logger_account.session_name:
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

        db_tg_admin_id = kwargs.get('db_tg_admin_id', None)
        chat_id = kwargs.get('chat_id', None)

        if db_tg_admin_id and chat_id:
            db_chat = self.get_db_chat(self.get_db_telegram_account(db_tg_admin_id), chat_id)
            chats = []
            if db_chat:
                chats.append(db_chat)
        else:
            chats = self.tg_models.Chat.objects.filter(admin_log_analyzer__isnull=False,
                                                       admin_log_analyzer__enabled=True)
        if chats and len(chats):
            for db_chat in chats:
                analyzer = db_chat.admin_log_analyzer
                now = arrow.utcnow().timestamp
                for client in clients:
                    if client.session_name == db_chat.logger_account.session_name:
                        client: Client = client
                        if client.is_connected:
                            response = self.analyze_chat_admin_logs(db_chat, db_chat.logger_account, client, response)
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

    def analyze_chat_admin_logs(self, db_chat, db_tg_admin_account, client: Client, response: BaseResponse):
        try:
            admin_log: AdminLogResults = client.send(
                raw.functions.channels.GetAdminLog(
                    channel=client.resolve_peer(peer_id=db_chat.chat_id),
                    q="",
                    min_id=0,
                    max_id=0,
                    events_filter=None,
                    admins=None,
                    limit=0
                )
            )
        except tg_errors.ChatAdminRequired:
            response.fail(f'chat admin required for chat {db_chat}')
            # this tg_account was demoted to participant;
            self.disable_tg_channel(db_chat.chat_id, client)
            self.disable_channel_analyzers_with_admin_required(self.get_db_chat(db_tg_admin_account, db_chat.chat_id))
        except Exception as e:
            logger.exception(e)
            response.fail('UNKNOWN_ERROR')
        else:
            # logger.info(admin_log)
            logger.info("\n" * 5)
            if admin_log.events:
                now = client, arrow.utcnow().timestamp
                tg_raw_users = {user.id: user for user in admin_log.users} if admin_log.users else {}
                tg_raw_chats = {chat.id: chat for chat in admin_log.chats} if admin_log.chats else {}

                with transaction.atomic():
                    for event in reversed(admin_log.events):
                        event: ChannelAdminLogEvent = event
                        logger.info(event)
                        _id = f"{db_chat.chat_id}:{event.id}"
                        try:
                            self.tg_models.AdminLogEvent.objects.get(
                                id=_id,
                            )
                        except exceptions.ObjectDoesNotExist as e:
                            action_type = type(event.action)
                            try:
                                db_user = self.get_or_create_db_tg_user(
                                    client.get_users(event.user_id),
                                    client,
                                    update_current=True,
                                )
                            except Exception as e:
                                logger.exception(e)
                            else:
                                db_event = self.tg_models.AdminLogEvent(
                                    id=_id,
                                    event_id=event.id,
                                    user=db_user,
                                    chat=db_chat,
                                    logged_by=db_tg_admin_account,
                                    date=event.date,
                                )
                                if action_type == ChannelAdminLogEventActionChangeTitle:
                                    db_event.action_change_title = self.tg_models.AdminLogEventActionChangeTitle.objects.create(
                                        prev_value=event.action.prev_value,
                                        new_value=event.action.new_value
                                    )
                                    db_event.save()
                                    # todo: update chat and channel title

                                elif action_type == ChannelAdminLogEventActionChangeAbout:
                                    db_event.action_change_about = self.tg_models.AdminLogEventActionChangeAbout.objects.create(
                                        prev_value=event.action.prev_value,
                                        new_value=event.action.new_value
                                    )
                                    db_event.save()
                                    # todo: update chat and channel description

                                elif action_type == ChannelAdminLogEventActionChangeUsername:
                                    db_event.action_change_username = self.tg_models.AdminLogEventActionChangeUsername.objects.create(
                                        prev_value=event.action.prev_value,
                                        new_value=event.action.new_value
                                    )
                                    db_event.save()
                                    # todo: update channel/chat username

                                elif action_type == ChannelAdminLogEventActionChangePhoto:
                                    db_event.action_change_photo = self.tg_models.AdminLogEventActionChangePhoto.objects.create(
                                    )
                                    db_event.save()

                                elif action_type == ChannelAdminLogEventActionToggleInvites:
                                    db_event.action_toggle_invites = self.tg_models.AdminLogEventActionToggleInvites.objects.create(
                                        new_value=event.action.new_value
                                    )
                                    db_event.save()

                                elif action_type == ChannelAdminLogEventActionToggleSignatures:
                                    db_event.action_toggle_signatures = self.tg_models.AdminLogEventActionToggleSignatures.objects.create(
                                        new_value=event.action.new_value
                                    )
                                    db_event.save()

                                elif action_type == ChannelAdminLogEventActionUpdatePinned:
                                    tg_message = trio.run(
                                        Message._parse,
                                        client,
                                        event.action.message,
                                        tg_raw_users,
                                        tg_raw_chats,
                                        False,
                                    )
                                    db_event.action_update_pinned = self.tg_models.AdminLogEventActionUpdatePinned.objects.create(
                                        message=self.get_or_create_db_tg_message(
                                            tg_message,
                                            db_chat,
                                            client,
                                            now,
                                        )
                                    )
                                    db_event.save()

                                elif action_type == ChannelAdminLogEventActionEditMessage:
                                    tg_message_prev = trio.run(
                                        Message._parse,
                                        client,
                                        event.action.prev_message,
                                        tg_raw_users,
                                        tg_raw_chats,
                                    )
                                    tg_message_new = trio.run(
                                        Message._parse,
                                        client,
                                        event.action.new_message,
                                        tg_raw_users,
                                        tg_raw_chats,
                                    )
                                    db_event.action_edit_message = self.tg_models.AdminLogEventActionEditMessage.objects.create(
                                        prev_message=self.get_or_create_db_tg_message(
                                            tg_message_prev,
                                            db_chat,
                                            client,
                                            now,
                                        ),
                                        new_message=self.get_or_create_db_tg_message(
                                            tg_message_new,
                                            db_chat,
                                            client,
                                            now,
                                        ),
                                    )
                                    db_event.save()

                                elif action_type == ChannelAdminLogEventActionDeleteMessage:
                                    tg_message = trio.run(
                                        Message._parse,
                                        client,
                                        event.action.message,
                                        tg_raw_users,
                                        tg_raw_chats,
                                    )
                                    db_event.action_delete_message = self.tg_models.AdminLogEventActionDeleteMessage.objects.create(
                                        message=self.get_or_create_db_tg_message(
                                            tg_message,
                                            db_chat,
                                            client,
                                            now,
                                            deletion_date=event.date,
                                        )
                                    )
                                    db_event.save()

                                elif action_type == ChannelAdminLogEventActionParticipantJoin:
                                    db_event.action_participant_join = self.tg_models.AdminLogEventActionParticipantJoin.objects.create()
                                    db_event.save()
                                    db_membership = self.get_or_create_membership(db_chat, db_user)
                                    db_participant = self.get_or_create_participant_by_event(
                                        client=db_membership,
                                        db_membership=db_membership,
                                        event_type='join',
                                        event_date=event.date,
                                    )
                                    self.update_membership_status(
                                        db_membership=db_membership,
                                        db_participant=db_participant,
                                        event_date=event.date,
                                    )

                                elif action_type == ChannelAdminLogEventActionParticipantLeave:
                                    db_event.action_participant_leave = self.tg_models.AdminLogEventActionParticipantLeave.objects.create()
                                    db_event.save()
                                    db_membership = self.get_or_create_membership(db_chat, db_user)
                                    db_participant = self.get_or_create_participant_by_event(
                                        client=client,
                                        db_membership=db_membership,
                                        event_type='left',
                                        event_date=event.date,
                                    )
                                    self.update_membership_status(
                                        db_membership=db_membership,
                                        db_participant=db_participant,
                                        event_date=event.date,
                                    )

                                elif action_type == ChannelAdminLogEventActionParticipantInvite:
                                    tg_invited_user = User._parse(
                                        client,
                                        tg_raw_users[event.action.participant.user_id]
                                    )
                                    db_invited_user = self.get_or_create_db_tg_user(
                                        tg_invited_user,
                                        client,
                                        update_current=True,
                                    )
                                    db_invited_user_membership = self.get_or_create_membership(
                                        db_chat,
                                        db_invited_user
                                    )
                                    db_participant = self.get_or_create_participant_by_event(
                                        client=client,
                                        db_membership=db_invited_user_membership,
                                        event_type='invite',
                                        event_date=event.date,
                                        by=db_user,
                                        tg_raw_participant=event.action.participant,
                                        tg_raw_users=tg_raw_users,
                                    )
                                    db_event.action_participant_invite = self.tg_models.AdminLogEventActionParticipantInvite.objects.create(
                                        participant=db_participant,
                                    )
                                    db_event.save()
                                    self.update_membership_status(
                                        db_membership=db_invited_user_membership,
                                        db_participant=db_participant,
                                        event_date=event.date,
                                    )

                                elif action_type == ChannelAdminLogEventActionParticipantToggleBan:
                                    prev_tg_user = User._parse(
                                        client,
                                        tg_raw_users[event.action.prev_participant.user_id]
                                    )
                                    db_membership = self.get_or_create_membership(
                                        db_chat,
                                        db_user=self.get_or_create_db_tg_user(
                                            prev_tg_user,
                                            client,
                                            update_current=True,
                                        )
                                    )

                                    prev_participant = self.get_or_create_participant_by_event(
                                        client=client,
                                        db_membership=db_membership,
                                        event_type='toggle_ban',
                                        event_date=event.date,
                                        is_previous_participant=True,
                                        tg_raw_participant=event.action.prev_participant,
                                        tg_raw_users=tg_raw_users,
                                    )
                                    new_participant = self.get_or_create_participant_by_event(
                                        client=client,
                                        db_membership=db_membership,
                                        event_type='toggle_ban',
                                        event_date=event.date,
                                        by=db_user,
                                        is_previous_participant=False,
                                        tg_raw_participant=event.action.new_participant,
                                        tg_raw_users=tg_raw_users,
                                    )

                                    db_event.action_participant_toggle_ban = self.tg_models.AdminLogEventActionToggleBan.objects.create(
                                        prev_participant=prev_participant,
                                        new_participant=new_participant,
                                    )
                                    db_event.save()

                                    self.update_membership_status(
                                        db_membership=db_membership,
                                        db_participant=prev_participant,
                                        event_date=event.date,
                                    )
                                    self.update_membership_status(
                                        db_membership=db_membership,
                                        db_participant=new_participant,
                                        event_date=event.date,
                                    )

                                elif action_type == ChannelAdminLogEventActionParticipantToggleAdmin:
                                    prev_tg_user = User._parse(
                                        client,
                                        tg_raw_users[event.action.prev_participant.user_id]
                                    )
                                    db_membership = self.get_or_create_membership(
                                        db_chat,
                                        db_user=self.get_or_create_db_tg_user(
                                            prev_tg_user,
                                            client,
                                            update_current=True,
                                        )
                                    )

                                    if prev_tg_user.id == db_tg_admin_account.user_id:
                                        temp_channel = self.get_db_tg_channel(db_tg_admin_account, db_chat.chat_id)
                                        temp_admin = db_tg_admin_account

                                    prev_participant = self.get_or_create_participant_by_event(
                                        client=client,
                                        db_membership=db_membership,
                                        event_type='toggle_admin',
                                        event_date=event.date,
                                        is_previous_participant=True,
                                        tg_raw_participant=event.action.prev_participant,
                                        tg_raw_users=tg_raw_users,

                                        db_tg_channel=temp_channel,
                                        db_tg_admin_account=temp_admin,
                                    )

                                    new_participant = self.get_or_create_participant_by_event(
                                        client=client,
                                        db_membership=db_membership,
                                        event_type='toggle_admin',
                                        event_date=event.date,
                                        by=db_user,
                                        is_previous_participant=False,
                                        tg_raw_participant=event.action.new_participant,
                                        tg_raw_users=tg_raw_users,

                                        db_tg_channel=temp_channel,
                                        db_tg_admin_account=temp_admin,
                                    )

                                    db_event.action_participant_toggle_admin = self.tg_models.AdminLogEventActionToggleAdmin.objects.create(
                                        prev_participant=prev_participant,
                                        new_participant=new_participant
                                    )
                                    db_event.save()

                                    self.update_membership_status(
                                        db_membership=db_membership,
                                        db_participant=prev_participant,
                                        event_date=event.date,
                                    )
                                    self.update_membership_status(
                                        db_membership=db_membership,
                                        db_participant=new_participant,
                                        event_date=event.date,
                                    )

                                    if get_class_name(event.action.prev_participant) in self._names and get_class_name(
                                            event.action.new_participant) == "ChannelParticipantAdmin":
                                        # this tg_account was promoted to admin;
                                        self.promote_account(db_chat.chat_id, db_tg_admin_account)

                                    elif get_class_name(event.action.new_participant) in self._names and get_class_name(
                                            event.action.prev_participant) == "ChannelParticipantAdmin":
                                        # this tg_account was demoted to participant;
                                        pass
                                    elif get_class_name(
                                            event.action.new_participant) == "ChannelParticipantAdmin" and get_class_name(
                                        event.action.prev_participant) == "ChannelParticipantAdmin":
                                        # this tg_account's admin rights was changed
                                        # the new rights is updated already
                                        pass

                                elif action_type == ChannelAdminLogEventActionChangeStickerSet:
                                    db_event.action_change_sticker_set = self.tg_models.AdminLogEventActionChangeStickerSet.objects.create()
                                    db_event.save()

                                elif action_type == ChannelAdminLogEventActionTogglePreHistoryHidden:
                                    db_event.action_toggle_prehistory_hidden = self.tg_models.AdminLogEventActionTogglePreHistoryHidden.objects.create(
                                        new_value=event.action.new_value
                                    )
                                    db_event.save()

                                elif action_type == ChannelAdminLogEventActionDefaultBannedRights:
                                    db_event.action_default_banned_rights = self.tg_models.AdminLogEventActionDefaultBannedRights.objects.create(
                                        prev_banned_rights=self.create_chat_banned_rights_from_raw_rights(
                                            event.action.prev_banned_rights
                                        ),
                                        new_banned_rights=self.create_chat_banned_rights_from_raw_rights(
                                            event.action.new_banned_rights
                                        ),
                                    )
                                    db_event.save()

                                elif action_type == ChannelAdminLogEventActionStopPoll:
                                    db_event.action_stop_poll = self.tg_models.AdminLogEventActionStopPoll.objects.create(
                                        message=self.get_or_create_db_tg_message(
                                            trio.run(
                                                Message._parse,
                                                event.action.message,
                                                tg_raw_users,
                                                tg_raw_chats,
                                            ),
                                            db_chat,
                                            client,
                                            now,
                                        )
                                    )
                                    db_event.save()

                                elif action_type == ChannelAdminLogEventActionChangeLinkedChat:
                                    db_event.action_change_linked_chat = self.tg_models.AdminLogEventActionChangeLinkedChat.objects.create(
                                        prev_value=event.action.prev_value,
                                        new_value=event.action.new_value,
                                    )
                                    db_event.save()
                                    # todo: update model?

                                elif action_type == ChannelAdminLogEventActionChangeLocation:
                                    prev_location = event.action.prev_value
                                    new_location = event.action.new_value

                                    prev_address = getattr(prev_location, 'address', None)
                                    new_address = getattr(new_location, 'address', None)

                                    prev_geo = getattr(prev_location, 'geo_point', None)
                                    if prev_geo:
                                        prev_lat = getattr(prev_geo, 'lat', None)
                                        prev_long = getattr(prev_geo, 'long', None)
                                        prev_access_hash = getattr(prev_geo, 'access_hash', None)

                                    new_geo = getattr(prev_location, 'geo_point', None)
                                    if new_geo:
                                        new_lat = getattr(new_geo, 'lat', None)
                                        new_long = getattr(new_geo, 'long', None)
                                        new_access_hash = getattr(new_geo, 'access_hash', None)
                                    db_event.action_participant_invite = self.tg_models.AdminLogEventActionChangeLocation.objects.create(
                                        prev_address=prev_address,
                                        prev_lat=prev_lat,
                                        prev_long=prev_long,
                                        prev_access_hash=prev_access_hash,

                                        new_address=new_address,
                                        new_lat=new_lat,
                                        new_long=new_long,
                                        new_access_hash=new_access_hash,
                                    )
                                    db_event.save()

                                elif action_type == ChannelAdminLogEventActionToggleSlowMode:
                                    db_event.action_toggle_slow_mode = self.tg_models.AdminLogEventActionToggleSlowMode.objects.create(
                                        prev_value=event.action.prev_value,
                                        new_value=event.action.new_value,
                                    )
                                    db_event.save()
                                    # todo: update model?
                        except Exception as e:
                            logger.exception(e)
                        else:
                            # event exits in the db
                            pass

            response.done()

        return response

    def analyze_chat_members(self, client: Client, db_chat, response: BaseResponse, _filter=None):
        try:
            tg_full_chat: Chat = client.get_chat(db_chat.chat_id)

            for chat_member in client.iter_chat_members(
                    db_chat.chat_id,
                    filter=_filter if _filter else Filters.ALL,
                    last_member_count=tg_full_chat.members_count,
            ):
                chat_member: ChatMember = chat_member
                now = arrow.utcnow().timestamp
                try:
                    db_user = self.tg_models.User.objects.get(
                        user_id=chat_member.user.id
                    )
                except exceptions.ObjectDoesNotExist as e:
                    # user and membership does not exist, create them
                    tg_user = chat_member.user
                    db_user = self.get_or_create_db_tg_user(tg_user, client, update_current=True, )
                    db_membership = self.get_or_create_membership(db_chat, db_user)
                    db_participant = self.create_channel_participant_from_chat_member(
                        chat_member=chat_member,
                        db_membership=db_membership,
                        client=client,
                        event_date=now,
                    )
                    self.update_membership_status(
                        db_membership=db_membership,
                        db_participant=db_participant,
                        event_date=now
                    )
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
                        db_participant = self.create_channel_participant_from_chat_member(
                            chat_member=chat_member,
                            db_membership=db_membership,
                            client=client,
                            event_date=now,
                        )
                        self.update_membership_status(
                            db_membership=db_membership,
                            db_participant=db_participant,
                            event_date=now
                        )
                        response.done()
                    else:
                        self.update_membership_status(
                            db_membership=db_membership,
                            chat_member=chat_member,
                            client=client,
                            event_date=now,
                        )

                        response.done()
        except tg_errors.RPCError as e:
            logger.exception(e)
            response.fail('TG_ERROR')
        except Exception as e:
            logger.exception(e)
            response.fail('UNKNOWN_ERROR')

        return response

    ########################################

    def get_all_dialogs(self, client: Client):
        if not client:
            return None
        offset_date = 0
        dialogs = []
        while True:
            try:
                dialogs_slice = client.get_dialogs(offset_date, )
            except tg_errors.RPCError:
                pass
            except Exception as e:
                logger.exception(e)
            else:
                if dialogs_slice:
                    dialogs.extend(dialogs_slice)
                    offset_date = dialogs_slice[-1].top_message.date
                else:
                    break
        return dialogs


class TelegramConsumerManager(Thread):
    def __init__(self, clients, i):
        Thread.__init__(self)
        self.clients = clients
        self.daemon = True
        self.name = 'Telegram_Consumer_Manager_Thread'
        self.index = i

    def run(self) -> None:
        logger.info(f"Telegram Consumer {self.index} started ....")
        Worker(connection=Connection('amqp://localhost'), clients=clients, index=self.index).run()


class TelegramClientManager(DataBaseManager):

    def __init__(self, clients: list):
        super().__init__(clients)
        self.clients = clients
        self.name = 'telegram_client_thread'
        from telegram import models
        self.tg_models = models

    def on_disconnect(self, client: Client):
        import arrow
        logger.info(f"client {client.session_name} disconnected @ {arrow.utcnow()}")

    def on_message(self, client: Client, message: Message):
        # logger.info('on_message:: %s : %s' % (mp.current_process().name, threading.current_thread().name))
        logger.info(f"in on_message : {threading.current_thread()}")
        logger.info(message)
        self.handle_new_message(client, message)

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
        elif get_class_name(update) == 'UpdateDeleteChannelMessages':
            self.update_db_message_to_deleted(update)
        else:
            pass
        logger.info("*" * 30)

    # noinspection PyTypeChecker
    def handle_channel_update(self, client: Client, update):
        channel_id = int('-100' + str(update.channel_id))
        # find the active telegram account associated with this client
        db_tg_admin = self.get_db_telegram_account_by_client(client)
        try:
            admin_logs: AdminLogResults = client.send(
                raw.functions.channels.GetAdminLog(
                    channel=client.resolve_peer(peer_id=channel_id),
                    q="",
                    min_id=0,
                    max_id=0,
                    events_filter=ChannelAdminLogEventsFilter(promote=True, demote=True),
                    admins=None,
                    limit=1  # fixme: what is the issue?
                )
            )
            logger.info(admin_logs)
        except tg_errors.ChatAdminRequired as e:
            self.disable_channel_with_analyzers(client, db_tg_admin, channel_id)
        except tg_errors.ChatWriteForbidden as e:
            self.disable_channel_with_analyzers(client, db_tg_admin, channel_id)
        except Exception as e:
            logger.exception(e)
        else:
            tasks.admin_logs_analyzer.apply_async(
                kwargs={
                    'db_tg_admin_id': db_tg_admin.user_id,
                    'chat_id': channel_id,
                },
                countdown=0,
            )

    def handle_new_message(self, client: Client, message: Message):
        # check if the chat is the type of `channel` and it's `public` (current policy)
        if message and message.chat and message.chat.username and message.chat.type == 'channel':
            now = arrow.utcnow().timestamp
            db_chat = self.get_or_create_db_tg_chat(
                message.chat,
                self.tg_models.TelegramAccount.objects.get(
                    session_name=client.session_name,
                    is_deleted=False,
                ),
                client,
                update_current=True,
            )
            if db_chat:
                self.get_or_create_db_tg_message(
                    message,
                    db_chat,
                    client,
                    now,
                )
                client.read_history(db_chat.chat_id, max_id=message.message_id)
            else:
                db_telegram_account = self.tg_models.TelegramAccount.objects.get(
                    is_deleted=False,
                    session_name=client.session_name,
                )
                db_chat = self.get_or_create_db_tg_chat(
                    message.chat,
                    db_telegram_account,
                    client,
                    update_current=True,
                    is_tg_full_chat=False,
                )
                self.get_or_create_db_tg_message(
                    message,
                    db_chat,
                    client,
                    now,
                )

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
    for i in range(tg_globals.number_of_telegram_workers):
        TelegramConsumerManager(clients, i + 1).start()

    TelegramClientManager(clients).run()
