from typing import Optional
from django.db import DatabaseError, transaction
from django.db import models
from ..base import BaseModel
from db.models import (SoftDeletableBaseModel, SoftDeletableQS)
from telegram import models as tg_models
from core.globals import logger


class DialogQuerySet(SoftDeletableQS):
    def get_dialog(self, *, id: str) -> Optional["Dialog"]:
        if not id:
            return None
        try:
            return self.get(id=id)
        except Dialog.DoesNotExist as e:
            pass
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None

    def update_or_create_dialog(self, **kwargs) -> Optional["Dialog"]:
        try:
            return self.update_or_create(
                **kwargs
            )[0]
        except DatabaseError as e:
            logger.exception(e)
        except Exception as e:
            logger.exception(e)
        return None

    def update_dialog(self, **kwargs) -> bool:
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

    def filter_by_id(self, *, id: str) -> "DialogQuerySet":
        return self.filter(id=id)


class DialogManager(models.Manager):
    def get_queryset(self) -> DialogQuerySet:
        return DialogQuerySet(self.model, using=self._db)

    def get_dialog(
            self,
            *,
            chat: "tg_models.Chat",
            account: "tg_models.TelegramAccount"
    ) -> Optional["Dialog"]:

        if not chat or not account:
            return None
        return self.get_queryset().get_dialog(id=f'{chat.chat_id}:{account.user_id}')

    def update_or_create_dialog(
            self,
            *,
            db_chat: "tg_models.Chat",
            db_account: "tg_models.TelegramAccount",
            is_member: bool = True,
            left_date_ts: int = None,
    ) -> Optional["Dialog"]:

        if not db_chat or not db_account:
            return None
        kwargs = {
            'id': f'{db_account.user_id}:{db_chat.chat_id}',
            'chat': db_chat,
            'account': db_account,
            'is_member': is_member,
        }
        if left_date_ts:
            kwargs.update(
                {
                    'left_date_ts': left_date_ts
                }
            )
        return self.get_queryset().update_or_create_dialog(
            **kwargs
        )


class Dialog(BaseModel, SoftDeletableBaseModel):
    id = models.CharField(max_length=265, primary_key=True, )  # `user_id:chat_id`
    chat = models.ForeignKey(
        'telegram.Chat',
        on_delete=models.CASCADE,
        null=False,
        related_name='dialogs',
    )

    account = models.ForeignKey(
        'telegram.TelegramAccount',
        on_delete=models.CASCADE,
        null=False,
        related_name='dialogs',
    )

    is_member = models.BooleanField(default=True, blank=True, )
    left_date_ts = models.BigIntegerField(null=True, blank=True, )

    objects = DialogManager()

    def __str__(self):
        return f"{self.account} : {self.chat}"
