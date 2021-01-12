from typing import Optional, Tuple

from django.db import models, DatabaseError

from ..base import BaseModel
from telegram import models as tg_models
from core.globals import logger
from pyrogram import types


class MembershipQuerySet(models.QuerySet):
    def update_or_create_membership(self, *, defaults: dict, **kwargs) -> Optional['Membership']:
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

    def update_membership(self, **kwargs) -> bool:
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

        return None

    def filter_by_user_and_chat(self, *, db_user: 'tg_models.User', db_chat: 'tg_models.Chat') -> 'MembershipQuerySet':
        return self.filter(
            user=db_user,
            chat=db_chat,
        )

    def get_by_user_and_chat(self, *, db_user: 'tg_models.User', db_chat: 'tg_models.Chat') -> Optional['Membership']:
        db_membership = None
        try:
            db_membership = self.get(user=db_user, chat=db_chat)
        except Membership.DoesNotExist as e:
            pass
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return db_membership

    def get_by_user_id_and_chat(self, *, user_id: int, db_chat: 'tg_models.Chat') -> Optional['Membership']:
        db_membership = None
        try:
            db_membership = self.get(user__user_id=user_id, chat=db_chat)
        except Membership.DoesNotExist as e:
            pass
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)

        return db_membership


class MembershipManager(models.Manager):
    def get_queryset(self) -> MembershipQuerySet:
        return MembershipQuerySet(self.model, using=self._db)

    def update_or_create_membership(
            self,
            *,
            db_user: 'tg_models.User',
            db_chat: 'tg_models.Chat',
            new_status: 'tg_models.ChatMember',
            event_date_ts: int,
    ) -> Optional['Membership']:

        if db_user is not None or db_chat is not None or new_status:
            return None

        return self.get_queryset().update_or_create_membership(
            user=db_user,
            chat=db_chat,
            defaults={
                'current_status': new_status,
                'status_change_date_ts': event_date_ts
            }
        )

    def get_membership(self, *, db_user: 'tg_models.User', db_chat: 'tg_models.Chat') -> Optional['Membership']:
        return self.get_queryset().get_by_user_and_chat(db_user=db_user, db_chat=db_chat)

    def get_membership_by_user_id(
            self,
            *,
            user_id: int,
            db_chat: 'tg_models.Chat',
    ) -> Optional['Membership']:
        return self.get_queryset().get_by_user_id_and_chat(user_id=user_id, db_chat=db_chat)

    def is_status_changed(
            self,
            *,
            db_user: 'tg_models.User',
            db_chat: 'tg_models.Chat',
            raw_chat_member: types.ChatMember
    ) -> Tuple['Membership', bool]:

        if db_user is None or db_chat is None or raw_chat_member is None:
            return None, False

        db_membership = self.get_membership(db_user=db_user, db_chat=db_chat)
        if db_membership:
            return db_membership, db_membership.current_status and db_membership.current_status.type == raw_chat_member.status
        else:
            return None, False

    @staticmethod
    def update_membership_status(
            *,
            db_membership: 'tg_models.Membership',
            new_status: 'tg_models.ChatMember',
            event_date_ts: int
    ) -> bool:

        if db_membership is None or new_status is None or event_date_ts is None:
            return False

        if not db_membership.current_status and not db_membership.previous_status:
            db_membership.current_status = new_status
            db_membership.status_change_date = event_date_ts
            db_membership.save()

        elif not db_membership.previous_status and db_membership.current_status:
            if event_date_ts < db_membership.status_change_date:
                db_membership.previous_status = new_status
                db_membership.save()
            elif event_date_ts > db_membership.status_change_date:
                db_membership.previous_status, db_membership.current_status = db_membership.current_status, new_status
                db_membership.status_change_date = event_date_ts
                db_membership.save()
            elif event_date_ts == db_membership.status_change_date:
                if not new_status.is_previous and db_membership.current_status.is_previous:
                    db_membership.previous_status, db_membership.current_status = db_membership.current_status, new_status
                    db_membership.save()
                elif new_status.is_previous and not db_membership.current_status.is_previous:
                    db_membership.previous_status = new_status
                    db_membership.save()
                else:
                    raise Exception("Oops!, why?")

        elif db_membership.current_status and db_membership.previous_status:
            if event_date_ts < db_membership.status_change_date:
                if event_date_ts < db_membership.previous_status.event_date_ts:
                    pass
                elif event_date_ts > db_membership.previous_status.event_date_ts:
                    db_membership.previous_status = new_status
                    db_membership.save()
                elif event_date_ts == db_membership.previous_status.event_date_ts:
                    if not new_status.is_previous and db_membership.previous_status.is_previous:
                        db_membership.previous_status = new_status
                        db_membership.save()
                    elif new_status.is_previous and not db_membership.previous_status.is_previous:
                        pass
                    else:
                        raise Exception("Oops!, why?")
            elif event_date_ts > db_membership.status_change_date:
                db_membership.previous_status, db_membership.current_status = db_membership.current_status, new_status
                db_membership.status_change_date = event_date_ts
                db_membership.save()
            elif event_date_ts == db_membership.status_change_date:
                if not new_status.is_previous and db_membership.current_status.is_previous:
                    db_membership.previous_status, db_membership.current_status = db_membership.current_status, new_status
                    db_membership.save()
                elif new_status.is_previous and not db_membership.current_status.is_previous:
                    db_membership.previous_status = new_status
                    db_membership.save()
                else:
                    raise Exception("Oops!, why?")

        return True


class Membership(BaseModel):
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
        'telegram.ChatMember',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='+'
    )
    previous_status = models.OneToOneField(
        'telegram.ChatMember',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='+'
    )

    status_change_date_ts = models.BigIntegerField(null=True, blank=True)

    objects = MembershipManager()

    ######################################
    # `participant_history` : participants related to this membership

    def update_membership_status(
            self,
            *,
            new_status: 'tg_models.ChatMember',
            event_date_ts: int
    ) -> bool:
        return Membership.objects.update_membership_status(
            db_membership=self,
            new_status=new_status,
            event_date_ts=event_date_ts
        )

    def __str__(self):
        return f"{self.user} @ {self.chat} : {self.current_status.type if self.current_status else ''}"
