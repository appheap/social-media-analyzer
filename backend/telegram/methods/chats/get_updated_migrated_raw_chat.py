from typing import Optional, Callable

from db.scaffold import Scaffold
from pyrogram import types
from telegram import models as tg_models
import pyrogram
from pyrogram import errors as tg_errors


class GetUpdatedMigratedRawChat(Scaffold):
    def get_updated_migrated_raw_chat(
            self,
            *,
            raw_chat: types.Chat,
            db_telegram_account: 'tg_models.TelegramAccount',
            client: 'pyrogram.Client'
    ) -> Optional["tg_models.Chat"]:

        if raw_chat is None or db_telegram_account is None:
            return None

        db_chat_migrated_from = self.get_updated_chat(
            raw_chat=raw_chat,
            db_telegram_account=db_telegram_account,

            downloader=client.download_media
        )

        if not raw_chat.group or not raw_chat.group.migrated_to:
            return None

        try:
            migrated_raw_chat = None
            migrated_raw_chat = client.get_chat(raw_chat.group.migrated_to.id)
        except tg_errors.ChannelInvalid as e:
            self.logger.info(raw_chat)
            self.logger.error(e)
        except tg_errors.ChannelPrivate as e:
            self.logger.info(raw_chat)
            self.logger.error(e)
        except tg_errors.ChannelPublicGroupNa as e:
            self.logger.info(raw_chat)
            self.logger.error(e)
        except Exception as e:
            self.logger.exception(e)
        else:
            return migrated_raw_chat

        return None
