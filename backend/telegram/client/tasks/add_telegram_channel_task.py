from tasks.task_scaffold import TaskScaffold
from ..base_response import BaseResponse
import pyrogram
from pyrogram import types
from pyrogram import errors as tg_errors
from core.globals import logger


class AddTelegramChannelTask(TaskScaffold):

    def add_telegram_channel_task(
            self,
            *args,
            **kwargs
    ) -> BaseResponse:
        db_admin_telegram_account_id = kwargs.get('db_tg_account_admin_id', None)
        channel_username = kwargs.get('channel_username', None)
        db_site_user_id = kwargs.get('db_userid', None)

        response = BaseResponse()

        if db_admin_telegram_account_id is None or channel_username is None or db_site_user_id is None:
            return response.fail('Invalid args')

        db_site_user = self.db.users.get_user_by_id(user_id=db_site_user_id)
        if not db_site_user:
            return response.fail('No such user exists')

        db_admin_telegram_account = self.db.telegram.get_telegram_account_by_id(id=db_admin_telegram_account_id)
        if not db_admin_telegram_account:
            return response.fail('Invalid Admin account')

        client = self.get_client(db_admin_telegram_account.session_name)
        if not client:
            return response.fail('Admin Client is not available right now.')
        if not client.is_connected:
            return response.fail('Sorry, that Admin account is not connected now.')

        if self.db.telegram.telegram_channel_exists(
                db_site_user=db_site_user,
                channel_username=channel_username,
        ):
            return response.fail('this channel is already added')

        try:
            raw_chat: types.Chat = client.get_chat(chat_id=channel_username)
        except tg_errors.ChatIdInvalid or tg_errors.ChannelInvalid or tg_errors.UserIdInvalid:
            return response.fail('username is invalid')
        except tg_errors.ChannelPrivate:
            return response.fail('channel is private')
        except tg_errors.ChannelPublicGroupNa:
            return response.fail('channel is not available')
        except tg_errors.RPCError as e:
            logger.error(e)
            # fixme: better response?
            return response.fail('TG_RPC_ERROR')
        except Exception as e:
            logger.exception(e)
            return response.fail('UNKNOWN_ERROR')
        else:
            if raw_chat is None:
                return response.fail('UNKNOWN_ERROR')

            if raw_chat.type == 'channel' and raw_chat.username is not None:
                try:
                    raw_chat_temp = client.join_chat(raw_chat.id)
                except tg_errors.ChannelsTooMuch as e:
                    # todo: what now?
                    return response.fail('Please select another admin')
                except tg_errors.UsersTooMuch as e:
                    return response.fail('Channel capacity is full')
                except tg_errors.UserAlreadyParticipant as e:
                    response.done('Admin has already joined.')
                    return self._join_channel(
                        response=response,
                        raw_chat=raw_chat,
                        raw_chat_temp=raw_chat_temp,
                        db_admin_telegram_account=db_admin_telegram_account,
                        db_site_user=db_site_user,
                        channel_username=channel_username,
                        client=client
                    )
                except tg_errors.RPCError as e:
                    logger.error(e)
                    return response.fail('TG_RPC_ERROR')
                except Exception as e:
                    logger.exception(e)
                    return response.fail('UNKNOWN_ERROR')
                else:
                    return self._join_channel(
                        response=response,
                        raw_chat=raw_chat,
                        raw_chat_temp=raw_chat_temp,
                        db_admin_telegram_account=db_admin_telegram_account,
                        db_site_user=db_site_user,
                        channel_username=channel_username,
                        client=client
                    )

            else:
                return response.fail('Only public channels can be added')

    def _join_channel(
            self,
            *,
            response: BaseResponse,
            raw_chat: 'types.Chat',
            raw_chat_temp: 'types.Chat',
            db_admin_telegram_account: 'tg_models.TelegramAccount',
            db_site_user: 'site_models.SiteUser',
            channel_username: 'str',
            client: 'pyrogram.Client'
    ) -> BaseResponse:
        if not raw_chat_temp:
            return response.fail('UNKNOWN_ERROR')

        db_chat = self.db.telegram.get_updated_chat(
            raw_chat=raw_chat,
            db_telegram_account=db_admin_telegram_account,

            downloader=client.download_media
        )
        db_telegram_channel = self.db.telegram.get_updated_telegram_channel(
            raw_chat=raw_chat,
            db_account=db_admin_telegram_account,
            db_site_user=db_site_user,
        )
        db_add_telegram_channel_request = self.db.telegram.create_add_channel_request(
            db_site_user=db_site_user,
            db_admin=db_admin_telegram_account,
            channel_username=channel_username,
            db_telegram_channel=db_telegram_channel,
        )

        if not db_chat or not db_telegram_channel or not db_add_telegram_channel_request:
            return response.fail('database error')

        if response.success:
            return response
        return response.done('Joined Channel')
