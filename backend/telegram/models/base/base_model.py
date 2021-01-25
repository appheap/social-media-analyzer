from db import models as db_models

base_url_telegram = 'telegram/'
base_url_users = 'users/'

site_user_profile_photos_url = base_url_users + 'profile_photos/'
telegram_user_profile_photos_url = base_url_telegram + 'user_profile_photos/'
telegram_chat_profile_photos_url = base_url_telegram + 'chat_profile_photos/'


class BaseModel(db_models.BaseModel):
    class Meta:
        abstract = True

    @staticmethod
    def file_dir_path(instance, filename):
        if instance.user:
            return telegram_user_profile_photos_url + 'user_{0}_{1}'.format(instance.user.user_id, filename)
        elif instance.chat:
            return telegram_chat_profile_photos_url + 'chat_{0}_{1}'.format(instance.chat.chat_id, filename)
        elif instance.site_user:
            return site_user_profile_photos_url + 'site_user_{0}_{1}'.format(instance.site_user.id, filename)
        else:
            raise ValueError(f'undefined instance {type(instance)}')
