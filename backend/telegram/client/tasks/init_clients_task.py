from tasks.task_scaffold import TaskScaffold
import pyrogram
from pyrogram import types
from ..base_response import BaseResponse
from telegram import tasks


class InitClientsTask(TaskScaffold):
    def init_clients_task(self, *args, **kwargs) -> BaseResponse:
        tg_accounts_to_be_iterated = []
        for client in self.clients:
            client: pyrogram.Client = client

            me: types.User = client.get_me()
            db_site_user = self.db.users.get_default_site_user()
            if db_site_user is None:
                return BaseResponse().fail('Could not find site_user with DEFAULT_USER_USERNAME')

            db_tg_admin_account = self.db.telegram.get_updated_telegram_account(
                db_site_user=db_site_user,
                raw_user=me,
                client=client,
            )
            # update chats table for each account
            if db_tg_admin_account:
                tg_accounts_to_be_iterated.append(db_tg_admin_account.user_id)

        tasks.iterate_dialogs.apply_async(
            kwargs={
                'tg_account_ids': tg_accounts_to_be_iterated,
            },
            countdown=0,
        )
        return BaseResponse().done(message='client init successful')
