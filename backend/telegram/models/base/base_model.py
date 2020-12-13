from db import models as db_models

base_url_telegram = 'telegram/'
telegram_profile_photos_url = base_url_telegram + 'profile_photos/'


class BaseModel(db_models.BaseModel):
    class Meta:
        abstract = True

    @staticmethod
    def file_dir_path(instance, filename):
        print(type(instance))
        from telegram import models as tg_models

        if isinstance(instance, tg_models.User):
            return telegram_profile_photos_url + 'user_{0}_{1}'.format(instance.user_id, filename)
        else:
            raise ValueError(f'undefined instance {type(instance)}')
