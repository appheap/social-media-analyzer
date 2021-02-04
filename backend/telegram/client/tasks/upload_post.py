from tasks.task_scaffold import TaskScaffold
import pyrogram
from ..base_response import BaseResponse
from pyrogram import types
from core.globals import logger


class UploadPost(TaskScaffold):
    def upload_post(self, *args, **kwargs) -> BaseResponse:
        from db.models import FileTypes

        db_post_id = kwargs.get('db_post_id', None)
        if db_post_id is None:
            raise ValueError(f'db_post_id cannot be None')

        db_post = self.db.telegram.get_post_by_id(post_id=db_post_id)
        if db_post is None:
            return BaseResponse().fail('post does not exist')

        if db_post.is_sent:
            return BaseResponse().fail('Post is already sent!')

        schedule_upload = db_post.is_scheduled and db_post.upload_to_telegram_schedule_list
        schedule_date = db_post.schedule_date_ts if schedule_upload else None
        if db_post.is_scheduled and not db_post.upload_to_telegram_schedule_list:
            return BaseResponse().done()

        client_session_names = self.get_client_session_names()
        db_telegram_accounts = self.db.telegram.get_telegram_accounts_by_session_names(
            db_chat=db_post.telegram_channel.chat,
            session_names=client_session_names,
            with_admin_permissions=True,
        )
        if db_telegram_accounts is None or not len(db_telegram_accounts):
            return BaseResponse().done(message='No Telegram Account is available now.')

        db_telegram_account = db_telegram_accounts[0]
        client = self.get_client(session_name=db_telegram_account.session_name)

        chat_id = db_post.telegram_channel.chat_id

        medias = []
        if db_post.has_media and db_post.medias.count() > 1:
            for media in db_post.medias.all():
                caption = media.caption if media.caption is not None else ''
                if media.type == FileTypes.photo:
                    medias.append(types.InputMediaPhoto(media.file.path, caption))
                elif media.type == FileTypes.document:
                    medias.append(types.InputMediaDocument(media.file.path, caption))
                elif media.type == FileTypes.video:
                    medias.append(types.InputMediaVideo(media.file.path, caption))
                elif media.type == FileTypes.audio:
                    medias.append(types.InputMediaAudio(media.file.path, caption))
                else:
                    # fixme : what now?
                    pass
        if len(medias):
            raw_messages = client.send_media_group(
                chat_id=chat_id,
                media=medias,
                schedule_date=schedule_date,
                send_in_background=False
            )
            for raw_message in raw_messages:
                raw_message.content.is_scheduled = db_post.is_scheduled

            db_messages = list(self.db.telegram.get_updated_messages(
                db_chat=db_post.telegram_channel.chat,
                raw_messages=raw_messages,
                logger_account=db_telegram_account,
            ))
            if db_messages is None or not len(db_messages):
                raise ValueError('could not store messages in db')

            db_post.update_post_from_message(
                db_message=db_messages[0]
            )

            return BaseResponse().done('uploaded_successfully', data={
                'db_message_id': db_messages[0].id,
                'album_id': db_messages[0].media_group_id
            })
        else:
            if db_post.has_media:
                db_media = db_post.medias.first()
                if db_media.type == FileTypes.photo:
                    raw_message = client.send_photo(
                        chat_id=chat_id,
                        photo=db_media.file.path,
                        caption=db_media.caption if db_media.caption is not None else '',
                        send_in_background=False,
                        schedule_date=schedule_date,
                    )
                elif db_media.type == FileTypes.document:
                    raw_message = client.send_document(
                        chat_id=chat_id,
                        document=db_media.file.path,
                        caption=db_media.caption if db_media.caption is not None else '',
                        send_in_background=False,
                        schedule_date=schedule_date,
                    )
                elif db_media.type == FileTypes.video:
                    raw_message = client.send_video(
                        chat_id=chat_id,
                        video=db_media.file.path,
                        caption=db_media.caption if db_media.caption is not None else '',
                        send_in_background=False,
                        schedule_date=schedule_date,
                    )
                elif db_media.type == FileTypes.audio:
                    raw_message = client.send_audio(
                        chat_id=chat_id,
                        audio=db_media.file.path,
                        caption=db_media.caption if db_media.caption is not None else '',
                        send_in_background=False,
                        schedule_date=schedule_date,
                    )
                else:
                    raw_message = None
            else:
                raw_message = client.send_message(
                    chat_id=chat_id,
                    text=db_post.text if db_post.text is not None else '',
                    schedule_date=schedule_date,
                )

            if raw_message is None:
                return BaseResponse().fail('Failed to upload')

            raw_message.content.is_scheduled = db_post.is_scheduled

            db_message = self.db.telegram.get_updated_message(
                db_chat=db_post.telegram_channel.chat,
                raw_message=raw_message,
                logger_account=db_telegram_account,
            )
            if db_message is None:
                raise ValueError('could not store message in db')

            db_post.update_post_from_message(
                db_message=db_message
            )

            return BaseResponse().done('uploaded_successfully', data={
                'db_message_id': db_message.id,
                'album_id': db_message.media_group_id
            })
