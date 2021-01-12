from typing import Union

from django.db import models

from pyrogram import types
from .user import User


class UserUpdater:

    @staticmethod
    def update_or_create_user_from_raw(
            *,
            model: models.Model,
            field_name: str,
            raw_user: Union[types.User, types.UserFull]
    ):
        field = getattr(model, field_name, None)
        if field and not isinstance(field, User):
            return

        if field:
            if raw_user:
                field.update_fields_from_raw(raw_user=raw_user)
            else:
                setattr(model, field_name, None)
                model.save()
        else:
            if raw_user:
                setattr(
                    model,
                    field_name,
                    User.users.update_or_create_from_raw(
                        raw_user=raw_user
                    )
                )
                model.save()
