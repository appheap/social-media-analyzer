from tasks.task_scaffold import TaskScaffold
from ..base_response import BaseResponse
from typing import List
from pyrogram import types
from pyrogram import errors as tg_errors
from core.globals import logger


class IterateDialogsTask(TaskScaffold):

    def iterate_dialogs_task(self, *args, **kwargs) -> BaseResponse:
        tg_account_ids = kwargs.get('tg_account_ids', None)
        if tg_account_ids is None:
            return BaseResponse().fail('missing `tg_account_ids` kwarg')

        db_telegram_accounts = self.db.telegram.get_telegram_accounts_by_ids(
            ids=tg_account_ids
        )
        if db_telegram_accounts is None or not len(db_telegram_accounts):
            return BaseResponse().fail('no telegram account is available now')

        for db_telegram_account in db_telegram_accounts:
            client = self.get_client(db_telegram_account.session_name)
            if client is None:
                continue

            raw_dialogs: List['types.Dialog'] = client.get_all_dialogs()
            if raw_dialogs is None or not len(raw_dialogs):
                continue

            _valid_raw_dialogs = []
            for raw_dialog in raw_dialogs:
                if raw_dialog.chat.group and raw_dialog.chat.group.migrated_to:
                    raw_migrated_chat = self.db.telegram.get_updated_migrated_raw_chat(
                        raw_chat=raw_dialog.chat,
                        db_telegram_account=db_telegram_account,
                        client=client,
                    )
                    if raw_migrated_chat:
                        raw_dialog.chat = raw_migrated_chat
                        db_chat = self.db.telegram.get_updated_chat(
                            raw_chat=raw_migrated_chat,
                            db_telegram_account=db_telegram_account,
                            downloader=client.download_media
                        )
                        _valid_raw_dialogs.append(raw_dialog)
                else:
                    db_chat = self.db.telegram.get_updated_chat(
                        raw_chat=raw_dialog.chat,
                        db_telegram_account=db_telegram_account,

                        downloader=client.download_media
                    )
                    _valid_raw_dialogs.append(raw_dialog)

            db_dialogs = self.db.telegram.get_updated_dialogs(
                raw_dialogs=_valid_raw_dialogs,
                db_telegram_account=db_telegram_account,
                update_chat=False,
            )

            if db_dialogs is None:
                continue

            for raw_dialog in _valid_raw_dialogs:
                raw_chat: types.Chat = raw_dialog.chat
                if raw_chat is None:
                    continue

                if raw_chat.type == 'channel':
                    db_telegram_channel = self.db.telegram.get_updated_telegram_channel(
                        raw_chat=raw_chat,
                        db_account=db_telegram_account,
                    )
                    if db_telegram_channel:
                        self.db.telegram.update_chat_analyzers_status(
                            db_chat=db_telegram_channel.chat,
                            enabled=raw_chat.is_admin,
                            only_admin_based_analyzers=True,
                        )
        return BaseResponse().done()
